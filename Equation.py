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

class AMEDiffren(Scene):
    def construct(self):
        title = Tex("Ampere-Maxwell equation (Integral Form)")
        AMEIntegral = MathTex(r"\oint_C \vec{\mathbf{b}} \cdot \vec{\mathbf{dl}}", r"=",  r"\mu_0 I_{enc} + \mu_0 \varepsilon_0 \frac{d\Phi_E}{dt}")
        AMEIntegralIntermediate = MathTex(r"\oint_C \vec{\mathbf{b}} \cdot \vec{\mathbf{dl}}", r"=",  r"\iint_{\mathbf{S}}\mu_0 \mathbf{J}\cdot d\mathbf{S} + \iint_{\mathbf{S}}\mu_0 \varepsilon_0 \frac{\delta \mathbf{E}}{\delta t}\cdot d\mathbf{S}")
        AMEIntegralDensityVersion = MathTex(r"\oint_C \vec{\mathbf{b}} \cdot \vec{\mathbf{dl}}", r"=",  r"\iint_{\mathbf{S}}(\mu_0 \mathbf{J} + \mu_0 \varepsilon_0 \frac{\delta \mathbf{E}}{\delta t})\cdot d\mathbf{S}")
        AMEDiffrentialDensityVersion = MathTex(r"\nabla \times \mathbf{B}", r"=",  r"\mu_0 \mathbf{J} + \mu_0 \varepsilon_0 \frac{\delta\mathbf{E}}{\delta t}")
        AMEDiffrentialDensityVersionSeperated = MathTex(r"\nabla \times \mathbf{B}", r"=",  r"\mu_0",r"\mathbf{J}", "+",r"\mu_0 \varepsilon_0", r"\frac{\delta\mathbf{E}}{\delta t}")

        VGroup(title, VGroup(AMEIntegral, AMEIntegralIntermediate, AMEIntegralDensityVersion, AMEDiffrentialDensityVersion, AMEDiffrentialDensityVersionSeperated)).arrange(DOWN)
        AMEHighlightJ = Brace(AMEDiffrentialDensityVersionSeperated[3], buff = .1)
        AMEHighlightJLabel = AMEHighlightJ.get_text("Current Density").scale(0.5)
        AMEHighlightE = Brace(AMEDiffrentialDensityVersionSeperated[-1], buff = .1)
        AMEHighlightELabel = AMEHighlightE.get_text("Change in Electric Field").scale(0.5)

        self.play(Write(title))
        self.play(FadeIn(AMEIntegral, shift=UP))
        self.wait()
        self.play(Transform(AMEIntegral, AMEIntegralIntermediate))
        self.wait()
        self.play(Transform(AMEIntegral, AMEIntegralDensityVersion))
        self.wait()
        self.play(Transform(AMEIntegral, AMEDiffrentialDensityVersion), title.animate.become(Tex("Ampere-Maxwell equation (Diffrential Form)").move_to(title)))
        self.wait()
        self.play(Create(VGroup(AMEHighlightJ, AMEHighlightJLabel, AMEHighlightE, AMEHighlightELabel)))
        self.wait()
        self.play(Uncreate(VGroup(AMEHighlightJ, AMEHighlightJLabel, AMEHighlightE, AMEHighlightELabel)))
        self.play(FadeOut(AMEIntegral, shift=DOWN))
        self.play(Unwrite(title))
        self.wait()

class Maxwell1(Scene):
    def construct(self):
        Eqn = MathTex(r"\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0}")
        title = Tex(r"Gauss's Law for Static Electric Fields")
        VGroup(Eqn, title).arrange(UP)

        
        self.play(
            Write(title)
        )
        self.play(FadeIn(Eqn, shift=UP))
        self.wait(2)
        self.play(
            FadeOut(Eqn),
            Unwrite(title))
        self.wait()
        return

class Maxwell2(Scene):
    def construct(self):
        Eqn = MathTex(r"\nabla \cdot \mathbf{B} = 0")
        title = Tex(r"Gauss's Law for Static Magnetic Fields")
        VGroup(Eqn, title).arrange(UP)

        
        self.play(
            Write(title)
        )
        self.play(FadeIn(Eqn, shift=UP))
        self.wait(2)
        self.play(
            FadeOut(Eqn),
            Unwrite(title))
        self.wait()
        return

class Maxwell3(Scene):
    def construct(self):
        Eqn = MathTex(r"\nabla \times \mathbf{E} = \frac{\delta\mathbf{B}}{\delta t}")
        title = Tex(r"Faraday's Law of Induction")
        VGroup(Eqn, title).arrange(UP)

        
        self.play(
            Write(title)
        )
        self.play(FadeIn(Eqn, shift=UP))
        self.wait(2)
        self.play(
            FadeOut(Eqn),
            Unwrite(title))
        self.wait()
        return

class Maxwell4(Scene):
    def construct(self):
        Eqn = MathTex(r"\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \varepsilon_0 \frac{\delta\mathbf{E}}{\delta t}")
        title = Tex(r"Ampere-Maxwell Law")
        VGroup(Eqn, title).arrange(UP)

        
        self.play(
            Write(title)
        )
        self.play(FadeIn(Eqn, shift=UP))
        self.wait(2)
        self.play(
            FadeOut(Eqn),
            Unwrite(title))
        self.wait()
        return

class AllMaxwell(Scene):
    def construct(self):
        title = Tex(r"Maxwell's equations")
        Eqn1 = MathTex(r"\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0}")
        Eqn2 = MathTex(r"\nabla \cdot \mathbf{B} = 0")
        Eqn3 = MathTex(r"\nabla \times \mathbf{E} = \frac{\delta\mathbf{B}}{\delta t}")
        Eqn4 = MathTex(r"\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \varepsilon_0 \frac{\delta\mathbf{E}}{\delta t}")
        VGroup(title, Eqn1, Eqn2, Eqn3, Eqn4).arrange(DOWN)

        
        self.play(
            Write(title)
        )
        self.play(
            Write(Eqn1),
            Write(Eqn2),
            Write(Eqn3),
            Write(Eqn4),
            )
        self.wait(5)
        self.play(
            FadeOut(Eqn1, Eqn2, Eqn3, Eqn4),
            Unwrite(title))
        self.wait()
        return