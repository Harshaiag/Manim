from manim import *

class NameofAnimation(Scene):
    def construct(self):
        # Code for animation goes here
        box = Rectangle(stroke_color=GREEN_C, fill_color=BLACK, fill_opacity=1, stroke_width=3).scale(2)
        circle = Circle(color=RED, fill_opacity=1).scale(2)
        text = Text("Hello There", font="Futura", stroke_width=0).scale(1.5)
        
        self.wait(1)
        self.add(box)
        
        self.play(box.animate.shift(UP*2),run_time=2)
        self.wait(1)
        self.play(Transform(box,circle),run_time=2)
        self.wait(1)
        self.play(Transform(box,text),run_time=2)
        self.wait(1)
        
        
class SquareToCircle(Scene):
    def construct(self):
        for i in range(4):
            circle = Circle()  # create a circle
            circle.set_fill(PINK, opacity=0.5)  # set color and transparency

            square = Square()  # create a square
            square.rotate(PI / 4)  # rotate a certain amount
        
            self.play(Create(square))  # animate the creation of the square
            self.play(Transform(square, circle))  # interpolate the square into the circle
            self.play(FadeOut(square))  # fade out animation
            
            
class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(
            ReplacementTransform(square, circle)
        )  # transform the square into a circle
        self.play(
            circle.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen
        
class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), right_square.animate.rotate(PI), run_time=2
        )
        self.wait()
        
from manim import *

class TextExample(Scene):
    def construct(self):
        # Create a Text object
        text = Text("Hello, Manim!", font_size=48)

        # Position the text on the scene
        text.to_edge(UP)

        # Add the text to the scene
        self.add(text)

        # Play the animation
        self.wait(2)
        
        
class ShapesLogo(Scene):
    def construct(self):
        
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        stream_lines = StreamLines(func, stroke_width=2, max_anchors_per_line=30)
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)
        
        circle = Circle( fill_opacity=0.7).shift(2 * LEFT, 2 * UP)
        square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT, 2 * UP)
        triangle = Triangle(color=RED, fill_opacity=0.7).shift(2 * DOWN,2*LEFT)
        pentagon = Circle(fill_opacity=0.7).shift(2 * DOWN,2*RIGHT)
        textc = Text("Hello, There", font_size=48).shift(2 * LEFT, 2 * UP)
        texts = Text("Hello, There", font_size=48).shift(2 * RIGHT, 2 * UP)
        textt = Text("Hello, There", font_size=48).shift(2 * DOWN,2*LEFT)
        textp = Text("Hello, There", font_size=48).shift(2 * DOWN,2*RIGHT)
        
        
        self.wait(1)
        self.play(Create(circle),Create(square),Create(triangle),Create(pentagon),run_time=2)
        self.wait(1)
        self.play(circle.animate.set_fill(PINK, opacity=0.5), Rotate(square,PI/4), pentagon.animate.set_fill(PINK, opacity=0.5), Rotate(triangle,PI/4) ,run_time=2)
        self.wait(1)
        self.play(Transform(circle,textc),Transform(square,texts),Transform(triangle,textt),Transform(pentagon,textp),run_time=2)
        self.wait(1)
        


import random
from manim import *

class Commence(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        stream_lines = StreamLines(func, stroke_width=2, max_anchors_per_line=30)
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)
        
        # Number of repetitions
        num_repetitions = 2

        title_text = "The Hackathon will Begin Shortly"
        title_text = Text(title_text, font="Futura Light", stroke_width=0)
        for i in range(num_repetitions):
            self.play(Create(title_text))
            self.wait(3)
            self.play(FadeOut(title_text))
        
