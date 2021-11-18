from manim import *
from manim_physics import *
import random

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

class CapacitorMagneticField(ThreeDScene):
    def construct(self):
        config.frame_height = 30
        config.frame_width = 30
        self.set_camera_orientation(phi=40 * DEGREES, theta=-30 * DEGREES, gamma=40 * DEGREES)
        #self.set_camera_orientation(phi=90 * DEGREES)
        
        CapPlate1 = Rectangle(height=4, width=4, color=BLUE_B,grid_xstep=0.1, grid_ystep=0.1).rotate(90*DEGREES, axis=Y_AXIS)
        CapPlate2 = Rectangle(height=4, width=4, color=BLUE_C,grid_xstep=0.1, grid_ystep=0.1).rotate(90*DEGREES, axis=Y_AXIS).shift(RIGHT)
        
        CapPlates = VGroup(CapPlate1, CapPlate2)

        wire1 = Line(10*LEFT, [0,0,0]).set_color(BLUE_B)
        wire2 = Line(RIGHT, 15*RIGHT).set_color(BLUE_C)
        capacitor = VGroup(CapPlates,wire2,wire1).rotate_about_origin(-90*DEGREES, axis=Y_AXIS)
        current = Current(magnitude=10)
        field = CurrentMagneticField(current)
        self.begin_ambient_camera_rotation(rate=-0.2)
        self.play(
            Write(capacitor, reverse=True, rate_func=rate_functions.smooth),
            FadeIn(field), run_time = 2)
        for _ in range(5):
            vec=VGroup()
            _vec_range = 50
            for i in range(_vec_range):
                vec.add(Vector(CapPlate1.get_center()-CapPlate2.get_center(), buff=0.3).shift(i*UP/(_vec_range/2)).shift(random.random()*1.8*LEFT))
                vec.add(Vector(CapPlate1.get_center()-CapPlate2.get_center(), buff=0.3).shift(i*UP/(_vec_range/2)).shift(random.random()*1.8*RIGHT))
                
                vec.add(Vector(CapPlate1.get_center()-CapPlate2.get_center(), buff=0.3).shift(i*DOWN/(_vec_range/2)).shift(random.random()*1.8*LEFT))
                vec.add(Vector(CapPlate1.get_center()-CapPlate2.get_center(), buff=0.3).shift(i*DOWN/(_vec_range/2)).shift(random.random()*1.8*RIGHT))

            vec.shift(OUT*1.2)
            self.play(FadeIn(vec),
                    vec.animate.shift(0.4*IN), rate_func=rate_functions.linear, run_time=0.6*3)
            self.play(FadeOut(vec, shift=0.2*IN), rate_func=rate_functions.linear, run_time=0.3*3)
            self.wait(0.5)
        self.stop_ambient_camera_rotation()

class DisplayCurl(Scene):
    def construct(self):
        MagneticField = Circle(radius=1, color=RED_B)
        MagneticFieldLabel = MathTex(r"\vec{B}.\vec{dl}")
        MagField = VGroup(MagneticField, MagneticFieldLabel).arrange(DOWN)

        
        CurlMagneticField = Circle(radius=1, color=BLUE_B, fill_opacity=0.3)
        CurlMagneticFieldLabel = MathTex(r"\nabla\times\textbf{B}")
        CurlMagField = VGroup(CurlMagneticField, CurlMagneticFieldLabel).arrange(DOWN)

        VGroup(MagField, CurlMagField).arrange(RIGHT, buff=2)
        self.play(Write(MagField), Write(CurlMagField), run_time = 3, rate_func=rate_functions.smooth)

        