import arcade


WIDTH = 640
HEIGHT = 480

x_circle = 325
y_circle = 300
radius = 100

arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()
# Begin drawing

arcade.draw_circle_filled(x_circle, y_circle, radius, arcade.color.BLUE_GREEN)

# End drawing
arcade.finish_render()
arcade.run()
