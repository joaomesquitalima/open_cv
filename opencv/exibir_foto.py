import cv2 as cv
linkedin = cv.imread("opencv/fotos/linkedin.png")
#redimensiona imagem
pequena = cv.resize(linkedin,(400,400))

cv.imshow('tela',pequena)
cv.waitKey(0)
