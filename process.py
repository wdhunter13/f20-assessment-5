log_file = open("um-server-01.txt") #opens the file and returns the file object 


def sales_reports(log_file):  # Creates a function
    for line in log_file:   # Says for every line in the um-server-01.txt 
        line = line.rstrip()  # Takes away any whitespaces at the end of the line
        day = line[0:3]  # Setting a variable equal to a line with the index being 3
        if day == "Mon":  # If the variable matches the string "Tue"
            print(line)  # Prints the line


sales_reports(log_file) #Console logs all the lines that meet the criteria above



