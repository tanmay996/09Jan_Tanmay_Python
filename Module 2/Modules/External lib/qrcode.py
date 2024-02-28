import pyqrcode
qr = pyqrcode.create("https://careercenter.tops-int.com/")
qr.png("tops.png",scale=7)
