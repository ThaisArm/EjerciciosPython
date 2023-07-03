import cv2

# Función para capturar rostros con la cámara y encerrarlos en un cuadrado
def capturar_rostros():
    # Cargar el clasificador pre-entrenado de detección de rostros
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Inicializar la cámara
    cap = cv2.VideoCapture(0)

    while True:
        # Leer el cuadro actual de la cámara
        ret, frame = cap.read()

        # Convertir la imagen a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detectar rostros en la imagen
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

        # Dibujar un rectángulo alrededor de cada rostro detectado
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Mostrar la imagen con los rostros detectados
        cv2.imshow('Capturando Rostros', frame)

        # Salir del bucle si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar los recursos y cerrar las ventanas
    cap.release()
    cv2.destroyAllWindows()

# Llamar a la función para capturar rostros
capturar_rostros()
