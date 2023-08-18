import numpy as np

from manim import *
from manim_rubikscube import *

class Solve(ThreeDScene):
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
        state = "UUUUUUUUULLLFFFRRRBBBLLLFFFRRRBBBLLLFFRDRRBBBDDFDDDDDD"
        cube.set_state(state)
        self.add(cube)
        cube.show()

        try:
            # Loop through results of the kociemba algorithm
            for i, m in enumerate(cube.solve_by_kociemba(state)):
                # Execute the move
                self.play(CubeMove(cube, m), run_time=1.5)
        except ValueError:
            raise

        self.wait(5)
