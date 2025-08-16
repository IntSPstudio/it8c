#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this library!
# Plugin: Data handling
#|==============================================================|#

#|COM|==========================================================|#
#MAKE INPUT TO ONLY LETTRS AND DIGITS
def cfc1219294(input,alt):
	return str(alt).join(i for i in input if i.isalnum())
#CHECK IF IT IS A NUMBER
def cfc318398(input):
    try:
        int(input)
        return 1
    except ValueError:
        return 0
#|1D ARRAY|=====================================================|#
#MAKE 1D ARRAY
def cad325305(array_size,array_content):
	return [array_content for xp in range(array_size)]
#MAKE 1D ARRAY TO 2D ARRAY
def cad1325478(array1_content,array2_def_content,array2_width):
	array1_width =  len(array1_content)
	array2_height =0
	xp =0
	for i in range(0, array1_width):
		xp +=1
		if xp >= array2_width:
			array2_height +=1
			xp =0
	array2_content = cbd325306(array2_height,array2_width,array2_def_content)
	xp =0
	yp =0
	for i in range(0, array1_width):
		if xp == array2_width:
			xp =0
			yp +=1
		array2_content[yp][xp] = array1_content[i]
		xp +=1
	return array2_content
#PRINT 1D ARRAY 
def cad1620472(array_content,separator):
	array_width = len(array_content)
	array_output =""
	for i in range(0, array_width):
		point = str(array_content[i])
		if array_output !="":
			array_output = array_output + separator + point
		else:
			array_output = point
	return array_output
#CALCULATE AVARAGE VALUE
def cad320542(array_content):
	array_width = len(array_content)
	array_output =0
	array_counter =0
	for i in range(0, array_width):
		point = array_content[i]
		check = cfc318398(point)
		if check == 1:
			array_counter = array_counter +1
			array_output = array_output + int(point)
	if array_counter > 0:
		return array_output / array_counter
	else:
		return 0
#CALCULATE SUM VALUE
def cad320479(array_content):
	array_width = len(array_content)
	array_output =0
	for i in range(0, array_width):
		point = array_content[i]
		check = cfc318398(point)
		if check == 1:
			array_output = array_output + int(point)
	return array_output
#CHECK MAX VALUE
def cad320776(array_content):
	array_width = len(array_content)
	array_output =0
	for i in range(0, array_width):
		point = array_content[i]
		check = cfc318398(point)
		if check == 1:
			point = int(point)
			if point > array_output:
				array_output = point
	return array_output
#CHECK 1D ARRAY OBJECTS
def cad319492(array1_content):
	array1_content = sorted(array1_content)
	array1_width = len(array1_content)
	point1 =""
	for i in range(0,2):
		if i == 1:
			check_height = ypb
			check_width =3
			check_content = cbd325306(check_height,check_width,"")
		ypb =0
		for ypa in range(0, array1_width):
			point2 = str(array1_content[ypa])
			if point2 !="":
				if point2 != point1:
					if i == 1:
						check_content[ypb][0] = str(ypb +1)
						check_content[ypb][2] = point2
					ypb +=1
				point1 = point2
	for ypa in range(0,check_height):
		check1 =0
		point1 = str(check_content[ypa][2])
		for ypb in range(0,array1_width):
			point2 = str(array1_content[ypb])
			if point1 == point2:
				check1 +=1
		check_content[ypa][1] = str(check1)
	return check_content
#CONTENT FORMAT
def cad320737(array_content,array_mode):
	array_width = len(array_content)
	for yp in range(0, array_width):
		point1 = str(array_content[yp])
		if array_mode == 1:
			point2 = str.lower(point1)
		elif array_mode == 2:
			point2 = str.upper(point1)
		elif array_mode == 3:
			point2 = cfc1219294(point1,"") 
		elif array_mode == 4:
			check = cfc318398(point1)
			if check == 1:
				point2 = int(point1)
			else:
				point2 =0
		array_content[yp] = point2
	return array_content
#FLIP OBJECTS
def cad619467(array1_content):
	array1_length = len(array1_content)
	array2_content = cad325305(array1_length,"")
	for ypa in range(0,array1_length):
		ypb = array1_length -ypa -1
		array2_content[ypa] = array1_content[ypb]
	return array2_content
#|2D ARRAY|=====================================================|#
#MAKE 2D ARRAY
def cbd325306(array_height,array_width,array_content):
	return [[array_content for xp in range(array_width)] for yp in range(array_height)]
#MAKE 2D ARRAY TO 1D ARRAY
def cbd1325477(array1_content):
	array1_height = len(array1_content)
	array1_width =  len(array1_content[0])
	array1_counter =0
	array2_width = array1_height * array1_width
	array2_content = cad325305(array2_width,"")
	for yp in range(0, array1_height):
		for xp in range(0, array1_width):
			array2_content[array1_counter] = array1_content[yp][xp]
			array1_counter +=1
	return array2_content
