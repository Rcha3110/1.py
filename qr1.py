import qrcode
features=qrcode.QRCode(version=1, box_size=40, border=3)
features.make(fit=True)

generate_img=features.make_image(fill_color="blue", back_color="white")
generate_img.save('img3.png')
