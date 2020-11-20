# Face Recognition using OpenCV and Keras
 Face recognition project using opencv and keras which detects my own face and classifies other faces as unknowns.
 In this project, I used OpenCV and Keras in Python to simulate the facial recognition applications for a CCTV camera which allows only the owner of the house to enter and when someone else tries to enter, the program classifies it as Unknown and sends a notification to the owner.
 This repo of course is not the whole implementation but just the program part of it.
 This uses the Label encodings of a face given in the datasets and on their basis trains the model using label encoder from sci-kit learn in keras.
 Then this program identifies the faces using normal haarcascades in OpenCV and then finds the faces in the image or the video.
The names it recognises are basically the names of the folders in which the images of the persons are stored.
There is a data_collector.py program which can be used to capture images in real-time to store them and use them as the training dataset images. 
For the test dataset, I used some old images of mine with people around me in the image. The program still shows above 80% accuracy in detecting me from the Unknowns.
I have also used argparse in Python to run each .py file in Powershell with the names of the model, embeddings and the test images as arguments in the command line interface. It makes it easier to change than in the IDLE.
You can also try to run this in your own Computer so that it may recognise your face.
Make your dataset by running the data_collector.py program and staring into your camera for about 3-4 seconds (Smile please :) .
Then transfer those files from Images folder to the Datasets folder with your name as folder name.
Run extract_embeddings.py so that it may extract the embeddings of your image.
Train the model using train_model.py.
You are done!
Just run recognize_video.py to see the code recognize your face with awesome accuracy.
The results are shown in the RESULTS folder.
Peace.
