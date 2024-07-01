import numpy as np
from openpose import pyopenpose as op

# Module for activity detection logic

def detect_activities(frame, model):
    datum = op.Datum()
    datum.cvInputData = frame
    model.emplaceAndPop([datum])
    keypoints = datum.poseKeypoints

    activities = []
    repetitions = []

    if keypoints is not None:
        for person in keypoints:
            # Detecting workouts based on keypoints
            if detect_squat(person):
                activities.append("squat")
                repetitions.append(count_repetitions(person))
            elif detect_pushup(person):
                activities.append("pushup")
                repetitions.append(count_repetitions(person))
            else:
                activities.append("unknown")
                repetitions.append(0)

    return activities, repetitions

def detect_squat(person):
    # Implement logic to detect squat exercise based on keypoints
    # Check if the keypoints for the knees and hips are present
    if person[9] is not None and person[10] is not None and person[11] is not None and person[12] is not None:
        # Calculate the angle between the knees and hips
        angle = calculate_angle(person[9], person[10], person[11], person[12])
        # Check if the angle is within a certain range (e.g., 70-100 degrees)
        if angle >= 70 and angle <= 100:
            return True
    return False

def calculate_angle(point1, point2, point3, point4):
    # Implement logic to calculate the angle between four points
    # Calculate the vectors between the points
    vector1 = np.array([point1[0] - point2[0], point1[1] - point2[1]])
    vector2 = np.array([point3[0] - point4[0], point3[1] - point4[1]])

    # Calculate the dot product of the vectors
    dot_product = np.dot(vector1, vector2)

    # Calculate the magnitudes of the vectors
    magnitude1 = np.linalg.norm(vector1)
    magnitude2 = np.linalg.norm(vector2)

    # Calculate the angle in radians
    angle_rad = np.arccos(dot_product / (magnitude1 * magnitude2))

    # Convert the angle to degrees
    angle_deg = np.degrees(angle_rad)

    # Return the calculated angle
    return angle_deg
    pass

def detect_pushup(person):
    # Check if the keypoints for the shoulders, elbows, and wrists are present
    if person[2] is not None and person[3] is not None and person[4] is not None and person[5] is not None and person[6] is not None and person[7] is not None:
        # Calculate the angle between the shoulders, elbows, and wrists
        angle1 = calculate_angle(person[2], person[3], person[4], person[5])
        angle2 = calculate_angle(person[3], person[4], person[5], person[6])
        angle3 = calculate_angle(person[4], person[5], person[6], person[7])
        # Check if the angles are within a certain range (e.g., 70-100 degrees)
        if angle1 >= 70 and angle1 <= 100 and angle2 >= 70 and angle2 <= 100 and angle3 >= 70 and angle3 <= 100:
            return True
    return False
    return False  # Placeholder

def count_repetitions(person):
    # Initialize variables
    previous_hand_y = None
    repetitions = 0

    # Iterate through the keypoints of the person
    for keypoint in person:
        # Check if the keypoint represents a hand (e.g., index 4 and 7)
        if keypoint is not None and (keypoint[1] == 4 or keypoint[1] == 7):
            current_hand_y = keypoint[0]

            # Check if this is the first iteration
            if previous_hand_y is None:
                previous_hand_y = current_hand_y
                continue

            # Check if the hand has moved from a lower position to a higher position
            if current_hand_y < previous_hand_y:
                repetitions += 1

            previous_hand_y = current_hand_y

    return repetitions