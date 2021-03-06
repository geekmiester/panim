#!/usr/bin/env python3

import numpy as np
from scipy.ndimage.filters import gaussian_filter

import matplotlib.pyplot as plt
from matplotlib import animation
import random

from panim.animator import (
    AbstractImageAnimator,
    AbstractAnimator
)
from panim.utils import (
    meshgrid_polar,
    get_image_array
)

plt.style.use('dark_background')

class GenerativeArt(AbstractImageAnimator):
    def __init__(self, **args):
        super().__init__(**args)
        self.r, self.a = meshgrid_polar(self.image_size)
        self.lr = np.log(1 + self.r)
        self.factor = -50
        self.p, self.q, self.r = -50, -40, 20

    def update(self, i):
        if -5 < self.p < 5:
            self.p += 0.01
        else:
            self.p += 0.2
        self.q += 0.1
        array = np.sin(self.a * self.p+ np.sin(self.lr * self.q) + self.lr*self.r)
        array = np.fmod((1 + array + self.lr), 1)
        array = get_image_array(array, normalize=False)
        return array

class RandomlyVanishingPixelArt(AbstractImageAnimator):
    def __init__(self, **args):
        super().__init__(**args)
        self.array = np.zeros((self.image_size[1], self.image_size[0]))
        self.val = 1
        self.white_spawn_rate = 0.9

    def update(self, i):
        w, h = 40, 40
        r, c = random.randint(2*w, self.image_size[1]-2*w), random.randint(2*h, self.image_size[0]-2*h)
        v = random.uniform(0, 1)
        if self.val < 0.8:
            self.array[r:r+w, c:c+h] = self.val
        elif v > (1-self.white_spawn_rate) and self.val >= 0.6:
            self.array[r:r+w, c:c+h] = 1
        self.val -= 0.001
        return self.array


def main():
    animator = GenerativeArt(interval=1, clockwise=False, factor=0.1)
    animator.animate(2000)
    animator.save("out/spiral.mp4")

if __name__ == "__main__":
    main()

