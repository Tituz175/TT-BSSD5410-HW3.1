import colorsys

from SortFunctions import quickSortIterative, selection_sort, mergesort
from SearchFunctions import binarySearch_sub
from PixelFunctions import storePixels, pixels_to_image, compare_pixels_quick_sort, compare_pixels_merge_sort, \
    pixels_to_points, grayscale
from PIL import Image


def rgb_input():
    valid_color = False
    threshold = input("Kindly enter desire rgb values separated by comma: ")
    red, green, blue = tuple(int(v) for v in threshold.split(","))
    if red <= 255 and green <= 255 and blue <= 255:
        valid_color = True
    return valid_color, red, green, blue


# end def rgb_input():

def im_highlight(IMG_NAME, tuple):
    with Image.open(IMG_NAME + ".jpg") as image:
        pixels, yiq_pixels = storePixels(image)
        yiq_pixels = mergesort(yiq_pixels, compare_pixels_merge_sort)
        target = (tuple[0] / 255, tuple[1] / 255, tuple[2] / 255)
        yiq_target = colorsys.rgb_to_yiq(target[0], target[1], target[2])
        sub_index = binarySearch_sub([r[0][0] for r in yiq_pixels], 0, len(yiq_pixels) - 1, yiq_target[0])
        print("target found at: ", sub_index)
        grayscale(image, pixels)
    return image, yiq_pixels, sub_index


# end def im_highlight():


def main():
    print("=======================================================")
    print("\t\t\tWelcome to Pixel Manipulation")
    print("\t\t   Press Q to Quit and save picture")
    print("\t\t   Press R to Reverse the highlight")
    print("\t\t Press T to Modify the highlighted area")
    print("\t\t Press C to Change the highlighted color")
    print("=======================================================")

    global sub_index
    global yiq_pixels
    global sub_index_position
    global pixels
    global image_copy

    IMG_NAME = "monkey"

    valid_color, red, green, blue = rgb_input()
    if valid_color:
        image, yiq_pixels, sub_index = im_highlight(IMG_NAME, (red, green, blue))

        tempimage = image.copy()
        reversed = False

        sub_index_position = True
        pixels_to_points(image, yiq_pixels[sub_index:])
        image.show()

        choice = input("Select an option: ").upper()

        while choice != "Q":

            if choice == "R":
                if not reversed:
                    pixels_to_points(tempimage, yiq_pixels[:sub_index])
                    sub_index_position = False;
                    reversed = True
                    tempimage.show()
                    choice = input("Select an option: ").upper()
                else:
                    pixels_to_points(image, yiq_pixels[sub_index:])
                    sub_index_position = True;
                    reversed = False
                    image.show()
                    choice = input("Select an option: ").upper()

            if choice == "T":
                if sub_index_position:
                    tolerance = int(len(yiq_pixels) / 16)
                    sub_index -= tolerance
                    pixels_to_points(image, yiq_pixels[sub_index:])
                    image.show()
                else:
                    tolerance = int(len(yiq_pixels) / 16)
                    sub_index += tolerance
                    pixels_to_points(image, yiq_pixels[:sub_index])
                    image.show()
                choice = input("Select an option: ").upper()

            if choice == "C":
                valid_color, red, green, blue = rgb_input()
                if not valid_color:
                    print("rgb individual values can't be greater than 255")
                    return
                else:
                    image, yiq_pixels, sub_index = im_highlight(IMG_NAME, (red, green, blue))
                    pixels_to_points(image, yiq_pixels[sub_index:])
                    image.show()
                choice = input("Select an option: ").upper()

        else:
            image.save("highlighted_" + IMG_NAME + ".jpg", "JPEG")

    else:
        print("rgb individual values can't be greater than 255")


# end def main():


if __name__ == "__main__":
    main()
