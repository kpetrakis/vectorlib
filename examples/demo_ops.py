import sys
import os
sys.path.append(os.getcwd())

from vectorlib import Vector3D as v3d

x = v3d([1,2,3])
y = v3d([0.35,10.93,1.78])
print(f"{'x':<30}: {x}")
print(f"{'y':<30}: {y}" )

r1 = 3*x - 4*y
print(f"{'3*x - 4*y':<30}:", r1)

r2 = x**3
print(f"{'x**3':<30s}:", r2)

r3 = x/5
print(f"{'(r3=) x / 5':<30}:", r3)
r3 += 1
print(f"{'r3 + 1':<30}:", r3)
print(f"{'5 / x':<30}:", 5/x)

r4 = (0.5 * x**(-2) + 2.5/x) / 3
print(f"{'(0.5 * x**(-2) + 2.5/x) / 3':<30}:", r4)
