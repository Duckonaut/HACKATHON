import pytesseract
import PIL
import sys

def main():
    if len(sys.argv) < 2:
        print('You need to pass the image filename')
        return

    source = PIL.Image.open(sys.argv[1])

    print(pytesseract.image_to_string(source).strip())


if __name__ == '__main__':
    main()
