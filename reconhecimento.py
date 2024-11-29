import face_recognition
import cv2

def processar_reconhecimento_facial(image_path):
    """
    Função para processar a imagem capturada e verificar faces.
    """
    # Carrega a imagem para o reconhecimento facial
    image = face_recognition.load_image_file(image_path)
    
    # Encontra todas as faces na imagem
    face_locations = face_recognition.face_locations(image)
    
    # Imprime o número de faces encontradas
    print(f"Faces encontradas na imagem: {len(face_locations)}")

    # Carrega a imagem com OpenCV para desenhar as caixas
    image_cv = cv2.imread(image_path)

    # Para cada face encontrada, desenha uma caixa ao redor
    for top, right, bottom, left in face_locations:
        cv2.rectangle(image_cv, (left, top), (right, bottom), (0, 255, 0), 2)

    # Salva a imagem com as caixas de reconhecimento facial desenhadas
    cv2.imwrite(image_path, image_cv)

    if len(face_locations) > 0:
        return f"Faces encontradas na imagem: {len(face_locations)}"
    else:
        return "Nenhuma face encontrada na imagem."