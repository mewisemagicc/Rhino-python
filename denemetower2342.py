#breathing facade
import rhinoscriptsyntax as rs

#creat base surface
circle1 = rs.AddCircle((0,0,0),1000)
circle2 = rs.AddCircle((0,0,3000),1500)
circle3 = rs.AddCircle((0,0,6000),1000)
circles = [circle1,circle2,circle3]
basesrf = rs.AddLoftSrf(circles)
rs.HideObject(basesrf)
rs.HideObjects(circles)

##create main body##
imax = 6 # number of stories
jmax = 20
udom = rs.SurfaceDomain(basesrf,0)
vdom = rs.SurfaceDomain(basesrf,1)
ustep= (udom[1]-udom[0])/imax
vstep= (vdom[1]-vdom[0])/jmax
pts = {}
for i in range(imax+1):
    for j in range(jmax+1):
            u = udom[0]+i*ustep
            v = vdom[0]+j*vstep
            point = rs.EvaluateSurface(basesrf,u,v)
            pts[(i,j)]=point

#creat slabs
floors = []
floor_thickness = 200
floor_hight = 6000/imax
for i in range(imax+1):
    j = 0
    radius = (pts[(i,j)][0]**2+pts[(i,j)][1]**2)**(0.5)
    base0 = (0,0,pts[(i,j)][2]-floor_thickness/2)
    base1 = (0,0,pts[(i,j)][2]+floor_thickness/2)
    line = rs.AddLine(base0,base1)
    floor = rs.AddPlanarSrf(rs.AddCircle(base0,radius+20))
rs.HideObject(floor)
floors.append(floor)
mat = rs.AddMaterialToObject(rs.ExtrudeSurface(floor,line))
rs.MaterialColor(mat,(70,70,70))

##creat outer lattice shell
I = 2*imax# number of stories
J = 10
udom = rs.SurfaceDomain(basesrf,0)
vdom = rs.SurfaceDomain(basesrf,1)
ustep= (udom[1]-udom[0])/I
vstep= (vdom[1]-vdom[0])/J
pts = {}
fpts = {}
for i in range(I+1):
    if i%2 == 0:
        for j in range(J):
                    u = udom[0]+i*ustep
                    v = vdom[0]+j*vstep
                    point = rs.EvaluateSurface(basesrf,u,v)
        vec = rs.SurfaceNormal(basesrf,(u,v))
        fvec = rs.VectorScale(vec,220)
        vec = rs.VectorScale(vec,200)
        pts[(i,j)] = rs.PointAdd(point,vec)
        fpts[(i,j)] = rs.PointAdd(point,fvec)
        line = rs.AddLine(point,pts[(i,j)])
        pipe = rs.AddPipe(line,0,30)
        mat = rs.AddMaterialToObject(pipe)
        rs.MaterialColor(mat,(160,160,160))
        #
                    #rs.AddPoint(point)
    else:
        for j in range(J):
                    u = udom[0]+i*ustep
                    v = vdom[0]+vstep/2+j*vstep
                    point = rs.EvaluateSurface(basesrf,u,v)
        vec = rs.SurfaceNormal(basesrf,(u,v))
        fvec = rs.VectorScale(vec,220)
        vec = rs.VectorScale(vec,200)
        pts[(i,j)] = rs.PointAdd(point,vec)
        fpts[(i,j)] = rs.PointAdd(point,fvec)
          #rs.AddPoint(point)
        #
for i in range(I+1):
    for j in range(J):
            sphere = rs.AddSphere(pts[(i,j)],40)
            mat = rs.AddMaterialToObject(sphere)
    rs.MaterialColor(mat,(160,160,160))

lines = []
for i in range(I+1):
    for j in range(J):
            p = j+1
    if p == J:
                p = 0
    lines.append(rs.AddLine(pts[(i,j)],pts[(i,p)]))

for i in range(I):
    for j in range(J):
        lines.append(rs.AddLine(pts[(i,j)],pts[(i+1,j)]))

for i in range(I):
    if i%2==0:
        for j in range(J):
            if j >0:
                lines.append(rs.AddLine(pts[(i,j)],pts[(i+1,j-1)]))
                lines.append(rs.AddLine(pts[(i,0)],pts[(i+1,J-1)]))
            else:
                for j in range(J-1):
                    lines.append(rs.AddLine(pts[(i,j)],pts[(i+1,j+1)]))
                    lines.append(rs.AddLine(pts[(i,J-1)],pts[(i+1,0)]))

