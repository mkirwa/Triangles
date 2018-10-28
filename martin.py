##I tried being detailed with my pseudocode as much as I could
##I haven't tested this code and there's bound to be errors
##it's just a pseudocode so you might wanna scratch your brain kidogo tu
##the method takes input_filename start year and end year..
def process(input_filename,start_year, end_year){
	target = open("input_filename","r")
	my_List = []
	for line in target:
	line = line.strip()
	line = line.replace("",'')
	my_List.append(line.split(','))

	##declaring the lists to hold the years, totals for
	##the military expenditure
	##totals for iron and steel production
	##maximum CINC and the country associated with it

	years = []
	mil_expend = []
	steel = []
	maximal_CINC = []
	country_CINC = []

	##looping through the given start and end year

	for i in range (len(my_List)):
		if my_List[i][2]>=start_year and my_List[i][2]<=end_year:
			years.append(line.split(','))

			##make sure the indentation looks something like this because python
			##is very keen on indentation

			##Getting the rows for military expenditure and storing it in expenditure
			##it's a for loop inside a for loop so you have to use
			##j instead of i
			expenditure = [j[4] for j in myList]
			##Getting the total for expenditure and storing it in mil_expend
			mil_expend = [sum(k) for k in expenditure]
			mil_expend.append(line.split(','))

			##getting the rows iron and steel production and storing it in steelProd
			steelProd = [j[3] for j in myList]
			##Getting the total for iron and steel and storing it in steel
			steel = [sum(k) for k in steelProd]
			steel.append(line.split(','))

			##getting the rows for maximum CINC and storing the rows in max_CINC
			max_CINC = [j[9] for j in myList]
			##Getting the maximum CINC
			maximal_CINC = max(max_CINC)
			maximal_CINC.append(line.split(','))
			##appends the country with the maximum CINC
			country_CINC.append(max(max_CINC))

	##Can you generate a separate CSV file for these data? if you cannot, let me know so we can see what to do about it

}