#PRINT 2D ARRAY
def cbd1620473(array_content,separator):
	array_height = len(array_content)
	array_width = len(array_content[0])
	array_content =""
	array_separatorv ="\n"
	for yp in range(0, array_height):
		for xp in range(0, array_width):
			point = str(array_content[yp][xp])
			if point !="":
				if xp == 0:
					array_content = array_content + point
				else:
					array_content = array_content + separator + point
		if yp < array_height -1:
			array_content = array_content + array_separatorv
	return array_content
#SMART PRINT 2D ARRAY
def cbd1920575(array1_content,separator,fill,content_mode):
	array1_height = len(array1_content)
	array1_width = len(array1_content[0])
	array_rowsp_width = cad325305(array1_width,"")
	array2_height = array1_height
	array2_width = array1_width
	array2_content = cbd325306(array2_height,array2_width,"")
	for xp in range(0,array1_width):
		content1 = cbd514472(array1_content,xp)
		content1_length = len(content1)
		check1 =0
		for yp in range(0,content1_length):
			check2 = len(str(content1[yp]))
			if check2 > check1:
				check1 = check2
		array_rowsp_width[xp] = check1
	for yp in range(0,array1_height):
		for xp in range(0,array1_width):
			point1 = str(array1_content[yp][xp])
			check1 = len(point1)
			check2 = array_rowsp_width[xp] - check1
			check3 = cfc318398(point1)
			if check2 > 0:
				point2 =""
				for _ in range(0, check2):
					if content_mode == 1:
						point2 = point2 + fill
					else:
						point2 = point2 + " "
				if check3 == 0:
					point3 = point1 + point2
				else:
					point3 = point2 + point1
			else:
				point3 = point1
			array2_content[yp][xp] = point3
	return cbd1620473(array2_content,separator)
#CALCULATE AVARAGE VALUE
def cbd320543(array_content):
	return cad320542(cbd1325477(array_content))
#CALCULATE SUM VALUE
def cbd320480(array_content):
	return cad320479(cbd1325477(array_content))
#CHECK MAX VALUE
def cbd320777(array_content):
	return cad320776(cbd1325477(array_content))
#CHECK 2D ARRAY OBJECTS
def cbd319493(array_content):
	return cad319492(cbd1325477(array_content))
#CONTENT FORMAT
def cbd320738(array1_content,array_mode):
	return cad1325478(cad320737(cbd1325477(array1_content),array_mode),"",len(array1_content[0]))
#EXTRACT ARRAY COLUMN
def cbd514472(array1_content,pos):
	array1_height = len(array1_content)
	array1_width = len(array1_content[0])
	array2_content = cad325305(array1_height,"")
	if pos < array1_width:
		for yp in range(0, array1_height):
			array2_content[yp] = array1_content[yp][pos]
	return array2_content
#ADD COLUMN TO ARRAY
def cdb114391(array1_content, array2_content):
	array1_height = len(array1_content)
	array1_width = len(array1_content[0])
	array2Length = len(array2_content)
	array3_height = array1_height
	array3_width = array1_width +1
	if array2Length > array1_height:
		array3_height = array2Length
	array3_content = cbd325306(array3_height, array3_width, "")
	for y in range(0, array1_height):
		for x in range(0, array1_width):
			array3_content[y][x] = array1_content[y][x]
	for i in range(0, array2Length):
		array3_content[i][array3_width -1] = array2_content[i]
	return array3_content
#ADD NEW ROW
def cbd125319(array1_content,array3_content):
	array1_height = len(array1_content)
	array1_width = len(array1_content[0])
	array2_height = array1_height +1
	array2_width = array1_width
	array3_width = len(array3_content)
	if array3_width > array2_width:
		check1 = array3_width
	else:
		check1 = array2_width
	array2_content = cbd325306(array2_height,check1,"")
	for yp in range(0,array1_height):
		for xp in range(0,array1_width):
			point1 = str(array1_content[yp][xp])
			array2_content[yp][xp] = point1
	yp = array1_height
	for xp in range(0,array3_width):
		array2_content[yp][xp] = str(array3_content[xp])
	return array2_content
#FLIP OBJECTS
def cbd619468(array1_content):
	array1_height = len(array1_content)
	array1_width = len(array1_content[0])
	array2_height = array1_height
	array2_width = array1_width
	array2_content = cbd325306(array2_height,array2_width,"")
	ypb = array2_height
	for ypa in range(0,array1_height):
		ypb -=1
		for xp in range(0,array1_width):
			point1 = str(array1_content[ypa][xp])
			array2_content[ypb][xp] = point1
	return array2_content
#REMOVE TITLE
def cbd75347(array1_content):
	array1_height = len(array1_content)
	array1_width = len(array1_content[0])
	array2_content = cbd325306(array1_height -1,array1_width,"")
	for y in range(1, array1_height):
		array2_content[y-1] = array1_content[y]
	return array2_content