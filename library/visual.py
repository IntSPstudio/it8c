#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this library!
# Plugin: Visual
#|==============================================================|#

#WHAT
def comTerminalDunno(stpoint):
	stmark =""
	if stpoint > 0:
		for i in range(stpoint):
			stmark = stmark +" "
	a = stmark +"######            "
	b = stmark +"#    #            "
	c = stmark +"#    #      ######"
	d = stmark +"#    #      #    #"
	e = stmark +"#    #  ##  #    #"
	f = stmark +"######  ##  ######"
	return "\n"+ a +"\n"+ b +"\n"+ c +"\n"+ d +"\n"+ e +"\n"+ f +"\n"
#TERMINAL LINE
def comTerminalBackgroundLine(width,mark):
	if width > 0:
		line =""
		for i in range(width):
			line = line + mark
	else:
		line = "----------------------------------------------------------------"
	return line