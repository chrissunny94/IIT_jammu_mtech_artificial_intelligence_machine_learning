import cv2
import numpy as np
import requests
import os

def download_file(url, filename):
    """Downloads a file from a given URL and saves it to the specified filename."""
    if os.path.exists(filename):
        print(f"{filename} already exists. Skipping download.")
        return
    
    print(f"Downloading {filename} from {url}...")
    response = requests.get(url, stream=True)
    
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download {filename}. HTTP Status Code: {response.status_code}")

def initialize_yolo():
    """Initializes the YOLO model with pre-trained weights and configuration."""
    weights_url = 'https://pjreddie.com/media/files/yolov3.weights'
    cfg_url = 'https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg?raw=true'
    
    weights_filename = 'yolov3.weights'
    cfg_filename = 'yolov3.cfg'
    
    # Download YOLO files
    download_file(weights_url, weights_filename)
    download_file(cfg_url, cfg_filename)
    
    # Load YOLO model
    net = cv2.dnn.readNet(weights_filename, cfg_filename)
    layer_names = net.getLayerNames()
    
    # Handle different formats of getUnconnectedOutLayers() return value
    out_layers_indices = net.getUnconnectedOutLayers()
    if isinstance(out_layers_indices, np.ndarray):
        out_layers_indices = out_layers_indices.flatten()
    
    output_layers = [layer_names[i - 1] for i in out_layers_indices]
    
    return net, output_layers

def detect_objects(frame, net, output_layers):
    """Detects objects in the frame using YOLO."""
    height, width, channels = frame.shape
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    class_ids = []
    confidences = []
    boxes = []
    
    for out in outs:
        print(f"Shape of out: {out.shape}")  # Debug the shape of the output tensor
        for detection in out:
            for obj in detection:
                # Ensure obj is a numpy array
                if isinstance(obj, np.ndarray):
                    scores = obj[5:]  # The scores start from index 5
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    if confidence > 0.5:
                        center_x = int(obj[0] * width)
                        center_y = int(obj[1] * height)
                        w = int(obj[2] * width)
                        h = int(obj[3] * height)
                        x = int(center_x - w / 2)
                        y = int(center_y - h / 2)
                        boxes.append([x, y, w, h])
                        class_ids.append(class_id)
                        confidences.append(float(confidence))

    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    if len(indices) > 0:
        indices = indices.flatten()
        for i in indices:
            box = boxes[i]
            x, y, w, h = box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            label = str(class_ids[i])
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    return frame

def apply_segmentation(frame):
    """Applies image segmentation to the frame."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    segmented_image = frame.copy()
    cv2.drawContours(segmented_image, contours, -1, (0, 0, 255), 2)
    return segmented_image

def main():
    # Initialize YOLO
    net, output_layers = initialize_yolo()
    
    # Capture video from webcam
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Object Detection
        detected_frame = detect_objects(frame, net, output_layers)

        # Scene Analysis
        segmented_frame = apply_segmentation(detected_frame)

        # Display the results
        cv2.imshow('Object Detection and Scene Analysis', segmented_frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
