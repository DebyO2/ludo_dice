

import random
import os


try:
    import pyfiglet
    
except ImportError:
     os.system("pip3 install pyfiglet")
     

os.system("cls")

if __name__ == "__main__":
    
    print(pyfiglet.figlet_format('The DiCe'))
    print("author: Mortal_coder\n")

    print("Hello i m the best alternate to a physical dice,")
    print("let me choose a number on a dice")
    while True:
        listw = list("123456")
        e = random.choice(listw)
        print("outcome /",e ) 
        a = input("if u want to roll the dice again(if u don't want to then just type 'no') just press enter/")
        if 'no' in a:
            exit()
        else:
            pass
