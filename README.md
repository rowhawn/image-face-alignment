# image-face-alignment
script using openCV2 to align faces in a directory of images

## Note
Supporting library file `facealigner.py` contains a bug. Update line 68 from 
```
eyesCenter = ((leftEyeCenter[0] + rightEyeCenter[0]) // 2,
    (leftEyeCenter[1] + rightEyeCenter[1]) // 2)
```
to 


```
eyesCenter = (int((leftEyeCenter[0] + rightEyeCenter[0]) // 2),
        int((leftEyeCenter[1] + rightEyeCenter[1]) // 2))
```


# Face alignment
## Input
- Directory of .jpg images

## Output
- Facially aligned .jpg images with original filename and suffix `_aligned` for each face recognized in image

## To Run
```
cd image-face-alignment

python align_faces.py --shape-predictor "../resources/shape_predictor_68_face_landmarks.dat" --imageDir "<images directory>"
```


# Image Ranker
## Input
- Directory of .jpg images

## Output
- Directory of .jpg images, in numerical order based on ranking metric

## To Run

```
cd image-face-alignment

python image-face-alignment/rank_faces.py --imageDir "<input images directory>" --outputDir "<output images directory>"
```
* User will be shown an image, and prompted to type number 1 through 9 on keyboard to indicate the rank of the displayed image. 