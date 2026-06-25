import cv2
from pyzbar.pyzbar import decode


def scan_barcode():
    """
    Opens the computer's camera and waits for the user to scan a barcode.

    Once a barcode is detected, its value and barcode type are returned.
    If the user closes the scanner or no barcode is found, None is returned.

    Returns:
        dict:
            {
                "value": The barcode number or text.
                "type": The barcode format (EAN13, QR, Code128, etc.)
            }

        None:
            If no barcode was successfully scanned.
    """

    # Open the default camera (camera 0).
    camera = cv2.VideoCapture(0)

    # Check the camera opened successfully.
    if not camera.isOpened():
        print("Could not open camera.")
        return None

    print("Camera opened. Hold a barcode up to the camera.")
    print("Press q to quit.")

    # Continuously capture frames from the camera until
    # a barcode is found or the user quits.
    while True:

        # Read the next frame from the camera.
        success, frame = camera.read()

        if not success:
            print("Could not read from camera.")
            break

        # Search the current frame for any supported barcodes.
        barcodes = decode(frame)

        # If one or more barcodes are found, process the first one.
        for barcode in barcodes:

            # Convert the barcode bytes into readable text.
            barcode_value = barcode.data.decode("utf-8")

            # Determine the barcode format.
            barcode_type = barcode.type

            # Close the camera before returning the result.
            camera.release()
            cv2.destroyAllWindows()

            return {
                "value": barcode_value,
                "type": barcode_type
            }

        # Display the live camera feed.
        cv2.imshow("Barcode Scanner", frame)

        # Allow the user to quit by pressing the 'q' key.
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the camera resources if the loop exits.
    camera.release()
    cv2.destroyAllWindows()

    return None