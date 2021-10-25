"""
Space Snakes: The Game
"""
import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "SPACE SNAKES: THE GAME"


class MyGame(arcade.Window):
    """
    Main Application Class
    """

    def __init__(self):
        # Call the parent class and setup the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.BLACK)
        pass

    def setup(self):
        """set up the gaem here. Call this function to restart the game."""
        pass

    def on_draw(self):
        """Render the screen"""
        arcade.start_render()

        # Code to draw the screen goes here

        pass


def main():
    """Main Function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
