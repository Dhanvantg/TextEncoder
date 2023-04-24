from PIL import Image
name = input('Enter name of image: ')
im = Image.open(name+'.png', 'r')
pxls = list(im.getdata())
output = ""
custom = {'@': 1, ' ': 2, '!': 3, '#': 4, '$': 5, '%': 6, '^': 7, '*': 8, '(': 9, ')': 10, '[': 11, ']': 12, '{': 13, '}': 14, ',': 15, '.': 16, '?': 17, '"': 18, "'": 19, '/': 20, '\\': 21, '1': 22, '2': 23, '3': 24, '4': 25, '5': 26, '6': 27, '7': 28, '8': 29, '9': 30, '0': 31}
for pxl in pxls:
    for char in pxl:
        if char < 225:
            output += chr(char//8+96)
        else:
            value = {i for i in custom if custom[i]==char-224}
            print(value)
            output += str(value)[2]
print(output.replace('`', ''))