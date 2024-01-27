
import cv2

ruta = r"D:\Users\Dayra\Documents\Cursos\VisionArtificial\Clase1\logo.jpg"
imagen = cv2.imread(ruta)

recorte = imagen[0:250, 0:250]

cv2.imshow("Imagen Original", imagen)
cv2.imshow("Imagen Recortada", recorte)

cv2.waitKey(0)



