from manim import *
from manim_physics import *

class MagneticFieldAroundWire(ThreeDScene):
    def construct(self):
        current1 = Current(magnitude=10)
        _field = CurrentMagneticField(current1)
        field = VGroup(_field)
        self.add(current1, field)
        self.begin_ambient_camera_rotation(rate=-0.3)
        self.wait(5.2)
        self.stop_ambient_camera_rotation()

#        self.play(field.animate.rotate(90*DEGREES, about_point=ORIGIN), run_time=1, rate_func=rate_functions.linear)
