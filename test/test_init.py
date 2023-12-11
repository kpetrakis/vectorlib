import unittest
import numpy as np
from vectorlib import Vector3D as v3d

class TestInitialization(unittest.TestCase):
  def setUp(self):
    self.v0 = v3d() # no args, should be all zeros
    self.v1 = v3d([1,2,3])

  def test_init(self):
    v = v3d((1,2,3))
    np.testing.assert_array_equal(np.array([1,2,3],dtype=np.float32), v.data)
    self.assertTrue(np.all(np.array([1,2,3],dtype=np.float32) == v.data))
    v = v3d([0.12531,1e-20,3.25e-15])
    np.testing.assert_array_equal(np.array([0.12531,1e-20,3.25e-15],dtype=np.float32), v.data)

    # test no args
    np.testing.assert_array_equal(np.zeros((3,), dtype=np.float32), self.v0.data)
    
    # test int, float, np.ndarray init
    v = v3d(1)
    np.testing.assert_array_equal(np.array([1,1,1],dtype=np.float32), v.data)
    v = v3d(5.312)
    np.testing.assert_array_equal(np.array([5.312,5.312,5.312],dtype=np.float32), v.data)
    v = v3d(np.array([0.5, 0.1, 0.25]))
    np.testing.assert_array_equal(np.array([0.5,0.1,0.25],dtype=np.float32), v.data)

  def test_rand(self):
    seed = 123456789
    rng = np.random.default_rng(seed=seed)
    np.testing.assert_array_equal(rng.random((3,), dtype=np.float32), v3d.rand(seed).data)
    
    # test reproducibility
    np.testing.assert_array_equal(v3d.rand(seed).data, v3d.rand(seed).data)

  def test_error_init(self):
    # error initializations
    self.assertRaises(Exception, lambda: v3d('a'))
    self.assertRaises(Exception, lambda: v3d([1]))
    self.assertRaises(Exception, lambda: v3d([1, 2]))
    self.assertRaises(Exception, lambda: v3d((1,2,'a')))
    self.assertRaises(Exception, lambda: v3d(np.array([1,2])))
    self.assertRaises(Exception, lambda: v3d(np.array(1)))
    #self.assertRaises(Exception, lambda: v3d((1,2,'3'))) # this will not raise exception

  def test_indexing(self):
    self.assertEqual(1.0, self.v1[0])
    self.assertEqual(2.0, self.v1[1])
    self.assertEqual(3.0, self.v1[2])
    self.assertRaises(Exception, lambda: self.v1[3])
    np.testing.assert_array_equal([1.0,2.0], self.v1[0:2])
    np.testing.assert_array_equal([1.0], self.v1[0:2:2])
    np.testing.assert_array_equal([1.0, 2.0, 3.0], self.v1[0:3])
    np.testing.assert_array_equal([1.0, 3.0], self.v1[0:3:2])
    np.testing.assert_array_equal([1.0, 3.0], self.v1[slice(0,3,2)])
    np.testing.assert_array_equal([], self.v1[3:])

  def test_assignment(self):
    self.v1[0] = 10
    self.assertEqual(10.0, self.v1[0])
    self.assertEqual(2.0, self.v1[1])
    self.assertEqual(3.0, self.v1[2])
    self.v1[0:2] = [10, 20]
    self.assertEqual(10.0, self.v1[0])
    self.assertEqual(20.0, self.v1[1])
    self.assertEqual(3.0, self.v1[2])
    with self.assertRaises(Exception):
      self.v1[3] = 10
      self.v1[0:2] = []
