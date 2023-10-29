import cv2 as cv
linkedin = cv.imread("C:/Users/mesqu/Desktop/python_testes/opencv/fotos/linkedin.png")
cara_chapeu = cv.imread("C:/Users/mesqu/Desktop/python_testes/opencv/fotos/cara_chapeu.png")


#redimensiona imagem
linkedin = cv.resize(linkedin,(400,400))
cara_chapeu = cv.resize(cara_chapeu,(400,400))

imagemSomada = cv.add(linkedin,cara_chapeu)
soma = linkedin - 255

cv.imshow('tela',linkedin)
cv.imshow('tela2',cara_chapeu)
cv.imshow('soma',imagemSomada)
cv.imshow("soma2",soma)

cv.waitKey(0)