import qrcode
import random

x = input("> ")
y = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
if random.randint(1, 100) == 1:
  img = qrcode.make(y)
else:
  img = qrcode.make(x)

type(img)  # qrcode.image.pil.PilImage

img.save(f"{x}.png")
