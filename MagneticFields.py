from manim import *
from manim_physics import *

class MagnetismExample(MovingCameraScene):
    def construct(self):
        current1 = Current()
        field = CurrentMagneticField(current1)
        self.add(current1, field)
        self.play(field.animate.rotate(1), run_time=5, rate_func=rate_functions.sigmoid)
