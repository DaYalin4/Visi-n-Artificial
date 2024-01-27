
import cv2

imagen = cv2.imread(r"D:\Users\Dayra\Documents\Cursos\VisionArtificial\Clase1\logo.jpg")


voltear1 = cv2.flip(imagen, 1)
voltear2 = cv2.flip(imagen, -1)
rotar1 = cv2.rotate(imagen, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("imagen original", imagen)
cv2.imshow("voltear", voltear1)
cv2.imshow("voltear 2", voltear2)
cv2.imshow("rotar", rotar1)

cv2.waitKey(0)


