import numpy as np

from manim import *
from manim_rubikscube import *

global FUCKY
FUCKY = False

class AllTogetherExample(ThreeDScene):
    def construct(self):
        # Change the cube from default colors
        #cube = RubiksCube(colors=[WHITE, ORANGE, DARK_BLUE, YELLOW, PINK, "#00FF00"]).scale(0.6)
        cube = RubiksCube()

        # I don't like this rotation but I can't figure out how to get the right perspective.
        self.move_camera(phi=PI/4, theta=PI/6)
        #self.renderer.camera.frame_center = cube.get_center()
        #self.renderer.camera.frame_center = cube.cubies[1,1,1].get_rounded_center()

        # This is what I don't like about the perspective, the directions are all funky.
        right, left, up, down, _in, out = UP, DOWN, OUT, IN, RIGHT, LEFT

        # Set the state of the cube
        # state = "BBFBUBUDFDDUURDDURLLLDFRBFRLLFFDLUFBDUBBLFFUDLRRRBLURR"
        # cube.set_state(state)
        self.add(cube)
        cube.show()

        #self.play(FadeIn(cube))
        self.wait()

        testcubie = cube.cubies[2,2,2]

        # self.play(Indicate(testcubie))
        # self.play(testcubie.animate.shift(OUT))
        # self.play(testcubie.animate.rotate(PI/2, about_point=testcubie.get_rounded_center()))
        # self.play(testcubie.animate.shift(IN))

        # A = testcubie
        # Ax = A.get_x()
        # B = cube.cubies[1,2,2]
        # Bx = B.get_x()
        # breakpoint() # cubies[1,2,2].get_rounded_center()
        # cube.set_indices()
        # self.play(AnimationGroup(*[
        #     #A.animate.shift(_in)
        #     A.animate.set_x(Bx),
        #     B.animate.set_x(Ax)
        # ]))
        # cube.adjust_indices(cube.cubies)

        # # Loop through results of the kociemba algorithm
        # for i, m in enumerate(cube.solve_by_kociemba(state)):
        #     # Execute the move
        #     self.play(CubeMove(cube, m), run_time=1.5)

        self.wait(5)
