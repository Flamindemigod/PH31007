from manim import *
import numpy as np

class Maxwell(ThreeDScene):
    def construct(self):
        img = ImageMobject("media/Assets/Maxwell.png").scale(0.8)
        imgLabel = Tex("James Clerk Maxwell")
        imgLabel.move_to(img.get_bottom()).shift(0.5*DOWN)
        self.play(FadeIn(img, shift=IN), Write(imgLabel))
        self.wait(2)
        self.play(FadeOut(img, shift=IN), Unwrite(imgLabel))

        #self.play(img.animate.to_corner(UP+LEFT).shift(DOWN+RIGHT), rate_func=rate_functions.ease_in_out_cubic, run_time=2)


class Gauss(ThreeDScene):
    def construct(self):
        img = ImageMobject("media/Assets/Gauss.png").scale(0.5)
        imgLabel = Tex("Johann Carl Friedrich Gauss")
        imgLabel.move_to(img.get_bottom())
        self.play(FadeIn(img, shift=IN), Write(imgLabel))
        self.wait(2)
        self.play(FadeOut(img, shift=IN), Unwrite(imgLabel))

        #self.play(img.animate.to_corner(UP+LEFT).shift(DOWN+RIGHT), rate_func=rate_functions.ease_in_out_cubic, run_time=2)

class Stokes(ThreeDScene):
    def construct(self):
        img = ImageMobject("media/Assets/Stokes.png").scale(0.4)
        imgLabel = Tex("George Stokes")
        imgLabel.move_to(img.get_bottom()).shift(0.5*DOWN)
        self.play(FadeIn(img, shift=IN), Write(imgLabel))
        self.wait(2)
        self.play(FadeOut(img, shift=IN), Unwrite(imgLabel))

        #self.play(img.animate.to_corner(UP+LEFT).shift(DOWN+RIGHT), rate_func=rate_functions.ease_in_out_cubic, run_time=2)
