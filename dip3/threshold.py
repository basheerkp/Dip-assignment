from PIL import Image

img = Image.open("../input.png").convert("L")
w, h = img.size
pix = img.load()

out = Image.new("L", (w, h))
out_pix = out.load()

lim = 128

for i in range(w):
    for j in range(h):
        s = 0 if pix[i, j] < lim else 255
        out_pix[i, j] = s

out.save("threshold.png")