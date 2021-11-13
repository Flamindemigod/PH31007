from manim import *
from manim_physics import *

class MagneticFieldAroundWire(ThreeDScene):
    def construct(self):
        current1 = Current(magnitude=10)
        field = CurrentMagneticField(current1)
        self.add(current1, field)
        self.begin_ambient_camera_rotation(rate=-0.3)
        self.wait(5.2)
        self.stop_ambient_camera_rotation()

