import qrcode

x = input("> ")

img = qrcode.make(x)

type(img)  # qrcode.image.pil.PilImage

img.save(f"{x}.png")
