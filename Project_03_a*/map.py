import numpy as np

class Map:
    def __init__(self, image, name, arr):
        self.name = name
        self.image = image
        
        self.array = arr
        
    def get_image(self):
        return self.image
    def get_arr(self):
        return self.array
    def get_name(self):
        return self.name