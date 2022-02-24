"""
Space Snakes: The Game
"""
import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "SPACE SNAKES: THE GAME"
SCALING_SNAKE_SPRITE = 0.5
SNAKE_MOVEMENT_SPEED = 5
ASTERIOD_SCALING = 0.2

class MyGame(arcade.Window):
    """
    Main Application Class
    """

    def __init__(self):
        # Call the parent class and setup the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # self.scene = None

        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.snake_list = None
        self.snake_sprite = None

        # Our physics engine
        # self.physics_engine = None

        # sets the background of the game window
        arcade.set_background_color(arcade.csscolor.BLACK)
        pass

    def setup(self):
        """set up the gaem here. Call this function to restart the game."""
        # self.scene = arcade.Scene()

        self.snake_list = arcade.SpriteList()

        self.snake_sprite = arcade.Sprite(":resources:images/space_shooter/playerShip2_orange.png", SCALING_SNAKE_SPRITE)
        self.snake_sprite.center_x = 500
        self.snake_sprite.center_y = 325
        self.snake_list.append(self.snake_sprite)

        # Create the ground
        # This shows using a loop to place multiple sprites horizontally
        """for x in range(0, 1250, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", ASTERIOD_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.scene.add_sprite("Walls", wall)"""

        # Create the 'physics engine'
        """self.physics_engine = arcade.PhysicsEngineSimple(
            self.snake_sprite, self.scene.get_sprite_list("Walls"),
        )"""
        pass

    def on_draw(self):
        """Render the screen"""
        arcade.start_render()

        # Code to draw the screen goes here
        self.snake_list.draw()
        pass

    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        #self.physics_engine.update()


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.snake_sprite.change_y = SNAKE_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.snake_sprite.change_y = -SNAKE_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.snake_sprite.change_x = -SNAKE_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.snake_sprite.change_x = SNAKE_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.snake_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.snake_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.snake_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.snake_sprite.change_x = 0


def main():
    """Main Function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
