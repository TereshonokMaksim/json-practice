import os
def path_finder(file = ""):
    if len(__file__.split("\\")) == 1:
        file = file.split("\\")
        file = "/".join(file)
        
    abs_path = os.path.abspath(__file__ + "/.." + "/..")
    return os.path.join(abs_path, file)
