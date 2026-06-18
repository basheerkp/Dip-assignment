from PIL import Image
import math

img = Image.open("../input.png").convert("L")
w, h = img.size
pix = img.load()

choice = int(input("1: Ideal HPF  2: Gaussian HPF  3: Butterworth HPF : "))

while choice not in [1, 2, 3]:
    choice = int(input(
        "your choice was not in the range of 1,2,3 \nchoose again 1: Ideal HPF  2: Gaussian HPF  3: Butterworth HPF : "))

D0 = float(input("Cutoff radius (e.g. 2): "))
n = 2
if choice == 3:
    n = int(input("Butterworth order n: "))

out = Image.new("L", (w, h))
out_pix = out.load()

for x in range(1, w - 1):
    for y in range(1, h - 1):

        val = 0
        weight_sum = 0

        for i in range(-1, 2):
            for j in range(-1, 2):

                D = math.sqrt(i * i + j * j)

                if choice == 1:  # Ideal
                    H = 0 if D <= D0 else 1

                elif choice == 2:  # Gaussian
                    H = 1 - math.exp(-(D * D) / (2 * (D0 * D0)))

                else:  # Butterworth
                    if D == 0:
                        H = 0
                    else:
                        H = 1 / (1 + (D0 / D) ** (2 * n))

                val += pix[x + i, y + j] * H
                weight_sum += H

        if weight_sum != 0:
            val /= weight_sum

        out_pix[x, y] = max(0, min(255, int(val)))
if choice == 1:
    name = "Ideal"
elif choice == 2:
    name = "Gaussian"
else:
    name = "Butterworth"
out.save(name + ".png")
