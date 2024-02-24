
import mediapipe as mp  
import cv2

# sirve para dibujar con las utilidades de mediapipe
mp_dibujo = mp.solutions.drawing_utils

# para inicializar la solucion de detección de manos
mp_manos = mp.solutions.hands

objeto_hands = mp_manos.Hands(static_image_mode = False, 
                              max_num_hands = 2,
                              min_detection_confidence = 0.5)

cap = cv2.VideoCapture(1)

ventana1 = "Detección de manos"
cv2.namedWindow(ventana1, cv2.WINDOW_NORMAL)
cv2.resizeWindow(ventana1, 720, 420)

while True:
    #Para que detecte todo el tiempo 
    dedoPlg, dedoInd, dedoMed, dedoAnl, dedoMnq, dedos_detectados = 0, 0, 0, 0, 0 , 0
    ret, frame =  cap.read()
    RGBframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultados = objeto_hands.process(RGBframe)

    if resultados.multi_hand_landmarks:
        for puntos in resultados.multi_hand_landmarks:

            dedo_pulgar = puntos.landmark[4]
            dedo_indice = puntos.landmark[8]
            dedo_medio = puntos.landmark[12]
            dedo_anular = puntos.landmark[16]
            dedo_menique = puntos.landmark[20]
            punto_central = puntos.landmark[5]
            
            alto, ancho, canales = frame.shape
            
            #Lo multiplicamos para obtenerla en pixeles y no en flotante
            coorPlgX, coorPlgY = int(dedo_pulgar.x * ancho), int(dedo_pulgar.y * alto)
            coorIndX, coorIndY = int(dedo_indice.x * ancho), int(dedo_indice.y * alto)
            coorMedX, coorMedY = int(dedo_medio.x * ancho), int(dedo_medio.y * alto)
            coorAnlX, coorAnlY = int(dedo_anular.x * ancho), int(dedo_anular.y * alto)
            coorMnqX, coorMnqY = int(dedo_menique.x * ancho), int(dedo_menique.y * alto)

            coorCenX, coorCenY = int(punto_central.x * ancho), int(punto_central.y * alto)

            
            # Dedo pulgar
            dedoPlg = 1 if coorPlgX > coorCenX else 0
            # Dedo medio índice
            dedoInd = 1 if coorIndY < coorCenY else 0
            # Dedo medio
            dedoMed = 1 if coorMedY < coorCenY else 0
            # Dedo anular
            dedoAnl = 1 if coorAnlY < coorCenY else 0
            # Dedo meñique
            dedoMnq = 1 if coorMnqY < coorCenY else 0   

            dedos_detectados = dedoPlg + dedoInd + dedoMed + dedoAnl + dedoMnq
            
    #Cuando solo se detecta 1 dedo es el pulgar arriba y los demás dedos doblados.
    if dedos_detectados==1 :
        cv2.putText(frame, f"Pulgar arriba", (100, 100), cv2.FONT_ITALIC, 1.5, (0,0,255), thickness=2)
        
    elif dedos_detectados==0:
        cv2.putText(frame, "No hay manos", (100, 100), cv2.FONT_ITALIC, 2, (0,0,255), thickness=2)
    else: 
        cv2.putText(frame, f"Mano extendida", (100, 100), cv2.FONT_ITALIC, 2, (0,0,255), thickness=2)
    
    cv2.imshow(ventana1, frame)
    salir = cv2.waitKey(1)
    if salir == 27:
        break

cap.release()
cv2.destroyAllWindows()
