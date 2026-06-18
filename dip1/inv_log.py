from PIL import Image
from math import log, exp

img = Image.open("../input.png").convert("L")
w, h = img.size
pix = img.load()

out = Image.new("L", (w, h))
out_pix = out.load()

c = 255 / log(256)

for i in range(w):
    for j in range(h):
        r = pix[i, j]
        out_pix[i, j] = int(exp(r / c) - 1)

out.save("inv_log.png")
