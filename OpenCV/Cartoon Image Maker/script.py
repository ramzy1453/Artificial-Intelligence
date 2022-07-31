import os
from cartoon import Cartoon


def main():
    img_path = input("enter image path :")
    while img_path not in os.listdir() :
        choice = int(input("this file don't exist, 1 : repeat , 0 : exit"))
        if choice == 1 :
            img_path = input("enter image path :")
        else : 
            print("ok.")
            quit()
    cartoon = Cartoon(img_path)
    cartoon.save()
    print("succesful.")

if __name__ == "__main__" :
    main()