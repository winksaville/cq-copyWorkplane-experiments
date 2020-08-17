import sys

import cadquery as cq

obj1 = cq.Workplane("YZ").circle(1).extrude(10)
obj2 = obj1.copyWorkplane(cq.Workplane("XZ")).circle(2).extrude(15)
obj3 = obj2.copyWorkplane(cq.Workplane("XY"))
log(f"obj3.all()={obj3.all()}")

obj4 = obj3.circle(2)
log(f"obj4.all()={obj4.all()}")

obj5 = obj4.extrude(2)
log(f"obj5.all()={obj5.all()}")

