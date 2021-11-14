from manim import *

class Equation(Scene):
  
    def construct(self):
        title = Tex(r"Ampere-Maxwell equation")
        AMEqn = MathTex(r"\oint_C \vec{\mathbf{b}} \cdot \vec{\mathbf{dl}}", r"=",  r"\mu_0 I_{enc}", "+", r"\mu_0 \varepsilon_0 \frac{d\Phi_E}{dt}")
        AmpEqn = AMEqn[:3]
        framebox1 = Brace(AmpEqn[-1], buff = .1).shift(0.5*DOWN)
        fb1text = framebox1.get_text("Ampere Contribution").scale(0.5)
        fb1 = VGroup(framebox1, fb1text)
        framebox2 = Brace(AMEqn[-1], buff = .1).shift(0.3*DOWN)
        fb2text = framebox2.get_text("Maxwell Contribution").scale(0.45)
        fb2 = VGroup(framebox2, fb2text)

        VGroup(title, AMEqn).arrange(DOWN)
        self.play(
            Write(title)
        )
        self.play(FadeIn(AMEqn, shift=DOWN))
        self.play(FadeIn(fb1, fb2))
        self.play(
            FadeOut(AMEqn[3:]),
            FadeOut(fb1, fb2)
            )
        self.remove(AMEqn)
        self.play(AmpEqn.animate.move_to(title).shift(DOWN))
        self.wait()
        return
