from PIL import Image

img = Image.open("../input.png").convert("L")
w, h = img.size
pix = img.load()

out = Image.new("L", (w, h))
out_pix = out.load()

r1, r2 = 10,200
s1, s2 = 90, 190
s = 0

for i in range(w):
    for j in range(h):
        r = pix[i, j]

        if 0 <= r <= r1:
            s = (s1 / r1) * r
        elif r1 < r <= r2:
            s = ((s2 - s1) / (r2 - r1)) * (r - r1) + s1
        elif r2 < r < 255:
            s = ((255 - s2) / (255 - r2)) * (r - r2) + s2

        out_pix[i, j] = int(s)

out.save("linear_stretch.png")