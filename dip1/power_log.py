from PIL import Image
from math import log

img = Image.open("../input.png").convert("L")
w, h = img.size
pix = img.load()

out_g1 = Image.new("L", (w, h))
out_pix_g1 = out_g1.load()

out_g2 = Image.new("L", (w, h))
out_pix_g2 = out_g2.load()

out_g3 = Image.new("L", (w, h))
out_pix_g3 = out_g3.load()

g1, g2, g3 = 1, 0.5, 2

c = 255 / log(256)

for i in range(w):
    for j in range(h):
        s = c * pix[i, j]
        out_pix_g1[i, j] = int(s ** g1)
        out_pix_g2[i, j] = int(s ** g2)
        out_pix_g3[i, j] = int(s ** g3)

out_g1.save("power_log1.png")
out_g2.save("power_log2.png")
out_g3.save("power_log3.png")
