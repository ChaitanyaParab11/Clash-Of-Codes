import cv2

def probability(imgpath):
    # load pre-trained Haar cascade for face detection
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # read input image
    img = cv2.imread(imgpath)

    # convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # create an array to store probabilities of having a face
    face_probs = []

    # loop over detected faces and calculate probabilities
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        # calculate probability by counting non-zero pixels in the grayscale ROI
        face_prob = cv2.countNonZero(roi_gray) / (roi_gray.shape[0] * roi_gray.shape[1])
        face_probs.append(face_prob)

    # print out the probabilities of having a face
    return face_probs
