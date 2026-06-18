from PIL import Image
import math

img = Image.open("../input.png").convert("L")
w, h = img.size
pix = img.load()

gx_kernel = [
[-1,0,1],
[-2,0,2],
[-1,0,1]
]

gy_kernel = [
[-1,-2,-1],
[0,0,0],
[1,2,1]
]

out = Image.new("L",(w,h))
out_pix = out.load()

for x in range(1,w-1):
    for y in range(1,h-1):

        gx = 0
        gy = 0

        for i in range(3):
            for j in range(3):
                val = pix[x+i-1, y+j-1]
                gx += val * gx_kernel[i][j]
                gy += val * gy_kernel[i][j]

        g = int(math.sqrt(gx*gx + gy*gy))
        g = max(0, min(255, g))

        out_pix[x,y] = g

out.save("sobel.png")
