from manim import *
import random
""" 
‘But an issue became clear, he couldn’t account for the apparently induced current across unconnected capacitor plates – something was missing.’
 """
#TODO
## Fade the vectors a bit faster
class CapacitorPlates(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=15 * DEGREES, theta=-45 * DEGREES, gamma=45 * DEGREES)
        CapPlate1 = Rectangle(height=2, width=2, color=BLUE_B,grid_xstep=0.1, grid_ystep=0.1).rotate(90*DEGREES, axis=Y_AXIS)
        CapPlate2 = Rectangle(height=2, width=2, color=BLUE_C,grid_xstep=0.1, grid_ystep=0.1).rotate(90*DEGREES, axis=Y_AXIS).shift(RIGHT)
        
        CapPlates = VGroup(CapPlate1, CapPlate2)

        wire1 = Line(3*LEFT, [0,0,0]).set_color(BLUE_B)
        wire2 = Line(RIGHT, 4*RIGHT).set_color(BLUE_C)
        wire_current = Cone(direction=X_AXIS, show_base=False, base_radius=0.06, height=0.09).shift(3*LEFT)
        wire_current_label = Tex("I").move_to(wire_current).shift(0.5*DOWN).scale(0.4)
        wire_current_group = VGroup(wire_current, wire_current_label)

        self.play(FadeIn(CapPlates, wire1, wire2))
        self.play(FadeIn(wire_current_group),
                wire_current_group.animate.shift(1.5*RIGHT), run_time=1.5, rate_func=rate_functions.linear)
        self.play(FadeOut(wire_current_group, shift = (1.5*RIGHT)), run_time=1.5, rate_func=rate_functions.linear)

        vec=VGroup()
        for i in range(10):
            vec.add(Vector(CapPlate2.get_center()-CapPlate1.get_center(), buff=0.3).shift(i*UP/10).shift(random.random()*0.5*LEFT))
            vec.add(Vector(CapPlate2.get_center()-CapPlate1.get_center(), buff=0.3).shift(i*DOWN/10).shift(random.random()*0.5*LEFT))

        self.play(FadeIn(vec),
                vec.animate.shift(0.5*RIGHT), rate_func=rate_functions.linear)
        self.play(FadeOut(vec, shift=0.5*RIGHT), rate_func=rate_functions.linear)
        return
        
        #Wire
        wire = Line(4*UP, 4*DOWN).set_color(BLUE_C)
        wire_current = Cone(direction=Y_AXIS, show_base=False, base_radius=0.06, height=0.09).shift(4*DOWN)
        wire_current_label = Tex("I").move_to(wire_current).shift(0.5*LEFT)
        wire_current_group = VGroup(wire_current, wire_current_label)
        wire_group = VGroup(wire, wire_current_group).shift(6*RIGHT)
        self.add(wire_group)

        #Magnet
        MagnetNorth = Polygon(0.3*LEFT, 0.3*RIGHT, UP, fill_opacity=1).set_color(RED_A)
        MagnetNorthLabel = Tex("N").shift(0.3*UP).set_color(RED_D)
        MagnetSouth = Polygon(0.3*LEFT, 0.3*RIGHT, DOWN, fill_opacity=1).set_color(BLUE_A)
        MagnetSouthLabel = Tex("S").shift(0.3*DOWN).set_color(BLUE_D)
        Magnet = VGroup(MagnetNorth, MagnetSouth, MagnetNorthLabel, MagnetSouthLabel)
        self.add(Magnet)

        
        self.play(
            Magnet.animate.rotate(-0.5),
            wire_current_group.animate.shift(4*UP), run_time=2.5, rate_func=rate_functions.linear)
        self.play(
            Magnet.animate.rotate(0.5),
            wire_current_group.animate.shift(4*UP), run_time=2.5, rate_func=rate_functions.linear)