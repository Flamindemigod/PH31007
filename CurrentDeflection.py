from manim import *

""" 
‘Andre-Marie Ampere, a man in the early 1800s, hears a story about a compass needle being deflected for an unknown reason;
the only thing nearby being an electric current through a wire.’ 
 """
class CurrentDeflection(Scene):
    def construct(self):
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