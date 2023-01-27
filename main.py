import wifi_qrcode_generator as qr
 
qrCode = qr.wifi_qrcode('O nosso WIFI', False, 'WPA', 'Password_do_wifi')

qrCode.show()
qrCode.save("meu_wifi_qr.png")
