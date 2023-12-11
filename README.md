# 3D Vector Library

## Example Usage

Some Basics operations:

```py
from vectorlib import Vector3D as v3d

e1 = v3d((1,0,0)) # x basis vector
x = v3d([1,2,3])
y = v3d.rand(seed=1234)

a = x + y
b = a * x + y**3
c = (3*x) / 10
c += b + 1

d = v3d.dot(x, y)
c_norm = c.norm()
cros = v3d.cross(a, x)

b_unit = b.unit()

angle = v3d.angle(cros, c)

dis = v3d.dist(b, c)

projection = v3d.project(a, e1)
```

## Installation

```bash
git clone https://github.com/kpetrakis/vectorlib.git 
cd vectorlib
virtualenv venv_name
source venv_name/bin/activate
pip install .
```

Note: If virtualenv is not available you can substitute:

```bash
virtualenv venv_name
```

with

```bash
python3 -m venv venv_name
```

## How to run

```bash
python main.py -op {dot, cross, dist, angle, project, all} -v1 {vector_values} -v2 {vector_values}
```

## Demonstration

```bash
python main.py -op all -v1 1 2 3 -v2 1 2 3
```

Sample Output:

```bash
Dot product <v1, v2>          : 14.0
Cross product of (v1 x v2)    : Vector3D([0. 0. 0.])
Euclidean Distance (v1 - v2)  : 0.0
Angle between v1, v2          : 0.019782341029446364
v1 projection to v2           : Vector3D([0.99999994 1.9999999  2.9999998 ])
```

## Running examples

```bash
python examples/line_angles.py
```

Sample Output:

```bash
line1                                        : Line(point=Vector3D([1. 2. 3.]), direction=Vector3D([1. 0. 0.]))
line2                                        : Line(point=Vector3D([4. 5. 6.]), direction=Vector3D([0. 1. 0.]))
Agle between line1 and line2 (perpendicular) : 90.0
line1                                        : Line(point=Vector3D([1. 2. 3.]), direction=Vector3D([1. 0. 0.]))
line2                                        : Line(point=Vector3D([4. 5. 6.]), direction=Vector3D([1. 0. 0.]))
Agle between line1 and line2 (parallel)      : 0.0

```

```bash
python examples/plane_and_point.py
```

Sample output:
```bash
xy-axis plane                                                         : Plane(a=Vector3D([1. 0. 0.]), b=Vector3D([0. 1. 0.]), normal=Vector3D([0. 0. 1.]))
Normal is pointing upward for xy_plane dot (dot==1)                   : 1.0
Normal is perpendicular to every vector in the plane (dot==0)         : 0.0
Normal is perpendicular to every vector in the plane (dot==0)         : 0.0
Distance between given point and the point xy_plane.a vector points to: 2.449489742783178
Projecting (xy_plane.a - point) to normal vector and taking the projection norm
Norm of point projection to the plane                                 : 2.0
It works for every point in the plane (same result as above)          : 2.0
```

### Running tests

```bash
python -m unittest -v test/test*
```

### Implementation details

- Python 3.11.5  
- numpy 1.24.3  
- It was tested on Artix Linux 6.5.7 and Ubuntu 22.04

### TODO

- [ ] add len functionality
- [ ] add dtype conversion
