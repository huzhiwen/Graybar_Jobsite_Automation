#This code is to generate QR codes for future implementation of scanning technology. This is not used in the first iteration of the project
import pyqrcode
import qrtools


qr = pyqrcode.create("LED Light \n Phillips \n 220 \n 25 \n 200")
print qr.terminal(quiet_zone=1)


qr.png("products.png", scale=6) 
qr = qrtools.QR()
qr.decode("products.png")
print qr.data 

