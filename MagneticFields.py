from manim import *
from manim_physics import *
import random
import manim_physics

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
        MagneticField_arrow = Cone(direction=X_AXIS, show_base=False, base_radius=0.05, height=0.1).shift(DOWN)
        MagneticField_group = VGroup(MagneticField, MagneticField_arrow)       
        MagField = VGroup(MagneticField_group, MagneticFieldLabel).arrange(DOWN)

        
        CurlMagneticField = Circle(radius=1, color=BLUE_B, fill_opacity=0.3)
        CurlMagneticFieldLabel = MathTex(r"\nabla\times\textbf{B}")
        CurlMagneticField_arrow = Cone(direction=X_AXIS, show_base=False, base_radius=0.05, height=0.1).shift(DOWN)
        CurlMagneticField_group = VGroup(CurlMagneticField, CurlMagneticField_arrow)       
        CurlMagField = VGroup(CurlMagneticField_group, CurlMagneticFieldLabel).arrange(DOWN)

        VGroup(MagField, CurlMagField).arrange(RIGHT, buff=2)
        self.play(
            Write(VGroup(MagneticField, CurlMagneticField)), 
            Write(VGroup(MagneticFieldLabel, CurlMagneticFieldLabel)),
            run_time = 3, rate_func=rate_functions.smooth)
        self.play(FadeIn(MagneticField_arrow),
                FadeIn(CurlMagneticField_arrow))
        self.play(
            Rotate(MagneticField_group, angle=2*PI, about_point=MagneticField.get_center()),
            Rotate(CurlMagneticField_group, angle=2*PI, about_point=CurlMagneticField.get_center()),
            run_time=3, rate_func=rate_functions.linear)
        self.wait()
        
class MagneticField(ThreeDScene):
    def construct(self):
        config.frame_height = 15
        config.frame_width = 15
        
        bar1 = BarMagnet().rotate(PI / 2).shift(LEFT * 3.5).scale(0.8)
        bar2 = BarMagnet().rotate(-PI / 2).shift(RIGHT * 3.5).scale(0.8)
        
        field = manim_physics.BarMagneticField(bar1, bar2)
        self.play(FadeIn(field),
                FadeIn(bar1, bar2))
        
        _bar1 = bar1.copy()
        _bar2 = bar2.copy()
        for _ in range(5):
            step=0.3
            
            _bar1 = _bar1.rotate(step*random.random()*PI/2).shift(step*random.random()*DOWN, step*random.random()*LEFT, step*random.random()*UP)
            _bar2 = _bar2.rotate(step*random.random()*PI/2).shift(step*random.random()*DOWN, step*random.random()*RIGHT, step*random.random()*UP)

            
            _field = manim_physics.BarMagneticField(_bar1, _bar2)
            
            
            self.play(
                Transform(bar1, _bar1),
                Transform(bar2, _bar2),
                Transform(field, _field), run_time=0.7)
            self.wait(0.3)