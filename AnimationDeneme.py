#CIRCLE ANIMATION EXAMPLE
import rhinoscriptsyntax as rs
import random as rnd

#input the number of frames you want to produce
num_of_frames = rs.GetInteger('Number of Frames to Output?', 240)
    
#loop through the number of frames creating the animation
for frame in range(num_of_frames):
    
#######________YOUR CODE GOES (INDENTED) BELOW THIS LINE________########
    #'frame' is your iteration variable - its simply counting from 0 to the maximum
    #number of frames that you input (num_of_frames)
    #use the 'frame' variable in your code to change something - to produce the 
    #animation.
    
    #create an empty list/dictionary
    ptDict = {}
    crvList = []

    #incremental loop to generate points
    for i in range(10):
        for j in range(10):
            #define x in terms of i
            #define y in terms of j
            x = i*1+(rnd.random()*frame/60)#+(i*i)
            y = j*1+(rnd.random()*frame/60)#+(j*j)
            z = 0
            
            #render point in rhinospace
#            rs.AddPoint(x,y,z)
            
            #save point values in a dictionary using (i,j) as a key
            ptDict[(i,j)] = (x,y,z)
        
    #loop through dictionary to create geometry
    for i in range(10):
        for j in range(10):
            ####  CREATE GEOMETRY  ####
            if i > 0 and j > 0:
                #find centroid of module using midPt of constructed line
                constLine = rs.AddLine(ptDict[(i,j)], ptDict[(i-1,j-1)])
                centroid = rs.CurveMidPoint(constLine)
                #delete constructed line
                rs.DeleteObject(constLine)
                
                
                #construct a closed curve from corner points
                crvList.append(rs.AddCurve((ptDict[(i,j-1)], ptDict[(i-1,j)],
                ptDict[(i-1,j-1)], ptDict[(i,j)], ptDict[(i,j-1)])))
                
                            #construct a closed curve from corner points
                crvList.append( rs.AddCurve((ptDict[(i-1,j)], ptDict[(i,j-1)],
                ptDict[(i-1,j-1)], ptDict[(i,j)], ptDict[(i-1,j)])))
                
    
#######________YOUR CODE GOES (INDENTED) ABOVE THIS LINE________########
    
    #Specify local folder to output frames -- you will need to change this to a
    #correct path on your computer
    render_folder = "C:\\Users\\gizem\\OneDrive\\Desktop\\Render\\"
    
    def render_step(render_folder, sequence_num):
        #Captures screenshots of the scene frame
        file_name = str(int(sequence_num)).zfill(5)
        file_path = " " + render_folder + file_name + ".png"
        rs.Command("_-ViewCaptureToFile" + file_path + " _Enter")
    
    #Call function to render frame
    render_step(render_folder, frame)
    
    #Clear canvas for the next frame -- 
    #YOU HAVE TO DELETE ALL THE OBJECTS YOU ARE RENDERING
    #This could also be optional if you want to overlay the frames of your animation
    #If you're deleteing a single object use rs.DeleteObject()
    #If you're deleteing a list of objects use rs.DeleteObjects()
    rs.DeleteObjects(crvList)
    
    