import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.LANGUID_LAVENDER)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.PEACH_PUFF)
    arcade.start_render()

    draw_grass()

    # Draw a snow person

    # Snow
    arcade.draw_circle_filled(450, 350, 70, arcade.color.WHITE)
    arcade.draw_circle_filled(450, 350, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(450, 350, 50, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(385, 450, 6, arcade.color.BLACK)
    arcade.draw_circle_filled(415, 3450, 6, arcade.color.BLACK)

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()