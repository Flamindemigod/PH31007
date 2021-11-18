from manim import *
from manim_physics import *
import random
from math import log
import manim_physics

class ElectricField(Scene):
    def construct(self):
        config.frame_height = 15
        config.frame_width = 15
        Charge1 = Charge(1, 2*RIGHT)
        Charge2 = Charge(1.3, 2*UL)
        Charge3 = Charge(-0.8, 1.5*(DOWN+LEFT))

        field = manim_physics.ElectricField(Charge1, Charge2, Charge3)
        self.play(FadeIn(Charge1, Charge2, Charge3))
        self.play(FadeIn(field))
        _Charge1 = Charge1.copy()
        _Charge2 = Charge2.copy()
        _Charge3 = Charge3.copy()
        for _ in range(7):
            step=1.5
            _Charge1 = _Charge1.shift(step*random.random()*DOWN, step*random.random()*RIGHT, step*random.random()*LEFT, step*random.random()*UP)
            _Charge2 = _Charge2.shift(step*random.random()*DOWN, step*random.random()*RIGHT, step*random.random()*LEFT, step*random.random()*UP)
            _Charge3 = _Charge3.shift(step*random.random()*DOWN, step*random.random()*RIGHT, step*random.random()*LEFT, step*random.random()*UP)
            _field = manim_physics.ElectricField(_Charge1, _Charge2, _Charge3)
            
            self.play(
                Transform(Charge1, _Charge1),
                Transform(Charge2, _Charge2),
                Transform(Charge3, _Charge3),
                Transform(field, _field), run_time=1)
