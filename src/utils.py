# Utility functions
from openpose import pyopenpose as op

def load_openpose_model():
    params = dict()
    params["model_folder"] = "path/to/openpose/models/"
    opWrapper = op.WrapperPython()
    opWrapper.configure(params)
    opWrapper.start()
    return opWrapper


    
