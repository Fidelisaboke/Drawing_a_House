import cairo
import math

WIDTH, HEIGHT = 1600, 1000
BG_COLOR = (0.8, 0.8, 0.8)

# Set up surface
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)
ctx.set_source_rgb(*BG_COLOR)
ctx.paint()

# Top surface of roof
ctx.set_line_width(5)
ctx.set_source_rgb(0, 0, 0)
ctx.move_to(410, 100)
ctx.line_to(1200, 50)
ctx.line_to(1370, 340)
ctx.line_to(580, 400)
ctx.close_path()
ctx.stroke()

# Roof outline
ctx.set_line_width(8)
ctx.move_to(220, 280) # x6, y6
ctx.line_to(400, 100) # x1, y1
ctx.line_to(1200, 50)
ctx.line_to(1370, 340)
ctx.line_to(1360, 360) #
ctx.line_to(560, 420) #
ctx.line_to(400, 130) # x1, y1 + 30
ctx.line_to(230, 300) # x5, y5
ctx.close_path()
ctx.stroke()

# Tiny triangle on the left side of the roof
ctx.move_to(230, 300)
ctx.line_to(250, 300)
ctx.line_to(250, 280)
ctx.set_line_join(cairo.LINE_JOIN_ROUND)
ctx.close_path()
ctx.stroke()

# Wall outline from top left to door
ctx.set_line_width(8)
ctx.set_line_join(cairo.LINE_JOIN_MITER)
ctx.move_to(250, 300)
ctx.line_to(250, 700)
ctx.line_to(550, 820)
ctx.line_to(1130, 730)
ctx.line_to(1130, 470)
ctx.line_to(1280, 455)
ctx.line_to(1280, 710)

# Door knob
ctx.new_sub_path()
ctx.arc(1240, 575, 10, 0, math.radians(360))
ctx.close_path()
ctx.stroke()

# Door frame bottom
ctx.new_sub_path()
ctx.move_to(1130, 710)
ctx.line_to(1260, 690)
ctx.line_to(1280, 710)
ctx.stroke()
ctx.close_path()

# Wall outline from door frame to top right
ctx.line_to(1280, 710)
ctx.line_to(1330, 700)
ctx.line_to(1330, 360)
ctx.stroke()

# Thinner outline of wall
ctx.set_line_width(5)
ctx.move_to(550, 820)
ctx.line_to(550, 400)
ctx.close_path()
ctx.stroke()

# Thinner outline next to door frame
ctx.move_to(1260, 455)
ctx.line_to(1260, 690)
ctx.stroke()

# Left window
ctx.set_line_width(8)
ctx.move_to(320, 420)
ctx.line_to(320, 580)
ctx.line_to(450, 640)
ctx.line_to(450, 480)
ctx.close_path()
ctx.move_to(385, 450)
ctx.line_to(385, 615)
ctx.move_to(320, 500)
ctx.line_to(450, 560)
ctx.close_path()
ctx.stroke()

# Front window left
ctx.move_to(640, 660)
ctx.line_to(640, 480)
ctx.line_to(760, 470)
ctx.line_to(760, 645)
ctx.close_path()
ctx.move_to(700, 470)
ctx.line_to(700, 650)
ctx.move_to(640, 570)
ctx.line_to(765, 555)
ctx.close_path()
ctx.stroke()

# Front window right
ctx.move_to(890, 640)
ctx.line_to(890, 460)
ctx.line_to(1010, 450)
ctx.line_to(1010, 625)
ctx.close_path()
ctx.move_to(950, 450)
ctx.line_to(950, 630)
ctx.move_to(890, 550)
ctx.line_to(1015, 535)
ctx.close_path()
ctx.stroke()


# Write to png
surface.write_to_png('house.png')
print('3D House Created!')
