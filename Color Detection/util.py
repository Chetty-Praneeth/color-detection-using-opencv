import numpy as np
import cv2 as cv

# for detecting yellow colored objects
def get_limits(color):
    c = np.uint8([[color]])  # BGR values
    hsvC = cv.cvtColor(c, cv.COLOR_BGR2HSV)

    hue = hsvC[0][0][0]  # Get the hue value

    # Handle red hue wrap-around
    if hue >= 165:  # Upper limit for divided red hue
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([180, 255, 255], dtype=np.uint8)
    elif hue <= 15:  # Lower limit for divided red hue
        lowerLimit = np.array([0, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)
    else:
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit

# for detecting purple colored objects
def get_limits(color):
    c = np.uint8([[color]])  # BGR values
    hsvC = cv.cvtColor(c, cv.COLOR_BGR2HSV)

    hue = hsvC[0][0][0]  # Get the hue value

    # Purple hue range is generally between 125 and 150
    if 125 <= hue <= 150:  
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)
    else:
        # You might want to handle out-of-range colors, but for simplicity:
        lowerLimit = np.array([125, 100, 100], dtype=np.uint8)
        upperLimit = np.array([150, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit