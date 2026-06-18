from PIL import Image

img = Image.open("input_color.png").convert("RGB")

w, h = img.size
pix = img.load()

out = Image.new("L", (w, h))
out_pix = out.load()

for i in range(w):
    for j in range(h):
        r, g, b = pix[i, j]

        gray = int(.299 * r + .587 * g + .114 * b)

        out_pix[i, j] = gray
out.save("input.png")