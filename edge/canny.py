from PIL import Image
import math

img = Image.open("../../../Downloads/BROWSER/dembouz.jpeg").convert("L")
w, h = img.size
pix = img.load()

# Gaussian 5×5
gauss = [
    [1, 4, 6, 4, 1],
    [4, 16, 24, 16, 4],
    [6, 24, 36, 24, 6],
    [4, 16, 24, 16, 4],
    [1, 4, 6, 4, 1]
]

blur = [[0] * w for _ in range(h)]

for y in range(2, h - 2):
    for x in range(2, w - 2):
        s = 0
        for j in range(5):
            for i in range(5):
                s += pix[x + i - 2, y + j - 2] * gauss[j][i]
        blur[y][x] = s // 256

# Sobel gradients
gx_k = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
gy_k = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]

mag = [[0] * w for _ in range(h)]
angle = [[0] * w for _ in range(h)]

for y in range(1, h - 1):
    for x in range(1, w - 1):
        gx = gy = 0
        for j in range(3):
            for i in range(3):
                val = blur[y + j - 1][x + i - 1]
                gx += val * gx_k[j][i]
                gy += val * gy_k[j][i]

        mag[y][x] = math.sqrt(gx * gx + gy * gy)
        angle[y][x] = math.atan2(gy, gx)

# Non-maximum suppression
nms = [[0] * w for _ in range(h)]

for y in range(1, h - 1):
    for x in range(1, w - 1):
        a = angle[y][x] * 180 / math.pi
        if a < 0: a += 180

        q = r = 0
        if (0 <= a < 22.5) or (157.5 <= a <= 180):
            q = mag[y][x + 1]
            r = mag[y][x - 1]
        elif (22.5 <= a < 67.5):
            q = mag[y + 1][x - 1]
            r = mag[y - 1][x + 1]
        elif (67.5 <= a < 112.5):
            q = mag[y + 1][x]
            r = mag[y - 1][x]
        else:
            q = mag[y - 1][x - 1]
            r = mag[y + 1][x + 1]

        if mag[y][x] >= q and mag[y][x] >= r:
            nms[y][x] = mag[y][x]

# Double threshold
high = 50
low = 10

edges = Image.new("L", (w, h))
e = edges.load()

for y in range(h):
    for x in range(w):
        if nms[y][x] >= high:
            e[x, y] = 255
        elif nms[y][x] >= low:
            e[x, y] = 100
        else:
            e[x, y] = 0

edges.show()
