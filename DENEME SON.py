#3D SURFACE MATRIX

#import modules
import rhinoscriptsyntax as rs

def SurfacePoints(STRSRF, INTU, INTV):
    #create empty dictionary
    ptMTX = {}
    srfNorm = {}
    
    #find domain of surface
    Udomain = rs.SurfaceDomain(STRSRF,0)
    Vdomain = rs.SurfaceDomain(STRSRF,1)
    #print domain values
    print 'Udomain: ', Udomain
    print 'Vdomain: ', Vdomain
    
    #calculate step values
    stepU = (Udomain[1] - Udomain[0])/INTU
    stepV = (Vdomain[1] - Vdomain[0])/INTV
    #print step values
    print 'stepU: ', stepU
    print 'stepV: ', stepV
    
    #PLOT POINTS ON SURFACE
    for i in range(INTU+1):
        for j in range(INTV+1):
            #define u and v in terms of step values and i and j
            u = Udomain[0] + stepU * i
            v = Vdomain[0] + stepV * j
            
            #evaluate surface
            point = rs.EvaluateSurface(STRSRF, u, v)
            rs.AddPoint(point)
            ptMTX[(i,j)] = point
            
 
#                
#    #LOOP TO CREATE GEOMETRY
#    for i in range(INTU+1):
#        for j in range(INTV+1):
#            if i > 0 and j > 0:
#                                    ###  CREATE GEOMETRY  ####
#                    #CREATE BACK CURVE
#                    crvBack = rs.AddCurve((ptMTX[(i-1,j,vecNorm-1)], ptMTX[(i,j,vecNorm-1)],
#                    ptMTX[(i,j,vecNorm)], ptMTX[(i-1,j,vecNorm)], ptMTX[(i-1,j,vecNorm-1)]),1)
#                    CREATE FRONT CURVE
#                    create construction surface to find grid of points
#                    srf = rs.AddSrfPt((ptMTX[(i-1,j-1,vecNorm-1)], ptMTX[(i,j-1,vecNorm-1)], 
#                    ptMTX[(i,j-1,vecNorm)], ptMTX[(i-1,j-1,vecNorm)]))
#                    rebuild surface to create 4 x 4 grid (9 quadrants)
#                    rs.RebuildSurface(srf, (3,3), (4,4))
#                    extract points from grid
#                    pts = rs.SurfacePoints(srf)
#                    call function to reveal order of points
#                    numberPoints(pts)
#                    delete construction surface
#                    rs.DeleteObject(srf)
#                    generate random integer between 1 and 9 to select quadrant
#                    quadNum = rnd.randint(1,9)
#                    use quadNum to create front rectangle and sweep profile
#                    if quadNum == 1:
#                        crvFront = rs.AddCurve((pts[0],pts[4],pts[5],pts[1],pts[0]),1)
#                        profile = rs.AddLine(ptMTX[(i-1,j,vecNorm-1)], pts[0])
#                    if quadNum == 2:
#                        crvFront = rs.AddCurve((pts[1],pts[5],pts[6],pts[2],pts[1]),1)
#                        profile = rs.AddLine(ptMTX[(i-1,j,vecNorm-1)], pts[1])
#                    if quadNum == 3:
#                        crvFront = rs.AddCurve((pts[2],pts[6],pts[7],pts[3],pts[2]),1)
#                        profile = rs.AddLine(ptMTX[(i-1,j,vecNorm-1)], pts[2])
#                    if quadNum == 4:
#                        crvFront = rs.AddCurve((pts[4],pts[8],pts[9],pts[5],pts[4]),1)
#                        profile = rs.AddLine(ptMTX[(i-1,j,vecNorm-1)], pts[4])
#                    if quadNum == 5:
#                        crvFront = rs.AddCurve((pts[5],pts[9],pts[10],pts[6],pts[5]),1)
#                        profile = rs.AddLine(ptMTX[(i-1,j,vecNorm-1)], pts[5])
#                    if quadNum == 6:
#                        crvFront = rs.AddCurve((pts[6],pts[10],pts[11],pts[7],pts[6]),1)
#                        profile = rs.AddLine(ptMTX[(i-1,j,vecNorm-1)], pts[6])
#                    if quadNum == 7:
#                        crvFront = rs.AddCurve((pts[8],pts[12],pts[13],pts[9],pts[8]),1)
#                        profile = rs.AddLine(ptMTX[(i-1,j,vecNorm-1)], pts[8])
#                    if quadNum == 8:
#                        crvFront = rs.AddCurve((pts[9],pts[13],pts[14],pts[10],pts[9]),1)
#                        profile = rs.AddLine(ptMTX[(i-1,j,vecNorm-1)], pts[9])
#                    if quadNum == 9:
#                        crvFront = rs.AddCurve((pts[10],pts[14],pts[15],pts[11],pts[10]),1)
#                        profile = rs.AddLine(ptMTX[(i-1,j,vecNorm-1)], pts[10])
#                        
#                    translate curve variables into lists for use in rs.AddSweep2() function
#                    crvs = [crvBack,crvFront]
#                    profile = [profile]
#                    use sweep two rail to create surface geometry
#                    rs.AddSweep2(crvs, profile)
#                
def main():
    #collect data
    strSRF = rs.GetObject('select surface', rs.filter.surface)
    intU = rs.GetInteger('how many U intervals?', 8)
    intV = rs.GetInteger('how many V intervals?', 8)
    rs.HideObject(strSRF)
    #call function
    SurfacePoints(strSRF, intU, intV)
    
main()