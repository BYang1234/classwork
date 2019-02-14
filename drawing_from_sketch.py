import arcade


WIDTH = 640
HEIGHT = 480

arcade.open_window(WIDTH, HEIGHT, "My Drawing")
#Background
arcade.set_background_color(arcade.color.SKY_BLUE)

arcade.start_render()
# Begin drawing

#Sun
arcade.draw_circle_filled(540, 380, 50, arcade.color.YELLOW)
#BG
arcade.draw_rectangle_filled(320, 50, 640, 100, arcade.color.GREEN)
#First Tree
arcade.draw_xywh_rectangle_filled(200, 50, 20, 75, arcade.color.BROWN)
arcade.draw_triangle_filled(140, 150, 240, 150, 200, 200, arcade.color.DARK_GREEN)  
#Second Tree
arcade.draw_xywh_rectangle_filled(WIDTH - 200 - 40, 50, 20, 75, arcade.color.BROWN)
#Third Tree
arcade.draw_xywh_rectangle_filled(515, 50, 20, 75, arcade.color.BROWN)



# End drawing
arcade.finish_render()
arcade.run()
