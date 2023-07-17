from manim import *
from manim_rubikscube import *

class AllTogetherExample(ThreeDScene):
    def construct(self):
        # Change the cube from default colors
        cube = RubiksCube(colors=[WHITE, ORANGE, DARK_BLUE, YELLOW, PINK, "#00FF00"]).scale(0.6)

        self.move_camera(phi=50*DEGREES, theta=160*DEGREES)
        self.renderer.camera.frame_center = cube.get_center()

        # Set the state of the cube
        state = "BBFBUBUDFDDUURDDURLLLDFRBFRLLFFDLUFBDUBBLFFUDLRRRBLURR"
        cube.set_state(state)

        self.play(FadeIn(cube))
        self.wait()

        # Loop through results of the kociemba algorithm
        for m in cube.solve_by_kociemba(state):
            # Execute the move
            self.play(CubeMove(cube, m), run_time=1.5)

        # Show the final product
        self.play(
            Rotating(cube, radians=2*PI, run_time=2)
        )
