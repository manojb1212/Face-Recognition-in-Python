# Face-Recognition-in-Python

The Face recognition is based on the API being developed by Python community developers called - Face recognition. This can be installed using the below command.

pip install face_recognition

There are some dependencies for the above package to work properly. They are

1. dlib - This is library built in C++ to perform machine learning and Deep Learning. This can installed using command - pip install dlib
2. Microsoft Visual studio tools for C++
3. CMAKE - This is a software/library used for the build or compilation purpose. This can be downloaded and installed from its official website.
 
 
 Please note that the above are mandatory for the functioning of Face recognition API.
 
 
 This API is built by leveraging  the CNNs (Convolutional Neural Networks) that commes under the area of Deep Learning. It first identifies the faces in the image, draws the face boundaries and identifies the faces based on the learnings during training.
 
It works on the distance based approach after encoding the faces that appear on the camera. It compares the distances of the camera image and the known distances of the images stored on the Server and identifies the person. 

If the difference in the distances is small, then it maps the current camera image with the respective store image.


Future Enhancements:
--------------------
This system will be useful in identyfing the unauthorised people entering any premises and thereby reducing theft, property loss, crime activities etc.

I am working on integrating this with the communication module to enable alarms/messages for the security team so that neccessary actions can be taken.

