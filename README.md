

# Height Estimation in video surveillance - Machine Learning

Height Estimation using Machine learning algorithms in Open CV python. 

# Abstract <br/>

This paper presents a simple method for estimating human height in video surveillance. Most cameras for video surveillance are installed in high positions at a slightly tilted angle, it is possible to retain human height using the tilt angle. Certain parameters such as reference height, detected pixel height and display resolution are taken into account. These parameters are calculated using a visual perception based formula proposed in the paper. The experimental results show that the proposed method can detect human height with the absolute error of 7 cm from ground. 

# Contributors:<br/>
1. Janki Desai (1401103)<br/>
2. Kedar Acharya (1401081)<br/>
3. Shloak Agarwal (1401105)<br/>
4. Rahul Rachh (1401057)<br/>

# Flowchart <br/>

![output](https://github.com/janki1996/ML_HeightEstimation/blob/master/flowdiagram.jpg?raw=true)

As shown in the Figure input image or the video is converted into gray scale and then re-sized into 400 X 400 to increase computation speed. After that, HOG descriptor is used with SVM to classify and detect the human body. Image is then padded to increase the accuracy of detection of human body from head to toe. Geometric and trignometric formula is developed for tilt. It is transformed in such a way so that the tilt image is transformed to zero angle plane. Then the predicted height is calculated which is then compared with reference image to provide output that is detected height. Here height estimation wascarried out for 2-4 people using video and static images. Only 1 camera was used with tilt known. 


# Proposed Method
This method is based on concept of visual perception. Parameters we used are explained in Figures below.<br />
 ![output](https://github.com/janki1996/ML_HeightEstimation/blob/master/dig.PNG?raw=true)
 
![output](https://github.com/janki1996/ML_HeightEstimation/blob/master/Fig1.PNG?raw=true)

![output](https://github.com/janki1996/ML_HeightEstimation/blob/master/Fig2.PNG?raw=true)
![output](https://github.com/janki1996/ML_HeightEstimation/blob/master/Fig3.PNG?raw=true)

 ’P ref’ is Pixel reference and equal to total pixel present in height of screen. 
 ’H ref’ is reference height of the person in ’cm’ and pixel height equivalent to ’P ref’.  
 ’h’ is pixel height detected by HOG.
 ’P left’ is difference between ’P ref’ and bottom most coordinate of detection box. 
 ’x’ is height more than horizontal height. 
 ’Height’ is predicted height.
 
According to visual perception if referred person moves to and fro with respect to frame of camera there will be change in its pixel height. If person moves backward there will be decrease in pixel height of person and there will be increase in P left value then,

  ![output](https://github.com/janki1996/ML_HeightEstimation/blob/master/Formula1.JPG?raw=true)
 
 where (y+h-pad h) is the coordinate of detection box with respect to y-axis/scale. According to visual perception, predicted height is directly proportional to pixel height (h) and inversely proportional to (P ref - (2×P left))

 ![output](https://github.com/janki1996/ML_HeightEstimation/blob/master/Formula2.JPG?raw=true)
 The challenges will be dispayed next.
 
 # Current Challenges 

 **Surface of Ground**  <br />

 In case of ground surface not being on the same level, the ﬂoor not being ﬂat or a shining ﬂoor there will be substantial error while estimating height <br />

 **Walking habit of human**  <br />

  All humans have different walking habits, some walk with bowed head, some with forward leaning pose, such cases provide error in detection which will cause substantial error in result. <br />


 




