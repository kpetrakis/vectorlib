# 3D Vector Library

## Example Usage

Some Basics operations:

```py
from vectorlib import Vector3D as v3d

x = v3d([1,2,3])
y = v3d.rand(seed=1234)

a = x + y
b = a * x + y**3
c += b + 1

d = v3d.dot(x, y)
d_norm = d.norm()
cros = v3d.cross(a, x)

b_unit = b.unit()

angle = v3d.angle(cros, d)

dis = v3d.dist(b, c)

projection = v3d.project(a, d)
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
python main.py -op dot -v1 1 2 3 -v2 1 2 3
```
Sample Output:
```bash
Dot product <v1, v2>          : 14.0
Cross product of (v1 x v2)    : Vector3D([0. 0. 0.])
Euclidean Distance (v1 - v2)  : 0.0
Angle between v1, v2          : 0.019782341029446364
v1 projection to v2           : Vector3D([0.99999994 1.9999999  2.9999998 ])
```

### Running examples

```bash
python examples/line_angles.py
python examples/plane_and_point.py
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

- [ ] add len
- [ ] add dtype conversion
