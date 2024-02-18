import cv2
import numpy as np    

cap= cv2.VideoCapture(1)

ventana1 = "captura de video"
cv2.namedWindow(ventana1, cv2.WINDOW_NORMAL)
cv2.resizeWindow(ventana1, 720,400)

ventana2= "Mascara"
cv2.namedWindow(ventana2, cv2.WINDOW_NORMAL)
cv2.resizeWindow(ventana2, 720,400)

while True: 
    ret, frame = cap.read()
    hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #definir el rango de colores en formato HSV 
    colorMin = np.array([51, 102, 153])
    colorMax = np.array([102, 255, 255])

#                  imagenHSV 
    mascara = cv2.inRange(hsv, colorMin, colorMax)
    contornos, _= cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contornos)>0: 
        contorno_mas_grande= max(contornos, key=cv2.contourArea)
        (x,y), radio = cv2.minEnclosingCircle(contorno_mas_grande)
        x= int(x)
        y=int(y)
        radio = int(radio)
        cv2.circle(frame, (x,y), radio, (0,255,0), thickness=5)

        texto1 = "Color detectado"

        texto2 = "No se detecto color"

        if radio > 100:
            cv2.putText(frame, texto1, (100, 50), cv2.FONT_ITALIC, 2, (255,0,0), thickness=4)
        else:
            cv2.putText(frame, texto2, (100, 50), cv2.FONT_ITALIC, 2, (0,0,255), thickness=4)
 
    cv2.drawContours(frame, contornos,-1, [0,0,255])
    
    cv2.imshow(ventana1, frame)
    cv2.imshow(ventana2, mascara)

    salir = cv2.waitKey(1)
    if salir == 27 : 
        break
cap.release()
cv2.destroyAllWindows()