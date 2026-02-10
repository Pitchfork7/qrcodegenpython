import qrcode

x = input("> ")
x = x.replace(":", "_").replace("/", "_").replace("?", "_").replace("=", "_").replace("&", "_")

img = qrcode.make(x)

type(img)  # qrcode.image.pil.PilImage

img.save(f"{x}.png")
