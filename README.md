# nnLB-NextPitch
## A Novel Deep Learning Approach to MLB Pitch Prediction Using In-Game Video Footage
### Abstract

The importance of analytics in baseball has grown considerably in recent decades. Accordingly, Major League Baseball (MLB) organizations have invested substantial resources into the research and development of advanced statistical methods that can be leveraged to gain competitive advantages. Pitch prediction has emerged as one of these active areas of research. Here we develop a novel deep learning approach for pitch prediction. Using pose estimation time-series data from in-game video footage, we train two pitcher-specific convolutional neural networks (CNNs) to predict the pitches of Tyler Glasnow (2019 season) and Walker Buehler (2021 season). Notably, our selected model achieves a prediction accuracy of 87.1% and an area under the curve (AUC) of 0.919 on a holdout test set for Tyler Glasnow's 2019 season. These results demonstrate the effectiveness of using in-game video footage and deep learning for pitch prediction tasks. 

The full HTML report for this repo can be found [here](https://github.com/BrentonGraham/nnLB-NextPitch/blob/main/docs/nnLB-nextpitch-report.html). We currently recommend that users download and view this this report locally for the best user experience.

### Feature Extraction Pipeline
Video → Image Conversion | Pitcher Detection & <br /> Background Blurring | OpenPose Pose Estimation
--- | --- | ---
![pipeline-step1-vid2images](https://user-images.githubusercontent.com/46132172/236989149-3f24ab40-9dc0-40a7-b7ac-5a22bdfc6be4.gif) | ![pipeline-step2-blur](https://user-images.githubusercontent.com/46132172/236989162-d2589707-df16-46cb-abee-929fafd33bb5.gif) | ![pipeline-step3-plot](https://user-images.githubusercontent.com/46132172/236989173-acc2302c-d6e5-49dc-9ed0-9b5993a6c843.gif)

### A Look at the Pose Estimation Time Series Data
Original Video | Pose Estimation of the Left Knee
--- | ---
![fig2-1](https://user-images.githubusercontent.com/46132172/236993590-ca7493dc-30a8-4df9-bdac-e35d77af50ee.gif) | ![fig2-2](https://user-images.githubusercontent.com/46132172/236993613-59b91d17-6348-47de-84bb-feeec1ecfdff.gif)

### Model Performance
#### Tyler Glasnow
![tyler-glasnow-cv-plot](https://user-images.githubusercontent.com/46132172/236987526-0fbfe195-bd55-45fd-bf00-46019d6ec031.png)
![tyler-glasnow-loss-plot](https://user-images.githubusercontent.com/46132172/236987712-518a3a28-1e1a-437c-8a43-3d3619d25d76.png)

#### Walker Buehler
![walker-buehler-cv-plot](https://user-images.githubusercontent.com/46132172/236987678-de258c18-0bed-45bd-b3cd-98969d6c4d57.png)
![walker-buehler-loss-plot](https://user-images.githubusercontent.com/46132172/236987730-df4f6a28-5de9-4896-a6e7-6f04fde901c8.png)
