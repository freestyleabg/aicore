import cv2
from keras.models import load_model
import numpy as np
model = load_model('models/keras_model.h5')
cap = cv2.VideoCapture(4)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


def find_cv2_backends():
    available_backends = [cv2.videoio_registry.getBackendName(b) for b in cv2.videoio_registry.getBackends()]
    print(available_backends)


def find_camera_index():
    # Print the list of available cameras and their indices
    for i in range(5):  # Assuming there are at most 10 cameras
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f"Camera index {i} is available")
            cap.release()
        else:
            print(f"No camera found at index {i}")


while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame from the webcam.")
        break
    print("Original frame shape:", frame.shape)
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    print("Resized frame shape:", resized_frame.shape)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
