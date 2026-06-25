import cv2
#from pyzbar.pyzbar import decode
from pyzbar.pyzbar import *

def scan_barcode():
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Could not open camera.")
        return None

    print("Camera opened. Hold a barcode up to the camera.")
    print("Press q to quit.")

    while True:
        success, frame = camera.read()

        if not success:
            print("Could not read from camera.")
            break

        barcodes = decode(frame)

        for barcode in barcodes:
            barcode_value = barcode.data.decode("utf-8")
            barcode_type = barcode.type

            camera.release()
            cv2.destroyAllWindows()

            return {
                "value": barcode_value,
                "type": barcode_type
            }

        cv2.imshow("Barcode Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()

    return None