from manim import *
import numpy as np
import textwrap



""" 
‘Andre-Marie Ampere, a man in the early 1800s, hears a story about a compass needle being deflected for an unknown reason;
the only thing nearby being an electric current through a wire.’ 
 """
class CurrentDeflection(ThreeDScene):
    def construct(self):
        intro_text = "The Magnetic Source"
        num_of_current_elements = 15
        distance_between_current_elements = 0.5
        


        img = ImageMobject("media/Assets/ampere.png")
        self.play(FadeIn(img, shift=IN))
        self.wait(2)
        self.play(img.animate.to_corner(UP+LEFT).shift(DOWN+RIGHT), rate_func=rate_functions.ease_in_out_cubic, run_time=2)

        #Wire
        wire = Line(4*UP, 4*DOWN).set_color(BLUE_C)
        current_elements_verticies = np.arange(0, num_of_current_elements*distance_between_current_elements, distance_between_current_elements)
        current_elements_verticies = np.expand_dims(current_elements_verticies, axis=0)
        z = np.zeros(current_elements_verticies.shape, dtype=current_elements_verticies.dtype)
        current_elements_verticies = np.concatenate((current_elements_verticies,z), axis=0)
        current_elements_verticies = np.transpose(current_elements_verticies)
        current_elements_verticies = np.pad(current_elements_verticies, ((0,0),(1,0)))
        
        wire_current = VGroup()
        for vertex in  current_elements_verticies:
            wire_current.add(Dot(vertex, color=BLUE_C))
        wire_current.to_edge(DOWN).shift((wire_current.get_top()-wire_current.get_bottom() + 1)*DOWN) 
        wire_current_label = Tex("I").move_to(wire).shift(1*LEFT)
        wire_current_arrow = Arrow(start= ORIGIN, end=UP).move_to(wire_current_label).shift(0.5*RIGHT)

        wire_current_group = VGroup(wire_current, wire_current_label, wire_current_arrow)
        wire_group = VGroup(wire, wire_current_group).shift(6*RIGHT)
        

        #Magnet
        MagnetNorth = Polygon(0.3*LEFT, 0.3*RIGHT, UP, fill_opacity=1).set_color(RED_A)
        MagnetNorthLabel = Tex("N").shift(0.3*UP).set_color(RED_D)
        MagnetSouth = Polygon(0.3*LEFT, 0.3*RIGHT, DOWN, fill_opacity=1).set_color(BLUE_A)
        MagnetSouthLabel = Tex("S").shift(0.3*DOWN).set_color(BLUE_D)
        Magnet = VGroup(MagnetNorth, MagnetSouth, MagnetNorthLabel, MagnetSouthLabel)
        
        self.play(Write(VGroup(Magnet, wire_group)), run_time=2, rate_func=rate_functions.ease_in_cubic)

        self.play(
            Magnet.animate.rotate(-0.5),
            wire_current.animate.move_to(wire), run_time=4, rate_func=rate_functions.linear)
        self.play(
            Magnet.animate.rotate(0.5),
            wire_current.animate.to_edge(UP).shift((wire_current.get_top()-wire_current.get_bottom() + 1)*UP), run_time=4, rate_func=rate_functions.linear)

        self.play(Unwrite(VGroup(Magnet, wire_current_label, wire_current_arrow)), FadeOut(img, shift=OUT))
        wire_current_group.remove(wire_current_label, wire_current_arrow)
        self.play(
            wire.animate.move_to(ORIGIN),
            wire_current_group.animate.move_to(ORIGIN))
        Intro_text = Tex(*textwrap.wrap(intro_text, int(len(intro_text)/len(current_elements_verticies)), replace_whitespace=False, drop_whitespace=False))
        Intro_text.scale(2)
        self.play(
            Transform(wire_current, Intro_text),
            FadeOut(wire),
            run_time=2,
            rate_func=rate_functions.ease_out_sine
        )
        self.add(Intro_text),
        self.remove(wire_current, wire)
        self.wait()
        self.play(Unwrite(Intro_text))
        self.wait()