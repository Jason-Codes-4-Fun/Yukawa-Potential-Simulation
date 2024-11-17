import bpy
import numpy as np

V_0 = .5
a = 1

#searches for plane
plane = bpy.data.objects.get("Plane")

#changes to object mode if needed
if bpy.context.object.mode != 'OBJECT':
    bpy.ops.object.mode_set(mode='OBJECT')
    

#code modifies the vertices of the plane as if it is a 3d graph
mesh = plane.data
for vertex in mesh.vertices:
    r = np.sqrt(vertex.co.x**2+vertex.co.y**2)
    vertex.co.z = -V_0*np.e**(-a*r)/r
mesh.update()