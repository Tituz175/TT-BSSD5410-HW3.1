from PIL import Image, ImageDraw
import colorsys


def compare_pixels_quick_sort(px1, px2):
    return px1[0][0] <= px2[0][0]

def compare_pixels_merge_sort(px1, px2):
    return px1[0][0] < px2[0][0]


# end def compare_pixels(pix1, pix2):

def storePixels(im):
    width = int(im.size[0])
    height = int(im.size[1])

    # store pixels in a list
    pixel_array = []
    yiq_pixels = []

    for j in range(height):
        for i in range(width):
            r, g, b = im.getpixel((i, j))
            yiq = colorsys.rgb_to_yiq(r / 255, g / 255, b / 255)
            yiq_pixels.append([yiq, (i, j)])
            pixel_array.append([(r, g, b), (i, j)])
        # end for j
    # end for i
    return pixel_array, yiq_pixels


# end def storePixels(im):

def pixels_to_image(im, pixels):
    outimg = Image.new("RGB", im.size)

    if type(pixels[0][0][0]) == float:
        yiq_out = []
        for p in pixels:
            r, g, b = colorsys.yiq_to_rgb(p[0][0], p[0][1], p[0][2])
            r, g, b = int(r * 255), int(g * 255), int(b * 255)
            yiq_out.append((r, g, b))
            outimg.putdata(yiq_out)
    else:
        outimg.putdata([p[0] for p in pixels])
    outimg.show()
    return outimg


# end def pixels_to_image(im, pixels):

def pixels_to_points(im, pixels):
    for p in pixels:
        if type(p[0][0]) == float:
            im.putpixel(p[1], tuple([int(v * 255) for v in colorsys.yiq_to_rgb(p[0][0], p[0][1], p[0][2])]))
        else:
            im.putpixel(p[1], p[0])
    # im.show()


# end def pixels_to_points(size, pixels):

def grayscale(im, pixels):
    draw = ImageDraw.Draw(im)
    for px in pixels:
        gray_av = int((px[0][0] + px[0][1] + px[0][2]) / 3)
        draw.point(px[1], (gray_av, gray_av, gray_av))

# end def grayscale(im, pixels):
