#!/usr/bin/env python3

import sys
from pathlib import Path

path = str(Path().absolute())
print("Adding {} to system path...".format(path))
sys.path.insert(0, path)

import numpy as np
import matplotlib.pyplot as plt

from panim.lsystem import LSystemAnimator
from panim.transformers import ZoomTransformer

plt.style.use('dark_background')


def main():
    angle = 90
    axiom = 'L'
    rule = {
        'L': '-RF+LFL+FR-',
        'R': '+LF-RFR-FL+'
    }
    iteration = 5
    n = 40
    animator = LSystemAnimator(
        interval=5,
        iteration=iteration,
        rule=rule,
        axiom=axiom,
        turn_angle=angle,
        start_position=(n//2, -n//2),
        nlimit=n
    )

    zoomer = ZoomTransformer(animobj=animator, factor=500)
    zoomer.animate(len(animator.coords))
    zoomer.save("out/hilbert.mp4")

if __name__ == "__main__":
    main()

