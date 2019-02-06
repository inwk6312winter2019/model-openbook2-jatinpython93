def tuple_required(file_name):
	fin = open(file_name,'r')
	for line in fin:
		line = line.split(",")
		tup = (line[2],line[4],line[6],line[7])
		print(tup)

tuple_required('Street_Centrelines.csv')

