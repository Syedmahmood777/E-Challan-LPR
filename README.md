# E-Challan-License Plate Recognition

## Project Overview
* Training a machine learning model to detect and recognize license plates.  
* Creating an electronic challan interface that uses the trained models.  
* Use the license plate extracted from the model to fetch challan details.  
* Visualizing all the data about challans based on different details.  
  
## Code and Resources Used
**OS**: Windows_NT x64 10.0.19045  
**Microsoft Visual Studio**: 1.90.0 (user setup)   
**Python**: 3.12  
**MongoDB**: 8.0
**Express.js**: 4.19.2  
**React.jS**: 18.2.0  
**Node.js**: 20.9.0  
**Tremor**: 3.16.3  
**Axios**: 1.7.2  
**Opencv Python**: 4.9.0.80
**Ultralytics**: 8.2.18
**Google Cloud Storage**: 1.25.0
**EasyOCR**: 1.7.1        
**Pillow**: 10.3.0

## Activity Diagrams

### HomePage
<img src="https://github.com/Syedmahmood777/E-Challan-LPR/blob/main/Activity/home1.png?raw=true" width="600" height="400" />

### Post-Image Upload & Fetch
<img src="https://github.com/Syedmahmood777/E-Challan-LPR/blob/main/Stats/retrieval.png?raw=true" width="600" height="400" />

### Visualization
<img src="https://github.com/Syedmahmood777/E-Challan-LPR/blob/main/Stats/graphs.PNG?raw=true" width="600" height="400" />
<img src="https://github.com/Syedmahmood777/E-Challan-LPR/blob/main/Stats/stats.PNG?raw=true" width="600" height="400" />



 ## Machine Learning Model
**Model Used**: YOLO V8 (Ultralytics)  
**GPU Used**: T4 GPU (Google Colab)
**Data Anottation Platform**: Roboflow  
**Dataset**: https://www.kaggle.com/datasets/saisirishan/indian-vehicle-dataset  
**Deployment**: Google Cloud Function APIs

### Model Stats
### F1-Confidence Curve
<img src="https://github.com/Syedmahmood777/E-Challan-LPR/blob/main/Stats/F1_curve.png?raw=true" width="600" height="400" />

### Precision Confidence Curve  
<img src="https://github.com/Syedmahmood777/E-Challan-LPR/blob/main/Stats/P_curve.png?raw=true" width="600" height="400" />  

### Precission-Recall Curve 
<img src="https://github.com/Syedmahmood777/E-Challan-LPR/blob/main/Stats/PR_curve.png?raw=true" width="600" height="400" />  

### Confusion Matrix
<img src="https://github.com/Syedmahmood777/E-Challan-LPR/blob/main/Stats/confusion_matrix.png?raw=true" width="600" height="400" />  

### Multiple Results

<img src="https://github.com/Syedmahmood777/E-Challan-LPR/blob/main/Stats/results.png?raw=true" width="600" height="400" />  

### Training Batch

<img src="https://github.com/Syedmahmood777/E-Challan-LPR/blob/main/Stats/train_batch0.jpg?raw=true" width="600" height="400" />  

### Validation Batch 

<img src="https://github.com/Syedmahmood777/E-Challan-LPR/blob/main/Stats/val_batch1_pred.jpg?raw=true" width="600" height="400" />    

### More stats are available in the main/Stats  


## Useful References
YOLO (You Only Look Once) Object Detection Model: <a href="https://www.ultralytics.com/">YOLO Official Website</a> 
EasyOCR Library: EasyOCR GitHub Repository
Google Cloud Functions Documentation: Google Cloud Functions
MERN Stack Guide: MERN Stack Guide
LDRS Icons :LDRS Github
MongoDB Setup, Fetching: Video Guide #1 , Video Guide #2   
React JS & API Guide :Video Guide
Tremor Guide : Video Guide
Node JS & MongoDB Connect: Video Guide




