# nnLB-NextPitch
## A Novel Deep Learning Approach to MLB Pitch Prediction Using In-Game Video Footage
### Abstract

The importance of analytics in baseball has grown considerably in recent decades. Accordingly, Major League Baseball (MLB) organizations have invested substantial resources into the research and development of advanced statistical methods that can be leveraged to gain competitive advantages. Pitch prediction has emerged as one of these active areas of research. Here we develop a novel deep learning approach for pitch prediction. Using pose estimation time-series data from in-game video footage, we train two pitcher-specific convolutional neural networks (CNNs) to predict the pitches of Tyler Glasnow (2019 season) and Walker Buehler (2021 season). Notably, our selected model achieves a prediction accuracy of 87.1% and an area under the curve (AUC) of 0.919 on a holdout test set for Tyler Glasnow's 2019 season. These results demonstrate the effectiveness of using in-game video footage and deep learning for pitch prediction tasks.  

### Results
#### Tyler Glasnow
![tyler-glasnow-cv-plot](https://user-images.githubusercontent.com/46132172/236987526-0fbfe195-bd55-45fd-bf00-46019d6ec031.png)
![tyler-glasnow-loss-plot](https://user-images.githubusercontent.com/46132172/236987712-518a3a28-1e1a-437c-8a43-3d3619d25d76.png)

#### Walker Buehler
![walker-buehler-cv-plot](https://user-images.githubusercontent.com/46132172/236987678-de258c18-0bed-45bd-b3cd-98969d6c4d57.png)
![walker-buehler-loss-plot](https://user-images.githubusercontent.com/46132172/236987730-df4f6a28-5de9-4896-a6e7-6f04fde901c8.png)
