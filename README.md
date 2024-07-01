# WorkoutTracker

I am developing a Python program to analyze CCTV footage from a gym to identify and count different workouts performed by users. The program should leverage computer vision techniques and machine learning models to detect specific exercises and count repetitions. Here's a detailed breakdown of the functionality required:

Project Requirements
Import Libraries: Import necessary libraries such as OpenCV, TensorFlow/Keras, and NumPy.

Load CCTV Footage: Load the CCTV footage from a specified directory.

Pre-process Footage:

Convert video frames to grayscale or RGB as required.
Resize frames for consistent input to the model.
Model for Activity Recognition:

Use a pre-trained deep learning model (e.g., YOLO, OpenPose) to detect human keypoints or recognize specific workout activities.
Fine-tune the model for gym-specific activities if necessary.
Activity Detection:

Implement logic to detect and classify different workouts such as squats, bench presses, and push-ups based on the recognized keypoints or model output.
Track movements over successive frames to count repetitions of each workout.
Output:

Display the identified workout and count of repetitions on each frame.
Save the processed video with annotations.
Optionally, output a summary report with counts of each detected workout.


WorkoutTracker/
│
├── models/                     # Directory for storing OpenPose models
│   ├── pose/                   # Pose models
│   │   ├── body_25/            # BODY_25 model files
│   │   ├── coco/               # COCO model files
│   │   └── mpi/                # MPI model files
│   └── face/                   # (Optional) Face model files
│
├── src/                        # Source code directory
│   ├── main.py                 # Main script for running the application
│   ├── detect_activities.py    # Module for activity detection logic
│   ├── preprocess_frame.py     # Module for frame preprocessing logic
│   ├── draw_annotations.py     # Module for drawing annotations on frames
│   ├── gui.py                  # Module for the GUI
│   └── utils.py                # Utility functions
│
├── data/                       # Directory for input videos and output data
│   ├── input/                  # Input videos
│   └── output/                 # Output files (JSON, etc.)
│
├── requirements.txt            # List of required Python packages
└── README.md                   # Project description and instructions


# Workout Tracker

This project uses OpenPose and OpenCV to detect and count workout activities from CCTV footage in a gym.

## Setup

1. Install the required Python packages:
   ```sh
   pip install -r requirements.txt

Detailed File Descriptions
models/: Directory containing the pre-trained OpenPose models.

pose/: Contains subdirectories for different pose models (BODY_25, COCO, MPI).
face/: (Optional) Contains face model files if facial keypoint detection is needed.
src/: Source code directory containing the following modules:

main.py: The main script that integrates all components and runs the application.
detect_activities.py: Contains logic for detecting and classifying different workouts.
preprocess_frame.py: Handles frame preprocessing (e.g., resizing, color conversion).
draw_annotations.py: Contains functions to draw annotations (e.g., detected activities, repetition counts) on frames.
gui.py: Implements the graphical user interface (GUI) for user interaction.
utils.py: Contains utility functions (e.g., for loading models, saving output).
data/: Directory for input videos and output data.

input/: Stores input video files.
output/: Stores output files such as JSON files with detected activities and counts.
requirements.txt: Lists all required Python packages (e.g., OpenCV, TensorFlow, OpenPose).

README.md: Provides an overview of the project, setup instructions, and usage guidelines.