"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the and dimensions (width and height)
arcade.open_window(800, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw the grass
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.NEON_FUCHSIA)

# --- Draw the barn ---
e.draw_rectangle_filled(70, 260, 20, 30, arcade.color.PEAR)

# Right-bottom window
arcade.draw_rectangle_filled(310, 260, 30, 40, arcade.color.BONE)
arcade.draw_rectangle_filled(310, 260, 20, 30, arcade.color.PEAR)

# Barn door
arcade.draw_rectangle_filled(190, 230, 100, 100, arcade.color.BRONZE)

# Rail above the door
arcade.draw_rectangle_filled(190, 280, 180, 5, arcade.color.PEACH_PUFF)

# Draw second level of barn
arcade.draw_polygon_filled([[20, 350],
                            [100, 470],
                            [280, 470],
                            [360, 340]],
                            arcade.color.PUCE)

# Draw loft of barn
arcade.draw_triangle_filled(100, 470, 280, 470, 190, 500, arcade.color.BROWN)

# Left-top window
arcade.draw_rectangle_filled(130, 440, 30, 40, arcade.color.BONE)
arcade.draw_rectangle_filled(130, 440, 20, 30, arcade.color.PEAR)

# Right-top window
arcade.draw_rectangle_filled(250, 440, 30, 40, arcade.color.BONE)
arcade.draw_rectangle_filled(250, 440, 20, 30, arcade.color.PEAR)

# Draw 2nd level door
arcade.draw_rectangle_outline(190, 310, 30, 60, arcade.color.BONE, 5)

# Barn cement base
arcade.draw_lrtb_rectangle_filled(30, 350, 210, 170, arcade.color.BABY_POWDER)

# Bottom half
arcade.draw_lrtb_rectangle_filled(30, 350, 350, 210, arcade.color.BROWN)

# Left-bottom window
arcade.draw_rectangle_filled(70, 260, 30, 40, arcade.color.BONE)

# import module
import arcade
# set parameters 
Width= 700
Height=700
Title="SUN"
# open window
arcade.open_window(Width, Height, Title)
# Set the background color
arcade.set_background_color(arcade.csscolor.BLUE)
# Get ready to draw
arcade.start_render()
# Draw a sun
arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)
# Rays to the left, right, up, and down
arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)
# Diagonal ray
arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)
# Finish drawing
arcade.finish_render()
# Keep the window up until someone closes it.
arcade.run()
