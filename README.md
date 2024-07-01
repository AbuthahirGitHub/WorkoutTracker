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
