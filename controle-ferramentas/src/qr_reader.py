import cv2
from pyzbar.pyzbar import decode

def ler_qr_code():
    cap = cv2.VideoCapture(0)  # Abre a câmera

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Decodifica os QR codes encontrados na imagem
        decoded_objects = decode(frame)
        for obj in decoded_objects:
            # Extrai o texto do QR code
            qr_data = obj.data.decode('utf-8')
            cap.release()
            cv2.destroyAllWindows()
            return qr_data

        cv2.imshow("Ler QR Code", frame)

        # Pressione 'q' para sair do loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return None