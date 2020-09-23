import cv2
import sys

#set args
input_type = sys.argv[1] # i: image; v: video; d: directory
input_file = sys.argv[2]

if len(sys.argv) < 3:
    print("need argument")
    #handle less arguments
elif input_type == 'i': # input is a image
    img = cv2.imread(input_file)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(
            gray_img,
            scaleFactor=1.3,
            minNeighbors=3,
            minSize=(30, 30)
    )

    print("Found {0} Faces!".format(len(faces)))

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)
        cv2.imwrite('./data/1.jpg', img)

elif input_type == 'v':
    video = cv2.VideoCapture(input_file)
    frame_count = 0
    file_name = input_file.split('.')[-2].split('/')[-1]
    
    while(video.isOpened()):
        #print("reading")
        _, frame = video.read()

        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = faceCascade.detectMultiScale(
                gray_img,
                scaleFactor=1.3,
                minNeighbors=3,
                minSize=(30, 30)
        )

        #print("Found {0} Faces!".format(len(faces)))
        
        face_count = 0
        for (x, y, w, h) in faces:
            roi = frame[y:y + h, x:x + w] 
            cv2.imwrite('./data/%s_%d_%d.jpg'%(
                file_name,
                frame_count, 
                face_count
            ), roi)
            face_count += 1
        frame_count += 1
        
