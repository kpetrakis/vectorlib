import time
import numpy as np
from typing import Union, Optional, List, Tuple

class Vector3D:
  '''
  Initialize a 3D Vector with the given values, or with zeros if no valueis given.
  Convention : All vectors have shape (3,) and are considered row vectors.

  :param data : the 3 values of the vector. can be a tuple, list, np.ndarray (of appropiate shape), 
  int or float
  '''
  def __init__(self, data:Optional[Union[int, float, List, Tuple, np.ndarray]]=None, dtype:Optional[Union[np.float32, np.float64]]=None):
    match data:
      case None:
        self.data = np.zeros((3,), dtype=np.float32)
      case list():
        assert len(data) == 3, f"You need to input a list or a tuple with 3 elements"
        self.data = np.array(data, dtype=np.float32) # default dtype=np.float32
      case tuple():
        assert len(data) == 3, f"You need to input a list or a tuple with 3 elements"
        self.data = np.array(data, dtype=np.float32) # default dtype=np.float32
      case np.ndarray():
        if data.shape == (3,):
          self.data = data.astype(np.float32)
        elif data.shape == (1, 3) or data.shape == (3,1): # row or column vector
          self.data = data.reshape(-1).astype(np.float32)
        else:
          raise(Exception(f"given array shape: {data.shape}, has to contain 3 elements"))
      case int(): # won't work for longs , e.g 1L
        self.data = np.array([data]*3, dtype=np.float32).reshape(-1)
      case float():
        self.data = np.array([data]*3, dtype=np.float32).reshape(-1)
      case _:
        raise(Exception(f"Cannot initialize vector from {type(data)}"))

  @property
  def dtype(self):
    return self.data.dtype

  @property
  def shape(self):
    return self.data.shape

  def norm(self):
    '''
    return the 2-norm of the vector
    '''
    return np.linalg.norm(self.data)#.item()

  def unit(self):
    '''
    return a unit vector with the same direction
    '''
    return Vector3D(self.data / self.norm())

  # NOTE: The way these ops are implemented they allow to do this like this: 
  # cross(3,2) translates to cross(Vector3D([3,3,3]), Vector3D([2,2,2]))
  # which is counterintuitive
  @staticmethod
  def cross(a, b):
    '''
    a x b: Direction of the result according to right hand rule 
    '''
    a = a if isinstance(a, Vector3D) else Vector3D(a)
    b = b if isinstance(b, Vector3D) else Vector3D(b)
    res = np.cross(a.data, b.data)
    return Vector3D(res)

  @staticmethod
  def dot(a, b):
    '''
    return the scalare value representing the dot product of a, b
    '''
    a = a if isinstance(a, Vector3D) else Vector3D(a)
    b = b if isinstance(b, Vector3D) else Vector3D(b)
    res = np.dot(a.data, b.data)
    # res = np.inner(a.data, b.data) # i think it's faster
    return res#.item()

  @staticmethod
  def angle(a, b):
    '''
    return angle theta between vectors a, b
    NOTE: arccos is ill-conditioned for angles near 0 or pi !!!
    '''
    theta_cos = Vector3D.dot(a, b) / (a.norm() * b.norm())
    # cliping is a bit hacky. I don't like it. But due to fp theta_cos can be > 1 and it breaks
    return np.degrees(np.arccos(theta_cos.clip(-1, 1)))
    # Didn't use it because we are told to use the dot product for angle calculation 
    # return numericaly_stable_angle(a,b) 

  @staticmethod
  def dist(a, b):
    a = a if isinstance(a, Vector3D) else Vector3D(a)
    b = b if isinstance(b, Vector3D) else Vector3D(b)
    #res = np.sqrt(np.sum((a.data - b.data)**2))
    res = (((a.data - b.data)**2).sum()) ** (1./2) # i think better numericaly
    return res#.item()

  @staticmethod
  def project(a, b):
    '''
    project vector a to vector b
    '''
    b_unit = b.unit()
    scalar_p = Vector3D.dot(a, b_unit) # scalar projection
    vector_p = scalar_p * b_unit
    return vector_p
    
  @staticmethod
  def rand(seed=int(time.time())):
    rng = np.random.default_rng(seed=seed)
    data = rng.random((3,), dtype=np.float32)
    return Vector3D(data)
    
  def __getitem__(self, i):
    return self.data[i]

  def __setitem__(self, key, val):
    self.data[key] = val 

  # NOTE : Element-wise ops
  def __add__(self, other):
    other = other if isinstance(other, Vector3D) else Vector3D(other)
    return Vector3D(self.data + other.data)

  def __mul__(self, other):
    other = other if isinstance(other, Vector3D) else Vector3D(other)
    return Vector3D(self.data * other.data)

  def __neg__(self):
    return self * (-1)

  def __sub__(self, other):
    return self + (-other)

  def __radd__(self, other):
    return self + other
  
  def __rsub__(self, other):
    return other + (-self)

  def __rmul__(self, other):
    return self * other

  def __pow__(self, other):
    return Vector3D(np.power(self.data, other))
  
  def __truediv__(self, other):
    return self * other**(-1)

  def __rtruediv__(self, other):
    return other * self**(-1)

  def __repr__(self):
    return f"Vector3D({self.data})" # add dtype info ?