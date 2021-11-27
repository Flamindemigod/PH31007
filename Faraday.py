from manim import *
from manim.mobject import value_tracker
from manim.utils.rate_functions import ease_out_cubic
from manim_physics import *
import numpy as np


#https://docs.manim.community/en/stable/reference/manim.mobject.changing.TracedPath.html


class Farday(Scene):
    def construct(self):
        #Coil
        radius = 0.5
        w = 30
        pitch = lambda t:  t
        
        springSpring = ParametricFunction(lambda t:radius*((np.sin(w*t))*DOWN + (0.1*w*pitch(t))*RIGHT + (np.cos(w*t))*OUT))
        springBounding = Rectangle(height=1, width=1.6).shift(0.7*RIGHT)        
        spring = VGroup(springBounding, springSpring)
    
        
        wire1 = Line(radius*((np.sin(0))*DOWN + (0.1*w*pitch(0))*RIGHT + (np.cos(0))*OUT), UP)
        wire2 = Line(radius*((np.sin(w*0.99))*DOWN + (0.1*w*pitch(0.99))*RIGHT + (np.cos(w*0.99))*OUT), springBounding.get_right()+UP)
        wire = VGroup(wire1, wire2)

        #Galvanometer
        GalBounding = Line(wire1.get_end(), wire2.get_end())
        GalBoundry = Circle(0.4, color=WHITE).move_to(GalBounding.get_center()).shift(0.2*UP)
        GalMeter = Line(GalBounding.get_center(), GalBoundry.get_edge_center(UP), buff=0.1).shift(0.1*DOWN)
        
        Galvanometer = VGroup(GalBoundry, GalBounding, GalMeter)
        def fieldUpdate(field):
            new_field = BarMagneticField(magnet)
            field.become(new_field)


        #Magnet
        magnet = BarMagnet().scale(0.7).rotate(90*DEGREES).shift(3*RIGHT+DOWN)
       
        field = BarMagneticField(magnet)
        field.add_updater(fieldUpdate)
        VGroup(magnet, Galvanometer, wire, spring).move_to(ORIGIN)

        self.play(Create(spring[1]), Create(wire), Create(Galvanometer))
        

        self.play(FadeIn(field, magnet))
        self.play(magnet.animate.shift(2*LEFT), GalMeter.animate.rotate(-45*DEGREES, about_point=GalMeter.get_start()), rate_func=rate_functions.ease_in_cubic, run_time=2)
        self.play(magnet.animate.shift(2*LEFT), GalMeter.animate.rotate(45*DEGREES, about_point=GalMeter.get_start()), rate_func=rate_functions.ease_out_cubic, run_time=2)

        self.wait()