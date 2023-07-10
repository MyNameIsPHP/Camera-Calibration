import cv2
import time

# Initialize the webcam
cap = cv2.VideoCapture(4)

# Set the frame width and height (adjust as needed)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Set the capture interval in seconds
capture_interval = 0.2

# Set the initial time
prev_capture_time = time.time()

i = 0
while True:
    # Read the current frame from the webcam
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow("Webcam", frame)

    # Calculate the time difference since the last capture
    current_time = time.time()
    elapsed_time = current_time - prev_capture_time

    # Check if the capture interval has elapsed
    if elapsed_time >= capture_interval:
        # Save the frame as an image
        image_name = f"capture_{current_time}.jpg"
        cv2.imwrite("image_"+str(i)+".jpg", frame)
        print(i)
        i+=1
        # Update the previous capture time
        prev_capture_time = current_time

    # Check for key press events
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()

