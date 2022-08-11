from PIL import Image

image= Image.open('Animation/testing_pallet.png')
width, height = image.size

pixels_raw = image.load()
pixels = []

for w in range(width):
    pixels.append([])
    for h in range(height):
        pixels[w].append(pixels_raw[w,h])

print(pixels)
