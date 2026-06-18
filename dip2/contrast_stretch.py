from PIL import Image

img = Image.open("../input.png").convert("L")
w, h = img.size
pix = img.load()

r_min, r_max = img.getextrema()

out = Image.new("L", (w, h))
out_pix = out.load()

for i in range(w):
    for j in range(h):
        s = ((pix[i, j] - r_min) / (r_max - r_min)) * 255
        out_pix[i, j] = int(s)

out.save("contrast_stretch.png")
