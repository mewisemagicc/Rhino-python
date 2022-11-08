#Inputting Points Lines and Shapes
import rhinoscriptsyntax as rs
import random as rnd

#create an empty list
ptList = []

#imput values for imax and jmax
imax = rs.GetInteger('input number in x direction',10)
jmax = rs.GetInteger('input number in y direction',10)

#incremental loop to generate points
for i in range(imax):
    for j in range(jmax):
        #generate a random number between 0 and 1
        print rnd.random()
        #define x in terms of i
        #define y interms of j
        x = i * 5 + (rnd.random()*3)
        y = j * 5 + (rnd.random()*3)
        z = 0
        rs.AddPoint(x,y,z)
        
        ptList.append((x,y,z))
        
#loop through point lists and print out index number and values
for i in range (len(ptList)):
    ##create a transformation geometry
    #generate a random intiger within a range - use as radius
    #radius - 5 * rnd.random()
    radius = 5 * rnd.random()
    print radius
    if radius > 4:
        radius = 4
    elif radius < .25:
        radius = .25
    else :
        radius = radius
    
    
        rs.AddCircle(ptList[2], radius)
    
    