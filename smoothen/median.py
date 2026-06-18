from PIL import Image

img = Image.open("../../../Downloads/BROWSER/dembouz.jpeg").convert("L")
w, h = img.size
p = img.load()

out = Image.new("L", (w, h))
o = out.load()

for y in range(1, h-1):
    for x in range(1, w-1):

        values = []

        for j in range(-1, 2):
            for i in range(-1, 2):
                values.append(p[x+i, y+j])

        values.sort()
        median = values[4]   # middle of 9 elements

        o[x, y] = median

out.show()