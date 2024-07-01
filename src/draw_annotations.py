import cv2

def draw_annotations(frame, detected_activities, repetitions):
    for i, (activity, count) in enumerate(zip(detected_activities, repetitions)):
        cv2.putText(frame, f'{activity}: {count}', (10, 30 * (i + 1)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    return frame
