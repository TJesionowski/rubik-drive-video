import numpy as np

from manim import *
from manim_rubikscube import *

class CanonicalCube(ThreeDScene):
    def construct(self):
        cube = RubiksCube().scale(0.5)
        axis = ThreeDAxes()

        # I don't like this rotation but I can't figure out how to get the right perspective.
        #self.renderer.camera.phi=45*DEGREES
        #self.renderer.camera.theta=30*DEGREES
        #self.renderer.camera.frame_center = cube.get_center()
        #self.renderer.camera.frame_center = cube.cubies[1,1,1].get_rounded_center()
        #self.renderer.camera.distance_to_origin = 100
        self.set_camera_orientation(phi =   60*DEGREES,
                                    theta = 45*DEGREES,
                                    focal_distance=20,
                                    zoom=0.8)
        

        # This is what I don't like about the perspective, the directions are all funky.
        #right, left, up, down, _in, out = UP, DOWN, OUT, IN, RIGHT, LEFT


        self.play(Create(cube), Create(axis))

        testcubie = cube.cubies[2,2,2]

        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()
        #self.begin_ambient_camera_rotation(about="theta")

        actions = Succession(Indicate(cube.cubies[2,2,2]),
                             Wait(run_time=2),
                             Indicate(cube.cubies[0,0,0]))

        view = Succession(Wait(run_time=1),
                          theta.animate.set_value((30+180)*DEGREES),
                          Wait(run_time=1))
        self.play(AnimationGroup(
            actions,
            view))
