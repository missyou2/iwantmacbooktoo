#Reference: https://github.com/chocoluffy/faceEmoji/blob/master/face_detect.py
import cv2

# Read the image
image = cv2.imread("C:/Users/yckhb/Desktop/start.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# try to add a emoji to a existing face
s_img = cv2.imread("C:/Users/yckhb/Desktop/tear.png") #Call the emoji file
s_height, s_width, s_channels = s_img.shape
l_img = image

'''
# Draw a rectangle around the faces
resized = False
for (x, y, w, h) in faces:
    # cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    resize_ratio = round(w*10/(10.0*s_width), 2)
    # print "width " + str(w)
    if not resized:
    	s_img = cv2.resize(s_img, (0,0), fx= resize_ratio, fy= resize_ratio) 
    	resized = True
    x_offset = x
    y_offset = y
    l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img
'''
x_offset = y_offset = 30
l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img #Add emoji picture to original picture
cv2.imwrite("C:/Users/yckhb/Desktop/result-emoji.jpg", image) #Save the result
cv2.imshow("Faces found", image) #Show
cv2.waitKey(0)


'''
# Reference : https://deep-eye.tistory.com/18#google_vignette
import timeit
# 영상 검출기
def videoDetector(cam,cascade):
    while True:
        start_t = timeit.default_timer()
        # 캡처 이미지 불러오기
        ret,img = cam.read()
        # 영상 압축
        img = cv2.resize(img,dsize=None,fx=1.0,fy=1.0)
        # 그레이 스케일 변환
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        # cascade 얼굴 탐지 알고리즘 
        results = cascade.detectMultiScale(gray,            # 입력 이미지
                                           scaleFactor= 1.1,# 이미지 피라미드 스케일 factor
                                           minNeighbors=5,  # 인접 객체 최소 거리 픽셀
                                           minSize=(20,20)  # 탐지 객체 최소 크기
                                           )
                                                                           
        for box in results:
            x, y, w, h = box
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,255), thickness=2)
        # 알고리즘 종료 시점
        terminate_t = timeit.default_timer()
        FPS = 'fps' + str(int(1./(terminate_t - start_t )))
        cv2.putText(img,FPS,(30,30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1)
         # 영상 출력        
        cv2.imshow('facenet',img) 
        if cv2.waitKey(1) > 0:
            break
# 가중치 파일 경로
cascade_filename = 'C:/Users/yckhb/School/OSS/haarcascade_frontalface_alt.xml'
# 모델 불러오기
cascade = cv2.CascadeClassifier(cascade_filename)
# 영상 파일 
cam = cv2.VideoCapture('C:/Users/yckhb/Videos/Captures/sample.mp4')
videoDetector(cam,cascade)
'''