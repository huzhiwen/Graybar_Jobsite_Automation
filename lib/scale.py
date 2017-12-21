import pyqrcode
import qrtools


class Scale(object):
	def __init__(self, barcode, product):
		self.barcode = barcode
		self.product = product

class Product(object):	
	def __init__(self, name, manufacturer,quantity, min, max):
		self.name = name
		self.manufacturer = manufacturer
		self.quantity = quantity
		self.min = min
		self.max = max

qr = qrtools.QR()
qr.decode("products.png")
text = qr.data.split('\n')
scale = Scale('abc',Product(text[0].strip(),  text[1].strip(), int(text[2].strip()), int(text[3].strip()), int(text[4].strip())))


print scale.product.name 
print scale.product.manufacturer, scale.product.quantity, scale.product.min, scale.product.max 


#text = pyqrcode.create(scale.barcode)
#print(text.terminal(quiet_zone=1))