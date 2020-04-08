import pickle


def load_pickle(file_path):
    with open(file_path, 'rb') as handle:
        data = pickle.load(handle)
        return data

# def update_list(features_list,names_list):
#     global KNOWN_FACE_ENCODINGS
#     KNOWN_FACE_ENCODINGS = features_list
#     print(len(KNOWN_FACE_ENCODINGS))
#     global KNOWN_NAMES
#     KNOWN_NAMES = names_list
#     print(len(KNOWN_NAMES))


def get_list():
    DATA = load_pickle(path_to_pickle)
    KNOWN_FACE_ENCODINGS = list(DATA.values())
    KNOWN_NAMES = list(DATA.keys())
    # global KNOWN_NAMES, KNOWN_FACE_ENCODINGS
    return KNOWN_FACE_ENCODINGS,KNOWN_NAMES

path_to_pickle = "./database/features/features.pickle"
# DATA = load_pickle(path_to_pickle)
# global KNOWN_FACE_ENCODINGS
# KNOWN_FACE_ENCODINGS = list(DATA.values())
# global KNOWN_NAMES
# KNOWN_NAMES = list(DATA.keys())