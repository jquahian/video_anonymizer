import numpy as np
import cv2
import os

videos = os.listdir('Data')
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
width = 800
height = 600
frame_rate = 28.0

for i in range(0, len(videos)):
	file_path = os.path.join('Data', videos[i])
	output_path = os.path.join('Output', 'anon_' + videos[i])
	out = cv2.VideoWriter(output_path, fourcc, frame_rate, (width,height))
	cap = cv2.VideoCapture(file_path)

	while(cap.isOpened()):
	    ret, file_name = cap.read()

	    if ret == True:
		    # color argument uses BGR
		    cv2.rectangle(file_name,(0,0),(500,60),(66,40,33), -1)
		    
		    out.write(file_name)

		    cv2.imshow(videos[i], file_name)

		    if cv2.waitKey(1) & 0xFF == ord('q'):
		    	break
	    else:
	    	break

	print('now saving: ' + videos[i])

	cap.release()
	cv2.destroyAllWindows()	
