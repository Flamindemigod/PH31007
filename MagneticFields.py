from manim import *
from manim_physics import *

class MagneticFieldAroundWire(ThreeDScene):
    def construct(self):
        config.frame_height = 15
        config.frame_width = 15
        current1 = Current(magnitude=10)
        field = CurrentMagneticField(current1)
        self.add(current1, field)
        self.begin_ambient_camera_rotation(rate=-0.3)
        self.wait(5.2)
        self.stop_ambient_camera_rotation()

class ArtisticMagneticFieldAroundWire(ThreeDScene):
    def construct(self):
        config.frame_height = 30
        config.frame_width = 30
        self.set_camera_orientation(phi=40 * DEGREES, theta=-30 * DEGREES, gamma=40 * DEGREES)
        current = Current(magnitude=10)
        currentLine = Line(10*UP, 15*DOWN).rotate_about_origin(90*DEGREES, axis=X_AXIS)
        field = CurrentMagneticField(current)
        self.begin_ambient_camera_rotation(rate=-0.3)
        self.play(
            Write(currentLine, reverse=True, rate_func=rate_functions.smooth),
            FadeIn(field), run_time = 2)
        self.wait(8.4)
        self.stop_ambient_camera_rotation()