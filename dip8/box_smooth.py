from PIL import Image

img = Image.open("../input.png").convert("L")
w, h = img.size
pix = img.load()

kernel = [
    [1/9,1/9,1/9],
    [1/9,1/9,1/9],
    [1/9,1/9,1/9]
]

out = Image.new("L",(w,h))
out_pix = out.load()

for x in range(1,w-1):
    for y in range(1,h-1):
        s = 0
        for i in range(3):
            for j in range(3):
                s += pix[x+i-1,y+j-1]*kernel[i][j]

        out_pix[x,y] = int(s)

out.save("box_smooth.png")