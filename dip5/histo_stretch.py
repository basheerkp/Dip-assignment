from PIL import Image

img = Image.open("../input.png").convert("L")
w, h = img.size
pix = img.load()

out = Image.new("L", (w, h))
out_pix = out.load()

for i in range(w):
    for j in range(h):
        r = pix[i, j]
        s = ((r - 45) / (165 - 45)) * 255

        out_pix[i,j] = int(s)

out.save("histo_stretch.png")