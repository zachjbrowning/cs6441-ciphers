import pickle




def load_data():
    pickle_in = open("datafile.p", "rb")
    data = pickle.load(pickle_in)
    pickle_in.close()
    return data   

def save_data(data):
    pickle_out = open("datafile.p", "wb")
    pickle.dump(data, pickle_out)
    pickle_out.close()

def reset_data():
    return {
        'users' : {},

    }

