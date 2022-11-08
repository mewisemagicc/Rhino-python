

##input rectangle
#crvGUID = rs.GetObject('select a rectangle', rs.filter.curve)
##rc.HideObject(CrvGUID)
#
##Find edit points
#pts = rs.CurveEditPoints(crvGUID)
#
##find centroid
#centroid = rs.CurveAreaCentroid(crvGUID) [0]
#
##create points in rhinospace
#rs.AddPoints(pts)
#rs.AddPoint(centroid)

#Inputting Points Lines and Shapes
import rhinoscriptsyntax as rs
import random as rnd

##bonestructure##
ptGUID = rs.GetObject('select a point', rs.filter.point)

#Randomly generate circle radius
radius = rnd.randint(5,15)
print radius

#draw a circle using point as origin
circle = rs.AddCircle(ptGUID, radius)

#divide circle - save points in a list
pts = rs.DivideCurve(circle, 8, True , True)

#label points
#rs.AddTextDot('pts[0]', pts[0])
#rs.AddTextDot('pts[1]', pts[1])
#rs.AddTextDot('pts[2]', pts[2])
#rs.AddTextDot('pts[3]', pts[3])
#rs.AddTextDot('pts[4]', pts[4])
#rs.AddTextDot('pts[5]', pts[5])
#rs.AddTextDot('pts[6]', pts[6])
#rs.AddTextDot('pts[7]', pts[7])

#add curve

rs.AddCurve((ptGUID, pts[0], pts[3], ptGUID), 4)
rs.AddCurve((ptGUID, pts[1], pts[4], ptGUID), 4)
rs.AddCurve((ptGUID, pts[2], pts[5], ptGUID), 4)
rs.AddCurve((ptGUID, pts[3], pts[6], ptGUID), 4)
rs.AddCurve((ptGUID, pts[4], pts[7], ptGUID), 4)
rs.AddCurve((ptGUID, pts[5], pts[0], ptGUID), 4)
rs.AddCurve((ptGUID, pts[6], pts[1], ptGUID), 4)
rs.AddCurve((ptGUID, pts[7], pts[2], ptGUID), 4)


rs.AddCurve((ptGUID, pts[0], pts[1], ptGUID))
rs.AddCurve((ptGUID, pts[1], pts[2], ptGUID))
rs.AddCurve((ptGUID, pts[2], pts[3], ptGUID))
rs.AddCurve((ptGUID, pts[3], pts[4], ptGUID))
rs.AddCurve((ptGUID, pts[4], pts[5], ptGUID))
rs.AddCurve((ptGUID, pts[5], pts[6], ptGUID))
rs.AddCurve((ptGUID, pts[6], pts[7], ptGUID))
rs.AddCurve((ptGUID, pts[7], pts[0], ptGUID))

rs.AddCurve((ptGUID, pts[0], pts[3], ptGUID), 1)
rs.AddCurve((ptGUID, pts[1], pts[4], ptGUID), 1)
rs.AddCurve((ptGUID, pts[2], pts[5], ptGUID), 1)
rs.AddCurve((ptGUID, pts[3], pts[6], ptGUID), 1)
rs.AddCurve((ptGUID, pts[4], pts[7], ptGUID), 1)
rs.AddCurve((ptGUID, pts[5], pts[0], ptGUID), 1)
rs.AddCurve((ptGUID, pts[6], pts[1], ptGUID), 1)
rs.AddCurve((ptGUID, pts[7], pts[2], ptGUID), 1)




