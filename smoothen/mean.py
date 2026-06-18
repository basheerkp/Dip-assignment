from PIL import Image

img = Image.open("../../../Downloads/BROWSER/dembouz.jpeg").convert("L")
w, h = img.size
p = img.load()

out = Image.new("L", (w, h))
o = out.load()

for y in range(1, h - 1):
    for x in range(1, w - 1):
        s = 0

        for j in range(-1, 2):
            for i in range(-1, 2):
                s += p[x + i, y + j]

        mean = s // 9
        o[x, y] = mean

out.show()