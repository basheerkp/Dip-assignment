import numpy as np
from PIL import Image

# ideal,gaussian,butterworth

img = Image.open("../input.png").convert("L")
f = np.array(img)

F = np.fft.fftshift(np.fft.fft2(f))

rows, cols = f.shape
crow, ccol = rows // 2, cols // 2

D0 = 50
n = 2

H_ideal = np.zeros((rows, cols))
H_gauss = np.zeros((rows, cols))
H_butter = np.zeros((rows, cols))

for u in range(rows):
    for v in range(cols):

        D = ((u - crow) ** 2 + (v - ccol) ** 2) ** 0.5

        if D <= D0:
            H_ideal[u, v] = 1

        H_gauss[u, v] = np.exp(-(D ** 2) / (2 * (D0 ** 2)))

        H_butter[u, v] = 1 / (1 + (D / D0) ** (2 * n))

# Apply filters
G_ideal = F * H_ideal
G_gauss = F * H_gauss
G_butter = F * H_butter

# Inverse transform
ideal_img = np.abs(np.fft.ifft2(np.fft.ifftshift(G_ideal)))
gauss_img = np.abs(np.fft.ifft2(np.fft.ifftshift(G_gauss)))
butter_img = np.abs(np.fft.ifft2(np.fft.ifftshift(G_butter)))

Image.fromarray(ideal_img.astype(np.uint8)).save("ideal.png")
Image.fromarray(gauss_img.astype(np.uint8)).save("gaussian.png")
Image.fromarray(butter_img.astype(np.uint8)).save("butterworth.png")
