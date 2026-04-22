import qrcode 

img = qrcode.make ("https://www.youtube.com/channel/UCWv7vMbMWH4-V0ZXdmDpPBA")

type (img)
img.save ("youtube_qr_code.png")

