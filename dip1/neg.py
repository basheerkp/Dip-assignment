from PIL import Image

image = Image.open("../input.png").convert("L")

w, h = image.size
pix = image.load()

out = Image.new("L", (w, h))
out_pix = out.load()

for i in range(h):
    for j in range(w):
        r = pix[j, i]
        out_pix[j, i] = 255 - r

out.save("neg.png")
print("negative done")
