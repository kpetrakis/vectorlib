import unittest
import numpy as np
from vectorlib import Vector3D as v3d

class TestOps(unittest.TestCase):
  def setUp(self):
    rng = np.random.default_rng(123456789) # reproducibility
    self.e1 = v3d((1,0,0))
    self.e2 = v3d((0,1,0))
    self.e3 = v3d((0,0,1))
    #self.v1 = v3d(())
    #self.v2 = v3d(())

    # 3D vectors with random values
    self.r1 = v3d(rng.random((3,), dtype=np.float32))
    self.r2 = v3d(rng.random((3,), dtype=np.float32))

  def test_cross(self):
    # test right hand rule
    cross = v3d.cross(self.e1, self.e2)
    np.testing.assert_array_equal(np.array([0,0,1], dtype=np.float32), cross.data)
    cross = v3d.cross(self.e1, self.e3)
    np.testing.assert_array_equal(np.array([0,-1,0], dtype=np.float32), cross.data)

    # test anti-commutative property
    cross1 = v3d.cross(self.e1, self.e2)
    cross2 = v3d.cross(self.e2, self.e1)
    np.testing.assert_array_equal(cross1.data, -cross2.data)

    # test that axb (and bxa) is perpedicular to both a and b
    self.assertEqual(0, v3d.dot(cross1, self.e1))
    self.assertEqual(0, v3d.dot(cross1, self.e2))
    self.assertEqual(0, v3d.dot(cross2, self.e1))
    self.assertEqual(0, v3d.dot(cross2, self.e2))

    # test cross in perpendicular to both r1 and r2
    cross1 = v3d.cross(self.r1, self.r2)
    cross2 = v3d.cross(self.r2, self.r1)
    np.testing.assert_allclose(0, v3d.dot(cross1, self.r1), rtol=1e-7,atol=1e-7)
    np.testing.assert_allclose(0, v3d.dot(cross1, self.r2), rtol=1e-7,atol=1e-7)
    # test anti-commutative for r1 and r2
    np.testing.assert_array_equal(cross1.data, -cross2.data)

  def test_dot(self):
    self.assertEqual(0, v3d.dot(self.e1, self.e2))
    self.assertEqual(0, v3d.dot(self.e1, self.e3))
    self.assertEqual(0, v3d.dot(self.e2, self.e3))

    v1 = v3d([1,2,3])
    v2 = v3d([1,2,3])
    self.assertEqual(14, v3d.dot(v1, v2))
    # NOTE: This breaks! for 1.000001, dot=14.000000953674316
    v1 = v3d([1.000001,2,3])
    #self.assertEqual(14.0, v3d.dot(v1, v2)) # this would fail
    np.testing.assert_allclose(14, v3d.dot(v1, v2))

    # test on random values
    #np.testing.assert_allclose(1.3422075087550905, v3d.dot(self.r1, self.r2))
    np.testing.assert_allclose(1.3422075486137928, v3d.dot(self.r1, self.r2))

  def test_dist(self):
    np.testing.assert_allclose(np.sqrt(2), v3d.dist(self.e1, self.e2))
    np.testing.assert_allclose(np.sqrt(2), v3d.dist(self.e1, self.e3))
    np.testing.assert_allclose(np.sqrt(2), v3d.dist(self.e2, self.e3))

    # commutative
    np.testing.assert_allclose(v3d.dist(self.e1, self.e2), v3d.dist(self.e2, self.e1))

    v1 = v3d((1,0,5))
    v2 = v3d((0,2,4))
    np.testing.assert_allclose(np.sqrt(6), v3d.dist(v1, v2))
    np.testing.assert_allclose(np.sqrt(6), v3d.dist(v2, v1))
    # commutative
    np.testing.assert_allclose(v3d.dist(v1, v2), v3d.dist(v2, v1))

  def test_norm(self):
    self.assertEqual(1, self.e1.norm())
    self.assertEqual(1, self.e2.norm())
    self.assertEqual(1, self.e3.norm())

    np.testing.assert_allclose(1.074744, self.r1.norm(), rtol=1e-6)
    np.testing.assert_allclose(1.309554, self.r2.norm(), rtol=1e-6)

  def test_unit(self):
    np.testing.assert_array_equal(self.e1.data, self.e1.unit().data)
    np.testing.assert_array_equal(self.e2.data, self.e2.unit().data)
    np.testing.assert_array_equal(self.e3.data, self.e3.unit().data)
    v1 = v3d([1,2,3])
    # Test that unit norm equals 1
    #self.assertEqual(1, v1.unit().norm()) # this breaks
    np.testing.assert_allclose(1.0, v1.unit().norm())
    np.testing.assert_allclose(1.0, self.r1.unit().norm())
    np.testing.assert_allclose(1.0, self.r2.unit().norm())

  def test_angle(self):
    self.assertEqual(90.0, v3d.angle(self.e1, self.e2))
    self.assertEqual(90.0, v3d.angle(self.e1, self.e3))
    self.assertEqual(90.0, v3d.angle(self.e2, self.e3))
    self.assertEqual(90.0, v3d.angle(self.e1, -self.e2))

    self.assertEqual(0.0, v3d.angle(self.e1, self.e1))
    self.assertEqual(180.0, v3d.angle(self.e1, -self.e1))
    self.assertEqual(90., v3d.angle(self.e2, self.e3))

    # test parallel
    self.assertEqual(0, v3d.angle(v3d([0.1, 0, 0]), v3d([0.5, 0, 0])))

    # test commutative
    self.assertEqual(v3d.angle(self.r1, self.r2), v3d.angle(self.r2, self.r1))

  def test_project(self):
    np.testing.assert_array_equal(v3d((0,0,0)).data, v3d.project(self.e1, self.e2).data)
    np.testing.assert_array_equal(v3d((0,0,0)).data, v3d.project(self.e1, self.e3).data)
    np.testing.assert_array_equal(v3d((1,0,0)).data, v3d.project(self.e1, -self.e1).data)

    # test projection on basis vectors
    p1 = v3d.project(self.r1, self.e1)
    p2 = v3d.project(self.r1, self.e2)
    p3 = v3d.project(self.r1, self.e3)

    self.assertEqual(self.r1[0], p1[0])
    self.assertEqual(self.r1[1], p2[1])
    self.assertEqual(self.r1[2], p3[2])
    np.testing.assert_array_equal(self.r1.data[0], p1.data[0])
    np.testing.assert_array_equal(self.r1.data[1], p2.data[1])
    np.testing.assert_array_equal(self.r1.data[2], p3.data[2])

    # test projection has the same angle between initial vector
    p = v3d.project(self.r1, self.r2)
    np.testing.assert_array_equal(v3d.angle(self.r1, self.r2), v3d.angle(p, self.r1))
    np.testing.assert_allclose(v3d.angle(self.r1, self.r2), v3d.angle(p, self.r1), rtol=1e-7)
    # test projecting one on the other, the angle should remain the same
    np.testing.assert_allclose(v3d.angle(self.r1,self.r2), v3d.angle(v3d.project(self.r1, self.r2), v3d.project(self.r2, self.r1)))