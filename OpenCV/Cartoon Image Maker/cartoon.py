import cv2 as cv
import os 

class Cartoon : 
    def __init__(self, path) -> None:
        self.path = path
        image = cv.imread(path)
        gray = cv.medianBlur(cv.cvtColor(image, cv.COLOR_BGR2GRAY), 5)
        edges = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 9)
        color = cv.bilateralFilter(image, 9, 250, 250)
        self.cartoon = cv.bitwise_and(color, color, mask=edges)
    
    def save(self) : 
        new_img_path = "anime_" + self.path
        if new_img_path not in os.listdir() :
            cv.imwrite(new_img_path , self.cartoon)
        else : 
            choice = int(input("this file exist, do you want to ecrase him ? 1 : yes , 0 : no"))
            if choice == 1 :
                cv.imwrite(new_img_path , self.cartoon)
            else : 
                print("ok.")
                quit()
