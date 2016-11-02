#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this library!
# Plugin: Encryption
#|==============================================================|#

#IMPORT
import hashlib
#SHA ENCRYPTION
def sha1Encryption(string):
	hasht = hashlib.sha1()
	hasht.update(string.encode("utf-8"))
	output = hasht.hexdigest()
	return output