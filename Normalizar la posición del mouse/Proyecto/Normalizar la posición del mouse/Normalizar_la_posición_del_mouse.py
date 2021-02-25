
import numpy as np
import cv2 as cv

#SCREEN SIZE
ix,iy = 512,512

#number of decimals
nd = 2

# mouse callback function
def click_mouse(event,x,y,flags,param):
    global mx,my
    if event == cv.EVENT_LBUTTONDOWN:
        mx = map_values(x,0,ix,0,1)
        my = map_values(y,0,iy,0,1)
        print('x pos: ',round(mx,nd),', y pos: ' ,round(my,nd))
        print_value(x, y, mx, my)
        
# map two values (like processing)
# x1(from lower),y1(from upper),x2(to lower),y2(to upper)
def map_values(value, x1, y1, x2, y2):
   return (value - x1) / (y1 - x1) * (y2 - x2) + x2

#print in screen the values of the mouse position
#def print_value(x,y,vx,vy):
    #position= 'x:'+ str(round(vx,nd)) + ', y:' + str(round(vy,2))
    #cv.putText(img, position, (x,y), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 1)
    
        
# Create a black image, a window and bind the function to window
img = np.zeros((ix,iy,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',click_mouse)
while(1):
    cv.imshow('image',img)
    ch=0xFF & cv.waitKey()
    if ch==ord('q'):
        break
cv.destroyAllWindows()