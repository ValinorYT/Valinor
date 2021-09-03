import numpy as np
from manim import Circle

from config import MY_COLORS

labels = [
    1,  # 0
    0,  # 1
    2,  # 2
    2,  # 3
    2,  # 4
    0,  # 5
    0,  # 6
    1,  # 7
    1,  # 8
    2,  # 9
    0,  # 10
    0,  # 11
    2,  # 12
    1,  # 13
    1,  # 14
]

positions = [
    [4.740375187660731, 0.7372038883912031],  # 0
    [-5.169838445288768, 3.558490331731283],  # 1
    [-2.2010512520402195, -1.3604007076600038],  # 2
    [1.521645979765103, -8.473850908419028],  # 3
    [5.399825082420257, -6.63938708380591],  # 4
    [-2.5332257266009535, 5.021910257994006],  # 5
    [0.5311241511570319, 1.3577235694576952],  # 6
    [3.8686089420855656, 0.1825256749907611],  # 7
    [13.564950081028758, 0.7100914907179231],  # 8
    [1.191267879396479, -5.0859315637617835],  # 9
    [2.6370386813372213, -2.694247067909828],  # 10
    [-1.0061421805504178, 3.7349533797037338],  # 11
    [3.3687941136203694, -6.266528644895686],  # 12
    [7.155170246177843, 3.265755849282281],  # 13
    [0.01794618521252178, 6.213779101812003],  # 14
]
positions = np.array([[float(line[0]) / 3, float(line[1]) / 3, 0] for line in positions])

dots = [Circle(color=MY_COLORS[labels[i]], radius=.15, stroke_width=5, fill_opacity=.1).move_to(positions[i])
        for i in range(len(positions))]
