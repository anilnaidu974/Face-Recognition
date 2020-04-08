# Face Recognition Live Feed

before running requirements.txt make sure you have CMake installed 
if not already installed, use the below command:

sudo apt-get install cmake (in Ubuntu)

Go to https://cmake.org/download/ link and download suitable file for windows users


# Process : 

There are two steps involved in this application

step 1 : Read all images from database/images folder, Extract all encodings and saved into a pickle file

step 2 : In the real time, it will read each frame and compare all the faces in the frame with pickle file encodings

    Step 1 : 
         1. To Recognise your face upload your image with filename as yourname into database/Images
         2. Run python file which is in preprocess folder
            ex : python store_features.py
            
    Step 2 : 
         1. Run run.py python file to test the application
            ex : python run.py



