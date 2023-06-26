import cv2
from cv2 import waitKey
import numpy 
import sys
from macros import MACRO
import random
import os

#from sklearn.datasets import make_circles

class EntryGiver: 

    table = {}

    def __init__(self, 
        imagePath = MACRO.GROUNDTRUTHIMAGES, 
        labelPath=MACRO.GROUNDTRUTHLABELS, 
        ):
        
        self.imageTable = []
        self.labelsTable = []
        
        for i in range(len(os.listdir(imagePath))):
            currentImage = cv2.imread(imagePath + f'{i+1}.bmp', cv2.IMREAD_GRAYSCALE)
            self.imageTable.append(currentImage)
            #self.labelsTable.append(numpy.zeros(currentImage.shape))
        
        
        self.test = []
        for i in range(len(self.imageTable)):
            x, y = 0, 0
            with open(labelPath + f"{i + 1}.txt") as f:
                line = f.readline().split()
                x, y = int(line[0]), int(line[1])
            img = self.imageTable[i].copy()
            cv2.circle(img, (x, y), 14, (255, 255, 255), -1)
            img_label = numpy.zeros(img.shape)
            cv2.circle(img_label, (x, y), 18, 255, -1)

            self.labelsTable.append(img_label)
            self.test.append(img)
        
        
    def getTable(self):
        return numpy.asarray(self.imageTable), numpy.asarray(self.labelsTable), numpy.asarray(self.test)

    def makeCircle(self, table, radious, locationX, locationY):
    
        for i in range(locationX-radious, locationX+radious+1):
            for j in range(locationY-radious, locationY+radious+1):
                if i >= 0 and j >= 0 and i < len(table) and j < len(table[0]):
                    if (i-locationX)**2 + (j-locationY)**2 <= radious**2:
                        try:
                            table[i][j] = 1#(1 - (((i-locationX)**2 + (j-locationY)**2)**0.5)/radious)
                        except: 
                            table[i][j] = 1






        


            

            





