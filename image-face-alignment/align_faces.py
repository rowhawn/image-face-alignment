from os import listdir
from os.path import isfile, join

# import the necessary packages
from imutils.face_utils import FaceAligner
from imutils.face_utils import rect_to_bb
import argparse
import imutils
import dlib
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
help="path to facial landmark predictor")
ap.add_argument("-i", "--imageDir", required=True,
help="path to input image directory")
args = vars(ap.parse_args())

img_dir_path = args["imageDir"]
onlyfiles = [f for f in listdir(img_dir_path) if isfile(join(img_dir_path, f)) and f.split(".")[1] == "jpg"]

for file in onlyfiles:
    print(f"Processing image {file}")
    img_file_name = f"{img_dir_path}/{file}"

    # initialize dlib's face detector (HOG-based) and then create
    # the facial landmark predictor and the face aligner
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(args["shape_predictor"])
    fa = FaceAligner(predictor, desiredFaceWidth=512)

    # load the input image, resize it, and convert it to grayscale
    image = cv2.imread(img_file_name)
    image = imutils.resize(image, width=800)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # show the original input image and detect faces in the grayscale
    # image
    cv2.imshow("Input", image)
    rects = detector(gray, 2)

    # loop over the face detections
    face_count = 0
    for rect in rects:
        face_count += 1
        # extract the ROI of the *original* face, then align the face
        # using facial landmarks
        (x, y, w, h) = rect_to_bb(rect)
        faceOrig = imutils.resize(image[y:y + h, x:x + w], width=256)
        faceAligned = fa.align(image, gray, rect)

        new_file_name = f"{img_file_name.split('.')[0]}_aligned_{face_count}.{img_file_name.split('.')[1]}"
        cv2.imwrite(new_file_name, faceAligned)
