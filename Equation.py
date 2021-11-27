from manim import *

class AME(Scene):
  
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

class GaussDivergence(Scene):
    def construct(self):
        GDTEqn = MathTex(r"\iiint_V (\nabla\cdot \vec{F} ) dV", r"=", r"\oiint_S (F\cdot\hat{n})dS")
        title = Tex(r"Gauss Divergence Theorem")
        VGroup(GDTEqn, title).arrange(DOWN)

        
        self.play(
            Write(title)
        )
        self.play(FadeIn(GDTEqn, shift=DOWN))
        self.wait(3)
        self.play(
            FadeOut(GDTEqn),
            Unwrite(title))
        self.wait()
        return

class StokesTheorem(Scene):
    def construct(self):
        STEqn = MathTex(r"\iint_\Sigma (\nabla\times A ) \cdot a", r"=", r"\oint_{\delta\Sigma} A\cdot dl")
        title = Tex(r"Stokes' theorem")
        VGroup(STEqn, title).arrange(DOWN)

        
        self.play(
            Write(title)
        )
        self.play(FadeIn(STEqn, shift=DOWN))
        self.wait(3)
        self.play(
            FadeOut(STEqn),
            Unwrite(title))
        self.wait()
        return
