
import mediapipe as mp  
import cv2
import serial

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

try:
    puerto = serial.Serial("COM3", 9600, timeout=1)
except:
    print("No hubo conexión")

dedoPlg, dedoInd, dedoMed, dedoAnl, dedoMnq, dedos_detectados = 0, 0, 0, 0, 0 , 0
while True:
    ret, frame =  cap.read()
    #frame = cv2.flip(frame, 1)

    #transformar de BGR a RBG
    RGBframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #  (matriz)          nombre_objeto en formato RGB
    resultados = objeto_hands.process(RGBframe)

    if resultados.multi_hand_landmarks:
        for puntos in resultados.multi_hand_landmarks:

            #Para mostrar las lineas y todos los puntos detectados.
            #mp_dibujo.draw_landmarks(frame, puntos, mp_manos.HAND_CONNECTIONS)

            #valores del 0 al 1 en donde se encuentra cada dedo.
            dedo_pulgar = puntos.landmark[4]
            dedo_indice = puntos.landmark[8]
            dedo_medio = puntos.landmark[12]
            dedo_anular = puntos.landmark[16]
            dedo_menique = puntos.landmark[20]
            punto_central = puntos.landmark[5]
            
            alto, ancho, canales = frame.shape
            #para imprimir resolusión de la pantalla 
            #print(alto, ancho)

            #Lo multiplicamos para obtenerla en pixeles y no en flotante
            coorPlgX, coorPlgY = int(dedo_pulgar.x * ancho), int(dedo_pulgar.y * alto)
            coorIndX, coorIndY = int(dedo_indice.x * ancho), int(dedo_indice.y * alto)
            coorMedX, coorMedY = int(dedo_medio.x * ancho), int(dedo_medio.y * alto)
            coorAnlX, coorAnlY = int(dedo_anular.x * ancho), int(dedo_anular.y * alto)
            coorMnqX, coorMnqY = int(dedo_menique.x * ancho), int(dedo_menique.y * alto)

            coorCenX, coorCenY = int(punto_central.x * ancho), int(punto_central.y * alto)

            cv2.circle(frame, (coorPlgX,coorPlgY), 10, (0,255,0), thickness=-1)
            cv2.circle(frame, (coorIndX,coorIndY), 10, (0,255,0), thickness=-1)
            cv2.circle(frame, (coorMedX,coorMedY), 10, (0,255,0), thickness=-1)
            cv2.circle(frame, (coorAnlX,coorAnlY), 10, (0,255,0), thickness=-1)
            cv2.circle(frame, (coorMnqX,coorMnqY), 10, (0,255,0), thickness=-1)
            cv2.circle(frame, (coorCenX,coorCenY), 10, (0,0,255), thickness=-1)
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
            puerto.write(f"{dedoPlg}A{dedoInd}B{dedoMed}C{dedoAnl}D{dedoMnq}\n".encode())

    
    if dedos_detectados==1:
        cv2.putText(frame, f"Pulgar arriba", (100, 100), cv2.FONT_ITALIC, 1, (0,0,255), thickness=2)
    
    else:
        cv2.putText(frame, "No hay manos", (100, 100), cv2.FONT_ITALIC, 0.5, (0,0,255), thickness=2)
        dedos_detectados = 0

    cv2.imshow(ventana1, frame)
    salir = cv2.waitKey(1)
    if salir == 27:
        break

cap.release()
cv2.destroyAllWindows()



