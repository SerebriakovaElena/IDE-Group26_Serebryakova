from PIL import Image
import numpy as np
import time
start_time = time.time()

def paint_mosaic(arr, size, gradation_step):
    for i in range(0, len(arr), size):
        for j in range(0, len(arr[0]), size):
            arr[i:i + size, j:j + size] = count_average_brightness(
                arr[i:i + size, j:j + size], size, gradation_step)
    return arr

def count_average_brightness(block, size, gradation_step):
    average_color = (block[:size, :size].sum() / 3) // size ** 2
    return int(average_color // gradation_step) * gradation_step


def main():
    image_file = Image.open("scale1200.jpg")
    mosaic_size = 10
    gradations_count = 50
    image = np.array(image_file)
    number_of_shades = 255 // gradations_count

    res = Image.fromarray(paint_mosaic(image, mosaic_size , number_of_shades ))
    res.save("res.jpg")

main()
print("Мозаика готова!")

print ("time elapsed: {:.2f}s".format(time.time() - start_time))
