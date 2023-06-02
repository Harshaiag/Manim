from manim import *

class NameofAnimation(Scene):
    def construct(self):
        # Code for animation goes here
        box = Rectangle(stroke_color=GREEN_C, fill_color=BLACK, fill_opacity=1, stroke_width=3).scale(2)
        diagram1 = diagram1(color=RED, fill_opacity=1).scale(2)
        text = Text("Hello There", font="Futura", stroke_width=0).scale(1.5)
        
        self.wait(1)
        self.add(box)
        
        self.play(box.animate.shift(UP*2),run_time=2)
        self.wait(1)
        self.play(Transform(box,diagram1),run_time=2)
        self.wait(1)
        self.play(Transform(box,text),run_time=2)
        self.wait(1)
        
        
class diagram2Todiagram1(Scene):
    def construct(self):
        for i in range(4):
            diagram1 = diagram1()  # create a diagram1
            diagram1.set_fill(PINK, opacity=0.5)  # set color and transparency

            diagram2 = diagram2()  # create a diagram2
            diagram2.rotate(PI / 4)  # rotate a certain amount
        
            self.play(Create(diagram2))  # animate the creation of the diagram2
            self.play(Transform(diagram2, diagram1))  # interpolate the diagram2 into the diagram1
            self.play(FadeOut(diagram2))  # fade out animation
            
            
class Animateddiagram2Todiagram1(Scene):
    def construct(self):
        diagram1 = diagram1()  # create a diagram1
        diagram2 = diagram2()  # create a diagram2

        self.play(Create(diagram2))  # show the diagram2 on screen
        self.play(diagram2.animate.rotate(PI / 4))  # rotate the diagram2
        self.play(
            ReplacementTransform(diagram2, diagram1)
        )  # transform the diagram2 into a diagram1
        self.play(
            diagram1.animate.set_fill(PINK, opacity=0.5)
        )  # color the diagram1 on screen
        
class DifferentRotations(Scene):
    def construct(self):
        left_diagram2 = diagram2(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_diagram2 = diagram2(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_diagram2.animate.rotate(PI), right_diagram2.animate.rotate(PI), run_time=2
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
        
        diagram1 = Circle( fill_opacity=0.7).shift(2 * LEFT, 2 * UP)
        diagram2 = Circle(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT, 2 * UP)
        triangle = Triangle(color=RED, fill_opacity=0.7).shift(2 * DOWN,2*LEFT)
        pentagon = Circle(fill_opacity=0.7).shift(2 * DOWN,2*RIGHT)
        textc = Text("Hello, There", font_size=48).shift(2 * LEFT, 2 * UP)
        texts = Text("Hello, There", font_size=48).shift(2 * RIGHT, 2 * UP)
        textt = Text("Hello, There", font_size=48).shift(2 * DOWN,2*LEFT)
        textp = Text("Hello, There", font_size=48).shift(2 * DOWN,2*RIGHT)
        
        
        self.wait(1)
        self.play(Create(diagram1),Create(diagram2),Create(triangle),Create(pentagon),run_time=2)
        self.wait(1)
        self.play(diagram1.animate.set_fill(PINK, opacity=0.5), Rotate(diagram2,PI/4), pentagon.animate.set_fill(PINK, opacity=0.5), Rotate(triangle,PI/4) ,run_time=2)
        self.wait(1)
        self.play(Transform(diagram1,textc),Transform(diagram2,texts),Transform(triangle,textt),Transform(pentagon,textp),run_time=2)
        self.wait(1)
        


import random
from manim import *

class Commence(Scene):
    def construct(self):

        
        # Number of repetitions
        num_repetitions = 3

        title_text = "The Hackathon will Begin Shortly"
        title_text = Text(title_text, font="Futura Light", stroke_width=0)
        for i in range(num_repetitions):
            
            diagram1 = Triangle(color= ORANGE)
            diagram2 = Square(color= BLUE_E) if random.random()> 0.5 else Circle(color= BLUE_E)
        #Showing shapes
            self.play(Create(diagram1))

            self.play(Transform(diagram1, diagram2) ,run_time=2) 
            self.play(Rotate(diagram2,PI))
            self.play(FadeOut(diagram2),FadeOut(diagram1),run_time=2)
 
            self.play(Create(title_text))
            self.wait(3)
            self.play(FadeOut(title_text))
        
