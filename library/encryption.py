#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this library!
# Plugin: Encryption
#|==============================================================|#

#IMPORT
import hashlib
#SHA1
def cpd51249(string):
	hasht = hashlib.sha1()
	hasht.update(string.encode("utf-8"))
	output = hasht.hexdigest()
	return output
#SHA256
def cpd56292(string):
	hasht = hashlib.sha256()
	hasht.update(string.encode("utf-8"))
	output = hasht.hexdigest()
	return output
#MD5
def cpd55232(string):
	hasht = hashlib.md5()
	hasht.update(string.encode("utf-8"))
	output = hasht.hexdigest()
	return output