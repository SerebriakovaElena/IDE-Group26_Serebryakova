from PIL import Image
import numpy as np

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
    image_file = Image.open(input("Введите имя исходного изображения: "))
    mosaic_size = int(input('Введите размер мозайки: '))
    gradations_count = int(input('Введите градацию серого: '))
    image = np.array(image_file)
    number_of_shades = 255 // gradations_count

    res = Image.fromarray(paint_mosaic(image, mosaic_size , number_of_shades ))
    res.save(input("Введите имя результирующего изображения: "))

main()
print("Мозаика готова!")