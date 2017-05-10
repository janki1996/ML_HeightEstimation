
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
# ![Alt text](/flowdiagram.jpg?raw=true "Flowchart")
As shown in the Figure input image or the video is converted into gray scale and then re-sized into 400 X 400 to increase computation speed. After that, HOG descriptor is used with SVM to classify and detect the human body. Image is then padded to increase the accuracy of detection of human body from head to toe. Geometric and trignometric formula is developed for tilt. It is transformed in such a way so that the tilt image is transformed to zero angle plane. Then the predicted height is calculated which is then compared with reference image to provide output that is detected height. Here height estimation wascarried out for 2-4 people using video and static images. Only 1 camera was used with tilt known. 




