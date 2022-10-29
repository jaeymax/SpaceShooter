from game.classes.window import Window
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
print(BASEDIR)

def main():
    window:Window = Window()
    window.run()





if __name__ == "__main__":
    main()