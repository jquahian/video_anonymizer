import numpy as np
import cv2
import os

videos = os.listdir('Data')
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

for i in range(0, len(videos)):
	file_path = os.path.join('Data', videos[i])
	cap = cv2.VideoCapture(file_path)

	# gets the fps, height, width from the source video
	frame_rate = cap.get(cv2.CAP_PROP_FPS)
	height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
	width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

	output_path = os.path.join('Output', 'anon_' + videos[i])
	out = cv2.VideoWriter(output_path, fourcc, frame_rate, (int(width),int(height)))

	while(cap.isOpened()):
	    ret, file_name = cap.read()

	    if ret == True:
		    # color argument uses BGR
		    cv2.rectangle(file_name,(0,0),(width,75),(0,0,0), -1)
		    
		    out.write(file_name)

		    cv2.imshow(videos[i], file_name)

		    if cv2.waitKey(1) & 0xFF == ord('q'):
		    	break
	    else:
	    	break

	print('now saving: ' + videos[i])

	cap.release()
	cv2.destroyAllWindows()	
