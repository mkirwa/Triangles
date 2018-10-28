
def process(input_filename,start_year, end_year){
	
	target = open("input_filename","r")
	my_List = []

	for line in target:

	line = line.strip()
	line = line.replace("",'')
	my_List.append(line.split(','))

	years = []
	mil_expend = []
	steel = []
	maximal_CINC = []
	country_CINC = []

	##looping through the given years and 
	for i in range (len(my_List)):
		if my_List[i][2]>=start_year and my_List[i][2]<=end_year:
			years.append(line.split(','))

			##make sure the indentation looks like this because python
			##is very keen on indentation
			##Getting the rows for military expenditure
			##it's a for loop inside a for loop so you have to use
			##j instead of i

			expenditure = [j[4] for j in myList]
			##Getting the total for expenditure
			mil_expend = [sum(k) for k in expenditure]
			mil_expend.append(line.split(','))

			##getting the rows iron and steel production
			steelProd = [j[3] for j in myList]
			##Getting the total for iron and steel
			steel = [sum(k) for k in steelProd]
			steel.append(line.split(','))

			##getting the rows for maximum CINC
			max_CINC = [j[9] for j in myList]
			##Getting the  for iron and steel
			maximal_CINC = max(max_CINC)
			maximal_CINC.append(line.split(','))
			##appends the country with the maximum CINC
			country_CINC.append(max(max_CINC))

	##Can you generate a separte CSV file?? for these data?

}