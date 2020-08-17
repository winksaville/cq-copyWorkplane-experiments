import sys

import cadquery as cq

obj1 = cq.Workplane("YZ").circle(1).extrude(10)
obj2 = cq.Workplane("XZ").circle(2).extrude(15)
obj3 = cq.Workplane("XY").box(10, 5, 1)

result = obj1.union(obj2).union(obj3)

