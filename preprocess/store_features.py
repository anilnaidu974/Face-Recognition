
import os
import face_recognition.api as face_recognition
import sys
import pickle

def extract_features(image_path):
    img = face_recognition.load_image_file(image_path)
    encodings = face_recognition.face_encodings(img)
    file_name = os.path.basename(image_path).split(".")[0]
    file_name = file_name.split('_')[0]
    return file_name, encodings

def store_features(path,data):
    with open(path, 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

def main():
    print("Extracting Image Features........")
    path_to_images = "../database/images/"
    path_to_pickle = "../database/features/features.pickle"
    data = {}
    for filename in os.listdir(path_to_images):
        image_path = os.path.join(path_to_images,filename)
        file_name, encodings = extract_features(image_path)
        if encodings:
            data[file_name] = encodings
        
    print("Storing Image Features")
    store_features(path_to_pickle,data)
    print("********* Completed ************")

if __name__ == "__main__":
    main()
