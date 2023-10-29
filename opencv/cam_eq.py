import cv2 as cv

minhaWebcam = cv.VideoCapture(0,cv.CAP_DSHOW)
capturou, img = minhaWebcam.read()

while True:

    if capturou:
       

        b,g,r = cv.split(img)
        cores = ['b','g','r']
        be = cv.equalizeHist(b)
        ge = cv.equalizeHist(g)
        re = cv.equalizeHist(r)
        img_eq = cv.merge((be,ge,re))
        cv.imshow("Webcan",img_eq)
        cv.imshow('original',img)


        capturou, img = minhaWebcam.read()
        cv.waitKey(1)