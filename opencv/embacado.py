import cv2 as cv
linkedin = cv.imread("C:/Users/mesqu/Desktop/python_testes/opencv/fotos/pra.jpg", cv.IMREAD_GRAYSCALE)


#redimensiona imagem
pequena = cv.resize(linkedin,(400,700))
eq = cv.equalizeHist(pequena)


cv.imshow('tela',eq)
cv.imshow('tela2',pequena)
cv.waitKey(0)