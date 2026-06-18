from PIL import Image

img = Image.open("../input.png").convert("L")
w, h = img.size
pix = img.load()

out = Image.new("L",(w,h))
out_pix = out.load()

for x in range(1,w-1):
    for y in range(1,h-1):
        window = []

        for i in range(-1,2):
            for j in range(-1,2):
                window.append(pix[x+i,y+j])

        out_pix[x,y] = min(window)

out.save("min_filtered.png")