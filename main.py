import argparse
from vectorlib import Vector3D as v3d

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Vector3D Library')
  parser.add_argument("-op", "--operation", type=str, help="choose operation",
                      choices=['dot', 'cross', 'dist', 'angle', 'project', 'all'], required=True)
  parser.add_argument("-v1", "--vector1", type=int, nargs=3, help="first vector", required=True)
  parser.add_argument("-v2", "--vector2", type=int, nargs=3, help="second vector", required=True)
  args = vars(parser.parse_args())
  op = args['operation']
  v1 = args['vector1']
  v2 = args['vector2']
  v1, v2 = v3d(v1), v3d(v2)

  match op:
    case 'dot':
      res = v3d.dot(v1, v2)
      print(f"{'Dot product <v1, v2>':<30s}: {res}")
    case 'cross':
      res = v3d.cross(v1, v2) 
      print(f"{'Cross product of (v1 x v2)':<30s}: {res}")
    case 'dist':
      res = v3d.dist(v1, v2) 
      print(f"{'Euclidean Distance (v1 - v2)':<30s}: {res}")
    case 'angle':
      res = v3d.angle(v1, v2) 
      print(f"{'Angle between v1, v2':<30s}: {res}")
    case 'project':
      res = v3d.project(v1, v2)
      print(f"{'v1 projection to v2':<30s}: {res}")
    case 'all':
      print(f"{'Dot product <v1, v2>':<30s}: {v3d.dot(v1, v2)}")
      print(f"{'Cross product of (v1 x v2)':<30s}: {v3d.cross(v1, v2)}")
      print(f"{'Euclidean Distance (v1 - v2)':<30s}: {v3d.dist(v1, v2)}")
      print(f"{'Angle between v1, v2':<30s}: {v3d.angle(v1,v2)}")
      print(f"{'v1 projection to v2':<30s}: {v3d.project(v1, v2)}")
