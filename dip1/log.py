from PIL import Image
from math import log

img = Image.open("../input.png").convert("L")
w, h = img.size
pix = img.load()

out = Image.new("L", (w, h))
out_pix = out.load()

c = 255 / log(256)
a = 1 / 255
g = 1/2.2

for i in range(w):
    for j in range(h):
        r = pix[i, j]
        out_pix[i, j] = int(c * (log(1 + r)))

out.save("log.png")
