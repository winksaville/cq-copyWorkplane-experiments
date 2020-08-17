import sys

import cadquery as cq


# obj = cq.Workplane("YZ").circle(1).extrude(10)
# show_object(obj, "obj.1")
# obj = obj.copyWorkplane(cq.Workplane("XZ")).circle(2).extrude(15)
# show_object(obj, "obj.2")
# obj = obj.copyWorkplane(cq.Workplane("XY")).box(10, 5, 1)
# show_object(obj, "obj.3")


obj = cq.Workplane("YZ").circle(1).extrude(10)
show_object(obj, "obj.1")
print(f"obj.1.all()={obj.all()}")
print(f"obj.1.parent.all()={obj.parent.all()}")
obj = obj.copyWorkplane(cq.Workplane("XZ")).circle(2).extrude(15)
show_object(obj, "obj.2")
print(f"obj.2.all()={obj.all()}")
print(f"obj.2.parent.all()={obj.parent.all()}")
obj = obj.copyWorkplane(cq.Workplane("XY"))
show_object(obj, "obj.3")
print(f"obj.3.all()={obj.all()}")
print(f"obj.3.parent.all()={obj.parent.all()}")

objx = obj.circle(2)
show_object(objx, "objx")
print(f"objx.all()={objx.all()}")
print(f"objx.parent.all()={objx.parent.all()}")

objy = objx.union()
show_object(objy, "objy")
print(f"objy.all()={objy.all()}")
print(f"objy.parent.all()={objy.parent.all()}")

#objy = objx.extrude(5, combine=False)
#show_object(objy, "objy")
#print(f"objy.all()={objy.all()}")
#print(f"objy.parent.all()={objy.parent.all()}")
