#include "EKF.h"

using namespace boost::numeric;

/**
 * Simplest constructor for the EKF class
 *
 * @param dimension The number of dimensions (states) for the EKF to track.
 * @param _beta The assumed absolute increase in uncertainty per frame
 * @param _gamma The uncertainty scaling factor per frame
 */
EKF::EKF(unsigned int dimension, float _beta, float _gamma)
    : xhat_k(dimension), xhat_k_bar(dimension),
      Q_k(dimension,dimension), A_k(dimension,dimension),
      P_k(dimension,dimension), P_k_bar(dimension,dimension),
      dimensionIdentity(dimension), numStates(dimension),
      beta(_beta), gamma(_gamma)
{
    // Initialize all matrix values to 0
    for(unsigned i = 0; i < dimension; ++i) {
        for(unsigned j = 0; j < dimension; ++j) {
            Q_k(i,j) = 0.0f;
            A_k(i,j) = 0.0f;
            P_k(i,j) = 0.0f;
            P_k_bar(i,j) = 0.0f;
        }
        xhat_k(i) = 0.0f;
        xhat_k_bar(i) = 0.0f;
    }
}

/**
 * Function to calculate the required steps of the EKF time update.
 * Implementing classes must implement associateTimeUpdate to return the change
 * in estimate based on the inputed MotionModel u_k.
 *
 * @param u_k - the MotionModel showing the estimate change since the last time
 * update.
 */
void EKF::timeUpdate(MotionModel u_k)
{
    // Have the time update prediction incorporated
    // i.e. odometery, natural roll, etc.
    ublas::vector<float> deltas = associateTimeUpdate(u_k);
    xhat_k_bar = xhat_k + deltas;

    // Calculate the uncertainty growth for the current update
    for(unsigned int i = 0; i < numStates; ++i) {
        Q_k(i,i) = beta + gamma * deltas(i) * deltas(i);
    }

    // Update error covariance matrix
    ublas::matrix<float> newP = prod(P_k, trans(A_k));
    P_k_bar = prod(A_k, newP) + Q_k;
}

/**
 * Function to perform the correction step of the EKF. Implementing classes must
 * implement the incorporateMeasurement, to set H_k, R_k, and return v_k
 *
 * @param z_k - All measurements to be incoporated at the current update.
 */
void EKF::correctionStep(std::vector<Measurement> z_k)
{
    // Necessary computational matrices
    // Kalman gain matrix
    ublas::matrix<float> K_k = ublas::scalar_matrix<float>(numStates, 2, 0.0f);
    // Observation jacobian
    ublas::matrix<float> H_k = ublas::scalar_matrix<float>(2, numStates, 0.0f);
    // Assumed error in measurment sensors
    ublas::matrix<float> R_k = ublas::scalar_matrix<float>(2, 2, 0.0f);
    // Measurement invariance
    ublas::vector<float> v_k(2);

    // Incorporate all correction observations
    for(unsigned int i = 0; i < z_k.size(); ++i) {
        incorporateMeasurement(z_k[i], H_k, R_k, v_k);

        // Calculate the Kalman gain matrix
        ublas::matrix<float> pTimesHTrans = prod(P_k_bar, trans(H_k));
        K_k = prod(pTimesHTrans, invert2by2(prod(H_k, pTimesHTrans) + R_k));

        // Use the Kalman gain matrix to determine the next estimate
        xhat_k_bar = xhat_k_bar + prod(K_k, v_k);

        // Update associate uncertainty
        P_k_bar = prod(dimensionIdentity - prod(K_k,H_k), P_k_bar);
    }
    xhat_k = xhat_k_bar;
    P_k = P_k_bar;
}

/**
 * Function to update necessary information when there is noCorrectionStep.
 * Should be called at every timeUpdate which has no correctionStep.
 */
void EKF::noCorrectionStep()
{
    // Set current estimates to a priori estimates
    xhat_k = xhat_k_bar;
    P_k = P_k_bar;
}

/**
Invert a two by two matrix easily
given:
 [a b
  c d]
return:
(1/(ad - bc)) [ d -b
               -c  a]
@param m the 2 by 2 matrix to invert.
@return the inversion of m
 */
ublas::matrix<float> invert2by2(ublas::matrix<float> m)
{
    float det = 1.0f / ( m(0,0) * m(1,1) - m(0,1) * m(1,0));
    float tmp = m(0,0);
    m(0,0) = m(1,1);
    m(1,1) = tmp;
    tmp = -m(0,1);
    m(0,1) = -m(1,0);
    m(1,0) = tmp;
    return det * m;
}
