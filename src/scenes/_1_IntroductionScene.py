import os
from pathlib import Path

from manim import *

from src.data.dots.dots1 import positions, labels2
from src.data.dots.utils import get_dots, get_positions
from src.data.graphics_stuff import LABEL_COLORS
from src.scenes.KNN_Scene import KNN_Scene


class IntroductionScene(KNN_Scene):
    dots = get_dots(get_positions(positions), labels2)

    def construct(self):
        self.play(Create(VGroup(*self.dots)))

        self.x.move_to([1, 1.2, 0])
        self.add(self.x, self.x_circle)

        self.wait(2)
        self.play(self.x.animate.set_color(LABEL_COLORS[2]), run_time=.6)
        self.wait(2)
        self.play(self.x.animate.set_color(LABEL_COLORS[0]), run_time=.6)
        self.wait(2)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} Changing_NB_1 -pqp")
