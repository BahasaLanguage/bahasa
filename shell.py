import bahasa

print(
'''
 ,ggggggggggg,                                                           
dP"""88""""""Y8,             ,dPYb,                                      
Yb,  88      `8b             IP'`Yb                                      
 `"  88      ,8P             I8  8I                                      
     88aaaad8P"              I8  8'                                      
     88""""Y8ba    ,gggg,gg  I8 dPgg,     ,gggg,gg    ,g,       ,gggg,gg 
     88       `8b dP"  "Y8I  I8dP" "8I   dP"  "Y8I   ,8'8,     dP"  "Y8I 
     88        88i8'    ,8I  I8P    I8  i8'    ,8I  ,8'  Yb   i8'    ,8I 
     88_______,d0d8,   ,d8b,,d8     I8,,d8,   ,d8b,,8'_   8) ,d8,   ,d8b,
    8888888888P" "Y8888P"`Y888P     `Y8P"Y8888P"`Y8P' "YY8P8PP"Y8888P"`Y8


Bahasa, An Indonesian Programming Language
Copyright(c) 2020 by Jeremy Gautama
Homepage: https://bahasalanguage.github.io/
Github	: https://github.com/bahasalanguage

help		type 'help' for help
bantuan		ketik 'bantuan' untuk bantuan
'''
)

while True:
	text = input('bahasa > ')
	if text.strip() == "": continue
	result, error = bahasa.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))