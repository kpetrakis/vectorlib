import os
import sys
sys.path.append(os.getcwd())

from vectorlib import Vector3D as v3d
from collections import namedtuple

# a and b are 2 linearly independent vectors on a plane and their cross product is the plane normal
Plane = namedtuple('Plane', ['a', 'b', 'normal']) 

# position of point relative to a plane
#----------------------
a = v3d([1,0,0])
b = v3d([0,1,0])
xy_plane = Plane(a, b, v3d.cross(a, b))
print(f"{'xy-axis plane':<70s}: {xy_plane}")
print(f"{'Normal is pointing upward for xy_plane dot (dot==1)':<70s}: {v3d.dot(v3d([0,0,1]), xy_plane.normal)}")
print(f"{'Normal is perpendicular to every vector in the plane (dot==0)':<70s}: {v3d.dot(a, xy_plane.normal)}")
print(f"{'Normal is perpendicular to every vector in the plane (dot==0)':<70s}: {v3d.dot(b, xy_plane.normal)}")

# example 1.4.5 : https://math.libretexts.org/Bookshelves/Calculus/CLP-3_Multivariable_Calculus_%28Feldman_Rechnitzer_and_Yeager%29/01%3A_Vectors_and_Geometry_in_Two_and_Three_Dimensions/1.04%3A_Equations_of_Planes_in_3d
point = v3d([0,1,-2])
print(f"{'Distance between given point and the point xy_plane.a vector points to':<70s}: {v3d.dist(point, xy_plane.a)}")
# Take the vector pointing from x to any given point in the plane. e.g  (xy_plane.a - point)
# Shortest distance between point and the plane == projection.norm(), projecting the above vector in the normal 
print(f"{'Projecting (xy_plane.a - point) to normal vector and taking the projection norm':<70s}")
print(f"{'Norm of point projection to the plane':<70s}: {v3d.project(xy_plane.a - point, xy_plane.normal).norm()}")
print(f"{'It works for every point in the plane (same result as above)':<70s}: {v3d.project(xy_plane.b - point, xy_plane.normal).norm()}")
