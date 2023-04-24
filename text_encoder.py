from PIL import Image
import math

with open('input.txt', 'r', errors="ignore") as input:
    text = input.read()
columns = math.ceil((math.ceil(len(text)/3)**(1/2)))
print(columns)
img = Image.new('RGB', (columns, columns))
chars = []
custom = {'@': 1, ' ': 2, '!': 3, '#': 4, '$': 5, '%': 6, '^': 7, '*': 8, '(': 9, ')': 10, '[': 11, ']': 12, '{': 13, '}': 14, ',': 15, '.': 16, '?': 17, '"': 18, "'": 19, '/': 20, '\\': 21, '1': 22, '2': 23, '3': 24, '4': 25, '5': 26, '6': 27, '7': 28, '8': 29, '9': 30, '0': 31}
R = 1
G = 1
B = 1
def pixelVal(letters, pos, img):
    v1 = []
    print(letters, pos)
    for letter in letters:
        asc = ord(letter)
        if asc >= 97 and asc <= 122:
            asc = (asc - 96) * 8
        else:
            try:
                asc = custom[chr(asc)] + 224
            except:
                print(chr(asc), 'Not Defined! Skipping with a space...')
                asc = 226
        v1.append(asc)
    print(round(v1[0])*R, round(v1[1])*G, round(v1[2])*B)
    img.putpixel((pos[0], pos[1]), (round(v1[0])*R, round(v1[1])*G, round(v1[2])*B))

text = text.lower()
column = 0
row = 0
for char in range(0, len(text)-2, 3):
    pixelVal((text[char], text[char+1], text[char+2]), (row, column), img)
    row += 1
    if row == columns:
        column += 1
        if column == columns:
            break
        row = 0

img.save(text.split(' ')[0]+'.png')