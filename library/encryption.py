#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this library!
# Plugin: Encryption
#|==============================================================|#

#IMPORT
import hashlib
#SHA1
def eptnSha1(string):
	hasht = hashlib.sha1()
	hasht.update(string.encode("utf-8"))
	output = hasht.hexdigest()
	return output
#SHA256
def eptnSha256(string):
	hasht = hashlib.sha256()
	hasht.update(string.encode("utf-8"))
	output = hasht.hexdigest()
	return output
#MD5
def eptnMd5(string):
	hasht = hashlib.md5()
	hasht.update(string.encode("utf-8"))
	output = hasht.hexdigest()
	return output