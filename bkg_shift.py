from scipy.optimize import curve_fit
import numpy as np

catalyst_path = './dat/LaCe-NiO4_accum_r01.xyd'
support_path = './dat/LaCe600_accum_r01.xyd'

name = support_path.split('/')[-1].split('.')[0]

q, catalyst = np.loadtxt(catalyst_path).T
_, support = np.loadtxt(support_path).T

q_min, q_max = 3.158, 3.311
mask = q_max > q

q_peak = q[mask]
catalyst_peak = catalyst[mask]
support_peak = support[mask]


mask = q_peak > q_min

q_peak = q_peak[mask]
catalyst_peak = catalyst_peak[mask]
support_peak = support_peak[mask]


def gauss(q, mu, A, sigma):
    return A*np.exp(-(q-mu)**2/(2.*sigma**2))


(mu_catalyst, *_), (*_) = curve_fit(
        gauss, q_peak, catalyst_peak, maxfev=int(1e6)
    )
(mu_support, *_), (*_) = curve_fit(
        gauss, q_peak, support_peak, maxfev=int(1e6)
    )
stretch_in_q = mu_catalyst / mu_support


stretched_support = np.interp(q,  q * stretch_in_q, support)

np.savetxt(f'out/{name}_stretched.xy', np.array([q, stretched_support]).T)
