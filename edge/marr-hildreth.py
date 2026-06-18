from PIL import Image

image = Image.open("../../../Downloads/BROWSER/dembouz.jpeg").convert("L")
w, h = image.size
pix = image.load()

# Gaussian kernel (5x5)
gauss = [
    [1, 4, 6, 4, 1],
    [4, 16, 24, 16, 4],
    [6, 24, 36, 24, 6],
    [4, 16, 24, 16, 4],
    [1, 4, 6, 4, 1]
]

# normalize factor
g_sum = 256

# Laplacian kernel
lap = [
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
]

# Gaussian smoothing
blur = [[0] * w for _ in range(h)]

for y in range(2, h - 2):
    for x in range(2, w - 2):
        s = 0
        for j in range(5):
            for i in range(5):
                s += pix[x + i - 2, y + j - 2] * gauss[j][i]
        blur[y][x] = s // g_sum

# Laplacian
lap_img = [[0] * w for _ in range(h)]

for y in range(1, h - 1):
    for x in range(1, w - 1):
        s = 0
        for j in range(3):
            for i in range(3):
                s += blur[y + j - 1][x + i - 1] * lap[j][i]
        lap_img[y][x] = s

# Zero crossing edge detection
edges = Image.new("L", (w, h))
e = edges.load()

for y in range(1, h - 1):
    for x in range(1, w - 1):
        center = lap_img[y][x]
        neighbors = [
            lap_img[y - 1][x], lap_img[y + 1][x],
            lap_img[y][x - 1], lap_img[y][x + 1]
        ]
        if any(center * n < 0 for n in neighbors):
            e[x, y] = 255
        else:
            e[x, y] = 0

edges.show()
