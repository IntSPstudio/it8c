#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this library!
# Plugin: Encryption
#|==============================================================|#

#IMPORT
import hashlib
#SHA256
def sha1Encryption(string):
	hasht = hashlib.sha256()
	hasht.update(string.encode("utf-8"))
	output = hasht.hexdigest()
	return output
#SHA1
def sha1Encryption(string):
	hasht = hashlib.sha1()
	hasht.update(string.encode("utf-8"))
	output = hasht.hexdigest()
	return output
#MD5
def sha1Encryption(string):
	hasht = hashlib.md5()
	hasht.update(string.encode("utf-8"))
	output = hasht.hexdigest()
	return output