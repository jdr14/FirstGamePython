
import arcade
import os
import time
import threading

DEFAULT_GAME_TITLE = "The Adventures of Joey"
DEFAULT_MAIN_WINDOW_WIDTH = 1200
DEFAULT_MAIN_WINDOW_HEIGHT = (DEFAULT_MAIN_WINDOW_WIDTH * 2) / 3  # proportional to the width (by 2/3)
DEFAULT_GAME_BACKGROUND_COLOR = arcade.color.BABY_BLUE

MAIN_CHARACTER = "graphics/main_character.png"
CHARACTER_SCALING = 0.5

JUMP_HEIGHT = 100
JUMP_RESOLUTION = 10  # Divisor (The higher the number, the smoother the jump animation)

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
        # Call parent class constructor to ensure parent is initialized
        super().__init__(width, height, title)
        arcade.set_background_color(background_color)

        # Ensure we are in the directory t hat contains this file.  If the folder hierarchy is setup correctly,
        # the image/graphics folder that contains all of the images necessary to construct the sprite and other game
        # entities will be visible to the program from this scope...
        # Note: The preceding '_' character is used to denote "private" variables which are intended for visibility
        #       to the containing function/method/class
        _this_file = os.path.dirname(os.path.abspath(__file__))
        os.chdir(_this_file)

        # Create the main character
        self.main_spr = arcade.Sprite(MAIN_CHARACTER, CHARACTER_SCALING)
        self.main_spr.center_x = 200
        self.main_spr.center_y = 300

        # Create an empty sprite list and add the character(s) to the list
        self.sprites_list = arcade.SpriteList()
        self.sprites_list.append(self.main_spr)

        # Setup for other game meta data
        self.score = 0

    def on_draw(self):
        arcade.start_render()
        self.sprites_list.draw()

    def _timer(self, seconds):
        time.sleep(seconds)

    def _jump(self):
        """
        Provide a simple animation for the character jumping
        :return:
        """
        for i in range(int(JUMP_HEIGHT/JUMP_RESOLUTION)):  # Jump up
            print(i)
            self.main_spr.center_y += JUMP_RESOLUTION
            time.sleep(0.5/JUMP_RESOLUTION)
        #for i in range(int(JUMP_HEIGHT/JUMP_RESOLUTION)):  # Come back down
        #    self.main_spr.center_y -= JUMP_RESOLUTION
        #    time.sleep(1/JUMP_RESOLUTION)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.UP:  # Up
            self._jump()
        elif key == arcade.key.S or key == arcade.key.DOWN:  # Down
            self.main_spr.center_y -= 50
        elif key == arcade.key.D or key == arcade.key.RIGHT:  # Right
            self.main_spr.center_x += 200
        elif key == arcade.key.A or key == arcade.key.LEFT:  # Left
            self.main_spr.center_x -= 200

    def start(self):
        arcade.run()