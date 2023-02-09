import pickle


def writefile(data, path):
    with open(path, "wb") as file:
        pickle.dump(data, file)


def readfile(path):
    with open(path, "rb") as file:
        return pickle.load(file)
