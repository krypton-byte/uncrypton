from sys import stdout
from uncompyle6.main import decompile
import marshal
class Decoder:
	def __init__(self,versi,kunci):
		self.versi = versi
		self.kunci = kunci
def uncrypton(version,bytecode):
	try:
		biar=Decoder(version,bytecode)
		bytecodex=marshal.loads(biar.kunci)
		decompile(biar.versi, bytecodex, stdout)
	except (TypeError,ValueError):
		print('bytecode error')

usage='usage: uncrypton(version,bytecode)'
usage="ex   : uncrypton(2.7,'c\x62\x62\x82')"
