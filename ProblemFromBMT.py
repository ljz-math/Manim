from manim import *

from manimlib import RIGHT

#manim ProblemFromBMT.py Example
#ProblemFromBMT
class Example(Scene):
    def construct(self):
        t1=Text("Evaluate:")
        self.play(Write(t1))
        self.play(t1.animate.shift(UP*2),run_time=1.5)

        g1=MathTex(r"\int_{0}^{\frac{1}{2}} \frac{1}{(1-x)^{\frac{1}{2}}(1+x)^{\frac{5}{2}}}dx")
        self.play(Write(g1))
        self.wait(1)
        target_font_size=30
        self.play(t1.animate.shift(UP*1.6+LEFT*4.4).scale(target_font_size/t1.font_size),g1.animate.shift(UP*2.2+LEFT*4.4).scale(target_font_size/g1.font_size),run_time=1.5)
#class Example2(Scene):
    #def construct(self):

        t2=Text("通过观察，我们发现:")
        self.play(Write(t2))
        self.play(t2.animate.shift(UP * 1.6).scale(target_font_size/t2.font_size), run_time=2)

        g2=MathTex(r"(1+x)^{\frac{5}{2}}=").shift(LEFT * 1)
        self.play(Write(g2))
        self.wait(1)

        g3=MathTex(r"\frac{(1+x)^3}{(1+x)^{\frac{1}{2}}}").shift(RIGHT * 1.3)
        self.play(Write(g3))
        self.wait(1)
        self.play(t2.animate.shift(UP*2.0+RIGHT*4.4).scale(target_font_size/t2.font_size),g2.animate.shift(UP * 2.2+RIGHT*4.7).scale(target_font_size/g2.font_size),g3.animate.shift(UP * 2.2+RIGHT*4.0).scale(target_font_size/g3.font_size),run_time=2)
        #self.play(g2.animate.shift(UP * 2), g3.animate.shift(UP * 2), run_time=1.5)
        #self.wait(2)
#class Example3(Scene):
    #def construct(self):
        #target_font_size=30

        t3=Text("代入原式可得:")
        self.play(Write(t3))
        self.wait(1)
        self.play(t3.animate.shift(UP * 1.6).scale(target_font_size / t3.font_size), run_time=2)

        g4=MathTex(r"\int_{0}^{\frac{1}{2}} \frac{1}{\sqrt\frac{1-x}{1+x}(1+x)^3}dx")
        self.play(Write(g4))
        self.play(FadeOut(t1,t2,t3,g1,g2,g3))
        self.wait(1)
        self.play(g4.animate.shift(UP * 1.6).scale(target_font_size / g4.font_size), run_time=2)
        #self.play(g4.animate.shift(LEFT*4.4))

        #t4=Text("再次化简:")
        #self.play(Write(t4))
        #self.wait(2)
        #self.play(t4.animate.shift(UP * 1.6).scale(target_font_size / t4.font_size), run_time=1.5)
        #g5=MathTex()
#class Example4(Scene):
    #def construct(self):
        #target_font_size = 30

        t4 = Text("换元:")
        self.play(Write(t4))
        self.play(FadeOut(g4))
        self.play(t4.animate.shift(UP * 1.6).scale(target_font_size/t4.font_size), run_time=1.5)

        g5 = MathTex(r"LET \quad t= \frac{1-x}{1+x}")
        self.play(Write(g5))
        self.wait(1)
        self.play(FadeOut(t4))
        self.play(g5.animate.shift(UP * 1.6).scale(target_font_size/g5.font_size), run_time=1.5)

        g6= MathTex(r"Therefore :\quad x= \frac{1-t}{1+t}")
        self.play(Write(g6))
        self.wait(1)
        self.play(FadeOut(g5))
        self.play(g6.animate.shift(UP * 1.6).scale(target_font_size / g6.font_size), run_time=1.5)

        g7=MathTex(r"When \quad x=0,t=1\\When \quad x=\frac{1}{2},t=\frac{1}{3}")
        self.play(Write(g7))
        self.wait(1)
        self.play(FadeOut(g6))
        self.play(g7.animate.shift(UP * 1.6).scale(target_font_size / g7.font_size), run_time=1.5)

        t5=Text("原式化为:")
        self.play(Write(t5))
        self.wait(1)
        self.play(FadeOut(g7))
        self.play(t5.animate.shift(UP * 1.6).scale(target_font_size / t5.font_size), run_time=1.5)

        g8=MathTex(r"\int_{1}^{\frac{1}{3}} \frac{(1+t)^3}{8\sqrt{t}} \times (-\frac{2}{(1+t)^2}dt)")
        self.play(Write(g8))
        self.wait(1)
        self.play(FadeOut(t5))
        self.play(g8.animate.shift(UP * 1.6).scale(target_font_size / g8.font_size), run_time=1.5)

        g9=MathTex(r"\frac{1}{2} \times \int_{\frac{1}{3}}^{1} (1+t)d\sqrt{t}")
        border = Rectangle(width=g9.width + 0.4, height=g9.height + 0.4, color=YELLOW)
        border.move_to(g9)
        self.play(Write(g9))
        self.play(Write(border))
        self.wait(2)
        self.play(FadeOut(g8))
        self.play(g9.animate.shift(UP*1.6+LEFT*4.4),border.animate.shift(UP*1.6+LEFT*4.4),run_time=1.5)

        g10 = MathTex(r"LET \quad m= \sqrt{t}")
        self.play(Write(g10))
        self.wait(1)
        self.play(g10.animate.shift(UP * 1.6).scale(target_font_size / g10.font_size), run_time=1.5)

        g11 = MathTex(r"When \quad t=1,m=1\\When \quad t=\frac{1}{3},m=\frac{\sqrt{3}}{3}")
        self.play(Write(g11))
        self.wait(1)
        self.play(FadeOut(g10))
        self.play(g11.animate.shift(UP * 1.6).scale(target_font_size / g11.font_size), run_time=1.5)

        t6 = Text("原式化为:")
        self.play(Write(t6))
        self.wait(1)
        self.play(FadeOut(g11))
        self.play(t6.animate.shift(UP * 1.6).scale(target_font_size / t6.font_size), run_time=1.5)

        g12=MathTex(r"\frac{1}{2} \times \int_{\frac{\sqrt{3}}{3}}^{1} (1+m^2)dm")
        self.play(Write(g12))
        self.wait(1)
        self.play(FadeOut(t6))
        self.play(g12.animate.shift(UP * 1.6).scale(target_font_size / g12.font_size), run_time=1.5)

        g13=MathTex(r"[\frac{1}{2}m]_{\frac{\sqrt{3}}{3}}^{1}+[\frac{1}{6}m^3]_{\frac{\sqrt{3}}{3}}^{1}")
        self.play(Write(g13))
        self.wait(1)
        self.play(FadeOut(g12))
        self.play(g13.animate.shift(UP * 1.6).scale(target_font_size / g13.font_size), run_time=1.5)

        g14=MathTex(r"=\frac{2}{3}-\frac{5\sqrt{3}}{27}")
        self.play(Write(g14))
        self.wait(1)
        self.play(FadeOut(g13,g14,g9,border))

        t7=Text("感谢倾听!!!",color=YELLOW)
        self.play(Write(t7))
        self.wait(1)
        self.play(FadeOut(t7))