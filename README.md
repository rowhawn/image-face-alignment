# image-face-alignment
script using openCV2 to align faces in a directory of images

## Input
- Directory of .jpg images

## Output
- Facially aligned .jpg images with original filename and suffix `_aligned` for each face recognized in image

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


## Running
```
cd image-face-alignment

python align_faces.py --shape-predictor "../resources/shape_predictor_68_face_landmarks.dat" --imageDir "<images directory>"
```
