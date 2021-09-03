import os
from pathlib import Path

from manim import *

from scenes.KNN_Scene import KNN_Scene


class Scene1(KNN_Scene):

    def construct(self):
        KNN_Scene.construct(self)
        self.play(self.tracker.animate.set_value(2), rate_func=linear, run_time=2)
        self.wait(3)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} Scene1 -pql")
