from PIL import Image

img = Image.open("../input.png").convert("L")
w, h = img.size
pix = img.load()

# histogram
hist = [0] * 256
for i in range(w):
    for j in range(h):
        hist[pix[i, j]] += 1

# cumulative distribution function
cdf = [0] * 256
cdf[0] = hist[0]
for i in range(1, 256):
    cdf[i] = cdf[i-1] + hist[i]

# normalize CDF
total = w * h
cdf_min = next(v for v in cdf if v > 0)

mapping = [0] * 256
for i in range(256):
    mapping[i] = int((cdf[i] - cdf_min) / (total - cdf_min) * 255)

# apply mapping
out = Image.new("L", (w, h))
out_pix = out.load()

for i in range(w):
    for j in range(h):
        r = pix[i, j]
        out_pix[i, j] = mapping[r]

out.save("histo_equalized.png")