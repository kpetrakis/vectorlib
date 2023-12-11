import os
import sys
sys.path.append(os.getcwd())

from vectorlib import Vector3D as v3d
from collections import namedtuple

Line = namedtuple('Line', ['point', 'direction']) # point + t * direction

r1 = v3d((1, 2, 3)) # point in line
d1 = v3d((1, 0, 0)) # direction vector
line1 = Line(r1, d1)
r2 = v3d((4, 5, 6)) # point in line
d2 = v3d((0, 1, 0)) # direction vector
line2 = Line(r2, d2)
print(f"{'line1':<45s}: {line1}")
print(f"{'line2':<45s}: {line2}")
print(f"{'Agle between line1 and line2 (perpendicular)':<45s}: {v3d.angle(line1.direction, line2.direction)}")

line2 = Line(r2, d1)
print(f"{'line1':<45s}: {line1}")
print(f"{'line2':<45s}: {line2}")
#print("Agle between line1 and line2 (parallel):", v3d.angle(line1.direction, line2.direction))
print(f"{'Agle between line1 and line2 (parallel)':<45s}: {v3d.angle(line1.direction, line2.direction)}")

"""
line_eq = lambda t: r1 + t * d1 # vector equation of line
print("line(0)", line_eq(0))
print("line(1)", line_eq(1))
"""