for i in range(len(lines)):
    pipe = rs.AddPipe(lines[i],0,25)
    mat = rs.AddMaterialToObject(pipe)
rs.MaterialColor(mat,(160,160,160))

##creat facade##
trimeshes = []
for i in range(I):
    if i%2==0:
        for j in range(J):
            if j == 0:
                trimesh1 = rs.AddCurve((fpts[(i,j)],fpts[(i,j+1)],fpts[(i+1,j)],fpts[(i,j)]),1)
                trimesh2 = rs.AddCurve((fpts[(i,j)],fpts[(i+1,j)],fpts[(i+1,J-1)],fpts[(i,j)]),1)
trimeshes.append(trimesh1)
trimeshes.append(trimesh2)
else 0 < j < J-1:
                trimesh1 = rs.AddCurve((fpts[(i,j)],fpts[(i,j+1)],fpts[(i+1,j)],fpts[(i,j)]),1)
                trimesh2 = rs.AddCurve((fpts[(i,j)],fpts[(i+1,j)],fpts[(i+1,j-1)],fpts[(i,j)]),1)
trimeshes.append(trimesh1)
trimeshes.append(trimesh2)
else:
                trimesh1 = rs.AddCurve((fpts[(i,j)],fpts[(i,0)],fpts[(i+1,j)],fpts[(i,j)]),1)
                trimesh2 = rs.AddCurve((fpts[(i,j)],fpts[(i+1,j)],fpts[(i+1,j-1)],fpts[(i,j)]),1)
trimeshes.append(trimesh1)
trimeshes.append(trimesh2)
else:
for j in range(J):
if j < J-1:
                trimesh1 = rs.AddCurve((fpts[(i,j)],fpts[(i,j+1)],fpts[(i+1,j+1)],fpts[(i,j)]),1)
                trimesh2 = rs.AddCurve((fpts[(i,j)],fpts[(i+1,j+1)],fpts[(i+1,j)],fpts[(i,j)]),1)
trimeshes.append(trimesh1)
trimeshes.append(trimesh2)
else:
                trimesh1 = rs.AddCurve((fpts[(i,j)],fpts[(i,0)],fpts[(i+1,0)],fpts[(i,j)]),1)
                trimesh2 = rs.AddCurve((fpts[(i,j)],fpts[(i+1,0)],fpts[(i+1,j)],fpts[(i,j)]),1)
trimeshes.append(trimesh1)
trimeshes.append(trimesh2)

rs.HideObjects(trimeshes)

for iin range(len(trimeshes)):
    centroid = rs.CurveAreaCentroid(trimeshes[i])[0]
    plane = rs.AddPlanarSrf(trimeshes[i])
rs.HideObject(plane)
    vector = rs.SurfaceNormal(plane,(.5,.5))
    centroid1 = rs.CopyObject(centroid,-200*vector)
rs.HideObject(centroid1)
    points = rs.CurveEditPoints(trimeshes[i])
    curves = rs.ExplodeCurves(trimeshes[i])
    lines = []
ept = []
for j in range(len(curves)):
        mid = rs.CurveMidPoint(curves[j])
rs.HideObject(curves[j])
        line = rs.AddLine(centroid,mid)
rs.HideObject(line)
        l = rs.AddLine(centroid,mid)
rs.HideObject(l)
lines.append(l)
for j in range(len(lines)):
        length = rs.CurveLength(lines[j])
ept.append(rs.EvaluateCurve(lines[j],length*0.5))
    planes = []
planes.append(rs.AddSrfPt((points[0],ept[0],centroid1)))
planes.append(rs.AddSrfPt((points[1],centroid1,ept[0])))
planes.append(rs.AddSrfPt((points[1],ept[1],centroid1)))
planes.append(rs.AddSrfPt((points[2],centroid1,ept[1])))
planes.append(rs.AddSrfPt((points[2],ept[2],centroid1)))
planes.append(rs.AddSrfPt((points[0],centroid1,ept[2])))
for kin range(len(planes)):
        mat = rs.AddMaterialToObject(planes[k])
rs.MaterialColor(mat,(255,191,0))
