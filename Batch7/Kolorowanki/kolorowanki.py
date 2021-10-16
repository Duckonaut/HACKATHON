from PIL import Image, ImageColor
import sys
import os

from PIL.ImagePalette import ImagePalette

COLOR_NUMBER = 8

def getPixel(data):
    pass

def main():
    if len(sys.argv) < 2:
        print('You need to pass the image filename')

    source = Image.open(sys.argv[1])
    source = source.convert('RGBA')

    midpoint = source.convert('RGBA')

    midpoint = midpoint.quantize(colors=COLOR_NUMBER)
    midpoint.save('midpoint.png')

    destination = Image.new('RGB', (source.width, source.height), (0, 0, 0))
    
    for c in range(COLOR_NUMBER):
        for x in range(midpoint.width):
            for y in range(midpoint.height):
                if midpoint.getpixel((x, y)) == c:
                    allNearbySimilar = True

                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if i != 0 or j != 0:
                                if x+i >= 0 and x+i < midpoint.width and y+j >= 0 and y+j < midpoint.height:
                                    if midpoint.getpixel((x+i, y+j)) != c:
                                        allNearbySimilar = False
                    if allNearbySimilar:
                        destination.putpixel((x, y), (255, 255, 255))
                    else:
                        destination.putpixel((x, y), (0, 0, 0))
    
    destination.save('output.png')


if __name__ == '__main__':
    main()
