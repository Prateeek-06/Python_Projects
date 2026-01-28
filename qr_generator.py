import qrcode

data = input("Enter text or URL: ")
img = qrcode.make(data)
img.save("user_qrcode.png")

print("QR code saved as user_qrcode.png")
