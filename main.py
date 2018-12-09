
from game import Game

def main():
    # Initialize game instance with all of the built in default options
    gameInstance = Game()
    gameInstance.onDraw()
    gameInstance.start()


if __name__ == '__main__':
    main()

