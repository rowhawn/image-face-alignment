from os import listdir
from os.path import isfile, join
import argparse
import cv2

# Read images from a directory
# Display them and prompt user for a number estimate
# write out the images to a new directory with image filenames sorted by the estimated number


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--imageDir", required=True,
help="path to input image directory")
ap.add_argument("-o", "--outputDir", required=True,
help="path to output image directory")
args = vars(ap.parse_args())

img_dir_path = args["imageDir"]
output_dir_path = args["outputDir"]
onlyfiles = [f for f in listdir(img_dir_path) if isfile(join(img_dir_path, f)) and f.split(".")[1] == "jpg"]
image_rank_map = {}

for file in onlyfiles:
    img_file_name = f"{img_dir_path}/{file}"
    image = cv2.imread(img_file_name)
    cv2.imshow("Input", image)
    while True:
        rank = cv2.waitKey(0)
        if 48 < rank < 58:
            break

    if not image_rank_map.get(rank):
        image_rank_map[rank] = [image]
    else:
        image_rank_map[rank].append(image)

image_num = 0
for key in sorted(image_rank_map.keys()):
    for image_data in image_rank_map[key]:
        cv2.imwrite(f"{output_dir_path}/{'{:0>3d}'.format(image_num)}.jpg", image_data)
        image_num += 1
