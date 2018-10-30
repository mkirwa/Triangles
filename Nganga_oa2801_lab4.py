# File: oa2801_lab4.py
# Name: NGANGA
# Email: martin.nganga@nps.edu
#
# OA2801 - Lab 4 (Military Spending)
# import statements first
import sys
# function definitions next
def process_file(infile,start_year, end_year):
    print("Reading file %s to process data in range [%d,%d]" % (infile, start_year, end_year))
    target = open("inflile", "r")    # open the target file in read mode
    my_list = []                         # create an empty list
    for line in target:                  # run a loop over each line of the target file
        line = line.strip()              # this strips any leading/lagging whitespace and any special characters
        line = line.replace('"','')
        line = line.replace('-9', '0')                                   #line = line.replace('-9','')# # remove the extra quotes around country names
        my_list.append(line.split(','))  # this splits the line into a list and appends that list to the my_data list
    years = []
    yearsvalues = []
    milex =[]
    steel = []
    cinc = []
    total_milex =[]
    total_steel =[]
    max_cinc = []
    ##this should loop through the entire document 
    for i in range(len(my_list)-1):
        if my_list[i+1][2]>= 'start_year' and my_list[i+1][2]<='end_year':
            years.append (int(my_list[i+1][2]))
            milex.append((my_list[i+1][2], my_list[i+1][4]))
            steel.append((my_list[i+1][2], my_list[i+1][3]))
            cinc.append ((my_list[i+1][0], my_list[i+1][2], float(my_list[i+1][9])))
         ##This code should be under the the for loop above as it picks up the necessary rows   
        for k in range(len(years)):
            if int(years[k]) not in yearsvalues:
                yearsvalues.append(years[k])         
            for k in range(len(yearsvalues)):
                mil_year = []
                for j in range(len(milex)):
                    if yearsvalues[k] == int(milex[j][0]):
                        mil_year.append((int(milex[j][1])))
                #print(sum(mil_year))
                total_milex.append(sum(mil_year))         
            for k in range(len(yearsvalues)):
                steel_year = []
                for j in range(len(steel)):
                    if yearsvalues[k] == int(steel[j][0]):
                        steel_year.append((int(steel[j][1])))
                #print(sum(steel_year))
                total_steel.append(sum(steel_year))
            
            
            for k in range(len(yearsvalues)):
                cinc_year = []
                for j in range(len(cinc)):
                    if yearsvalues[k] == int(cinc[j][1]):
                        cinc_year.append((float(cinc[j][2]), cinc[j][0]))
                #print(sum(mil_year))
                max_cinc.append(max(cinc_year)) 
           
    return (yearsvalues, total_milex, total_steel, max_cinc)  


    target.close() 
    

    #######################
    # YOUR CODE GOES HERE #
    #######################
    
# end of process_file()

#
# the main part of the script comes last
#
if __name__ == '__main__':

    # Here we assume that there are exactly three additional arguments...
    if len(sys.argv) != 4:
        sys.stderr.write("\tUsage: this script requires three command line arguments.\n")
        sys.stderr.write("\t arg1: name of csv file with data \n")
        sys.stderr.write("\t arg2: start year \n")
        sys.stderr.write("\t arg3: end year \n")
        sys.stderr.write("\tAborting.\n")
        sys.exit() # exit the program immediately

    #print 'The first argument is always the name of the script'
    #print 'argv[0] = %s' % sys.argv[0]

    infile = sys.argv[1]
    start_year = int(sys.argv[2])
    end_year = int(sys.argv[3])

    process_file(infile, start_year, end_year)

    print("End of script.")
