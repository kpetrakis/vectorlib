import numpy as np

'''
Numericaly stable implementions of some ops
I didn't use these functions. I just played with them after some tests failed
on some ops.
'''

def norm(x):
  return (np.abs(x)**2).sum() ** (1./2)

def robust_norm(x):
  '''
  a bit more robust against overflow
  https://timvieira.github.io/blog/post/2014/11/10/numerically-stable-p-norms/
  '''
  ## a bit hacky. For large numbers use robust to overflow
  #if np.log10(x.max()) > 10 or np.log10(x.min()) <10:
  a = np.abs(x).max()
  return a * norm(x / a)
  #else:
  #return norm(x)

def numericaly_stable_angle(x, y):
  '''
  a bit more robust near 0 and pi.
  https://github.com/pytorch/pytorch/issues/59194
  '''
  x_norm = x.norm()
  y_norm = y.norm()

  radians = 2 * np.arctan2(
    (x * y_norm - x_norm * y).norm(),
    (x * y_norm + x_norm * y).norm()
  )
  return np.degrees(radians)