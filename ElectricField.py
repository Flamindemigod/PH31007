from manim import *
from manim_physics import *
import random
from math import log
import manim_physics

class ElectricField(Scene):
    def construct(self):
        config.frame_height = 15
        config.frame_width = 15

        charges = VGroup()
        
        def fieldUpdate(field):
            new_field = manim_physics.ElectricField(*charges)
            field.become(new_field)
        field = manim_physics.ElectricField()
        field.add_updater(fieldUpdate)

        Charge1 = Charge(1, 2*RIGHT)
        Charge2 = Charge(1.3, 2*UL)
        Charge3 = Charge(-0.8, 1.5*(DOWN+LEFT))

        charges.add(Charge1, Charge2, Charge3)

        self.play(FadeIn(charges))
        self.play(FadeIn(field))

        for _ in range(7):
            step=1.5
            self.play(
                Charge1.animate.shift(step*random.random()*DOWN, step*random.random()*RIGHT, step*random.random()*LEFT, step*random.random()*UP),
                Charge2.animate.shift(step*random.random()*DOWN, step*random.random()*RIGHT, step*random.random()*LEFT, step*random.random()*UP),
                Charge3.animate.shift(step*random.random()*DOWN, step*random.random()*RIGHT, step*random.random()*LEFT, step*random.random()*UP), run_time=1)
