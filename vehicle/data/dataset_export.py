import cv2
import uuid
import os

cap = cv2.VideoCapture(0)

while cap.isOpened():
	ret, frame = cap.read()

	#recolor feed
	image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	#set flag
	image.flags.writeable = False

	#set flag to true
	image.flags.writeable = True

	#recolor image back to BGR for rendering (opencv love BGR)
	image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

	if cv2.waitKey(1) & 0xFF == ord('e'):
		cv2.imwrite(os.path.join('weights', '{}.jpg'.format(uuid.uuid1())), image)


	cv2.imshow('Raw Webcam Feed', image)

	if cv2.waitKey(10) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()