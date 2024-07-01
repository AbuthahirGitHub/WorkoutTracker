import cv2
import json
import tkinter as tk
from tkinter import filedialog
from detect_activities import detect_activities
from preprocess_frame import preprocess_frame
from draw_annotations import draw_annotations
from utils import load_openpose_model

def load_video():
    root = tk.Tk()
    root.withdraw()
    try:
        video_path = filedialog.askopenfilename()
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise Exception("Failed to open video file")
    except Exception as e:
        print(f"Error: {str(e)}")
        return None, None
    return cap, video_path

def save_output(detected_activities, repetitions, video_path):
    output_data = {"video_path": video_path, "activities": detected_activities, "repetitions": repetitions}
    try:
        output_file = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        with open(output_file, 'w') as f:
            json.dump(output_data, f)
    except Exception as e:
        print(f"Error saving output: {str(e)}")

def main():
    root = tk.Tk()
    root.withdraw()
    
    cap, video_path = load_video()
    model = load_openpose_model()
    detected_activities = []
    repetitions = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        preprocessed_frame = preprocess_frame(frame)
        activities, reps = detect_activities(preprocessed_frame, model)
        detected_activities.extend(activities)
        repetitions.extend(reps)
        annotated_frame = draw_annotations(frame, activities, reps)
        
        cv2.imshow("Workout Tracker", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    save_output(detected_activities, repetitions, video_path)
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
