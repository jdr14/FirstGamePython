
import arcade
import os

DEFAULT_GAME_TITLE = "The Adventures of Joey"
DEFAULT_MAIN_WINDOW_WIDTH = 1200
DEFAULT_MAIN_WINDOW_HEIGHT = (DEFAULT_MAIN_WINDOW_WIDTH * 2) / 3  # proportional to the width (by 2/3)
DEFAULT_GAME_BACKGROUND_COLOR = arcade.color.BABY_BLUE

MAIN_CHARACTER = "graphics/main_character.png"
CHARACTER_SCALING = 0.5

class Game(arcade.Window):
    """
    Class inherits from the Window submodule (from arcade)
    """
    def __init__(self,
                 width=DEFAULT_MAIN_WINDOW_WIDTH,
                 height=DEFAULT_MAIN_WINDOW_HEIGHT,
                 title=DEFAULT_GAME_TITLE,
                 background_color=DEFAULT_GAME_BACKGROUND_COLOR
                 ):
        """
        :param width:
        :param height:
        :param title:
        :param background_color:  Named arg is provided as an option for the user to change the main background color
        """

        # The following is to setup the main game window
        self.main_window_width = width
        self.main_window_height = height
        self.main_window_title = title

        # Call parent class constructor to ensure parent is initialized
        super().__init__(width, height, title)
        arcade.set_background_color(background_color)
        self.background_image = None

        # Ensure we are in the directory t hat contains this file.  If the folder hierarchy is setup correctly,
        # the image/graphics folder that contains all of the images necessary to construct the sprite and other game
        # entities will be visible to the program from this scope...
        # Note: The preceding '_' character is used to denote "private" variables which are intended for visibility
        #       to the containing function/method/class
        _this_file = os.path.dirname(os.path.abspath(__file__))
        os.chdir(_this_file)

        # Create the main character
        self.main_character = arcade.Sprite(MAIN_CHARACTER, CHARACTER_SCALING)
        self.main_character_center_posx = width
        self.main_character_center_posy = 500

        # Create an empty sprite list and add the character(s) to the list
        self.sprites_list = arcade.SpriteList()
        self.sprites_list.append(self.main_character)

        # Setup for other game meta data
        self.score = 0

    def onDraw(self):
        self._drawMainWindow()
        arcade.start_render()
        self.sprites_list.draw()

    def start(self):
        arcade.run()