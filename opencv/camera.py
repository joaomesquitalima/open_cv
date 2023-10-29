import cv2 as cv

minhaWebcam = cv.VideoCapture(0,cv.CAP_DSHOW)
capturou, img = minhaWebcam.read()

estatua = None


while True:

    if capturou:
       

        capturou, img = minhaWebcam.read()
       
       
        cv.imshow("tela",img)

        cv.waitKey(1)
        

           