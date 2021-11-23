import numpy as np
from PIL import Image

def count_average_brightness(block , size, gradation_step):
    """
    Give a array part (block), mosaic_size (size), gradiation_step
    Count average brightness for given block.

    :param word: list, int, int
    :return int
    >>> count_average_brightness(np.array(Image.open('scale1200.jpg')), 2, 5)
    190
     >>> count_average_brightness(np.array(Image.open('scale1200.jpg')), 10, 50)
     150
     >>> count_average_brightness(np.array(Image.open('scale1200.jpg')), 5, 20)
     180
    """

    average_color = (block[:size, :size].sum() / 3) // size ** 2
    return int(average_color // gradation_step) * gradation_step


if __name__ == "__main__":
    import doctest
    doctest.testmod()