import cv2
import rospy
from sensor_msgs.msg import Image
import time
import numpy as np

class MsgsCatcher:
    def __init__(self):
        self.img  = None
        self.frame2 = None

    def imagen(self,msg):
        self.frame2 = msg.data
        # for i in range(len(msg.data)):
        #     self.arr[i] = msg.data[i]
            
        # self.arreglo = ((self.arr).reshape(180,240)).astype(np.uint8) 

def saveVideo(frame2):
	arr = np.arange(43200)
	arreglo = np.zeros([180,240])

	if frame2 != None:
		lenf = len(frame2)
		for i in range(lenf):
			arr[i] = frame2[i]
   
		arreglo = (arr.reshape(180,240)).astype(np.uint8) 
	return arreglo
  
def main():
	print("Main")
	rospy.init_node('dvs_reader', anonymous=True)
	mcat = MsgsCatcher()
	rate = rospy.Rate(20.0)
	rospy.Subscriber('/dvs/image_raw', Image, mcat.imagen)

	c=0
	fourcc = cv2.VideoWriter_fourcc(*'MJPG')
	out = cv2.VideoWriter('save_videos/out_monoc_150.avi', fourcc, 15,(240,180)) 

 
	tt=0
	while True:
		st = time.time()
  
		if mcat.frame2!= None:
			arr = saveVideo(mcat.frame2)
			im_rgb = cv2.cvtColor(arr, cv2.COLOR_GRAY2RGB)
			out.write(im_rgb)
			cv2.imshow("video", im_rgb)
   
		et= time.time()
		tim = et-st
		tt = tt + tim
		c=c+1
		#print("tt:", tt)
  
		if (tt>= 1):
			print("**************fps: ",c)
			c=0
			tt=0
		
			
		if cv2.waitKey(1) == ord('q'):
			out.release()
			cv2.destroyAllWindows()
			break
	
		
   
	  
		#rospy.spin()

if __name__ == '__main__':
	try:	
		main()
	except: #rospy.ROSInterruptException:
		pass 
