import pytest

import numpy as np
from numpy.testing import (
    assert_almost_equal,
    assert_array_equal,
    assert_allclose,
)

from skrmt.covariance import sample_estimator
from skrmt.covariance import FSOpt_estimator
from skrmt.covariance import loss_mv, prial_mv



def test_prial_sample():
    # population covariance matrix
    Sigma = np.array([[3.00407916, -1.46190757, 1.50140806, 1.50933526, 0.27036442],
                      [-1.46190757, 5.61441061, -0.51939653, -2.76492235, 1.38225566],
                      [1.50140806, -0.51939653, 2.3068582, 1.41248896, 0.84740175],
                      [1.50933526, -2.76492235, 1.41248896, 6.57182938, 0.73407095],
                      [0.27036442, 1.38225566, 0.84740175, 0.73407095, 9.50282265]])

    p, n = Sigma.shape[0], 3*Sigma.shape[0]
    # input data matrix
    X = np.random.multivariate_normal(np.random.randn(p), Sigma, size=n)

    sigma_sample = sample_estimator(X)
    sigma_fsopt = FSOpt_estimator(X, Sigma)

    E_Sn = loss_mv(Sigma_tilde=sigma_sample, Sigma=Sigma)
    E_Sigma_tilde = loss_mv(Sigma_tilde=sigma_sample, Sigma=Sigma)
    E_Sstar = loss_mv(Sigma_tilde=sigma_fsopt, Sigma=Sigma)

    prial = prial_mv(E_Sn=E_Sn, E_Sigma_tilde=E_Sigma_tilde, E_Sstar=E_Sstar)

    assert(prial == 0.0)


def test_prial_fsopt():
    # population covariance matrix
    Sigma = np.array([[3.00407916, -1.46190757, 1.50140806, 1.50933526, 0.27036442],
                      [-1.46190757, 5.61441061, -0.51939653, -2.76492235, 1.38225566],
                      [1.50140806, -0.51939653, 2.3068582, 1.41248896, 0.84740175],
                      [1.50933526, -2.76492235, 1.41248896, 6.57182938, 0.73407095],
                      [0.27036442, 1.38225566, 0.84740175, 0.73407095, 9.50282265]])

    p, n = Sigma.shape[0], 3*Sigma.shape[0]
    # input data matrix
    X = np.random.multivariate_normal(np.random.randn(p), Sigma, size=n)

    sigma_sample = sample_estimator(X)
    sigma_fsopt = FSOpt_estimator(X, Sigma)

    E_Sn = loss_mv(Sigma_tilde=sigma_sample, Sigma=Sigma)
    E_Sigma_tilde = loss_mv(Sigma_tilde=sigma_fsopt, Sigma=Sigma)
    E_Sstar = loss_mv(Sigma_tilde=sigma_fsopt, Sigma=Sigma)

    prial = prial_mv(E_Sn=E_Sn, E_Sigma_tilde=E_Sigma_tilde, E_Sstar=E_Sstar)

    assert(prial == 1.0)