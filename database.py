#F220759


def Open_file(name):# returns a 2d array of each record and their elements
    n=[]# a temp variable used to store data
    f = open(name, "r")# opens the file in read mode
    for x in f:# iterates through list creating a 2d array of all data in it
        temp = x.split(";")
        n.append(temp)
    f.close()# closes file
    return(n)


def add_record(action,member_id,book_id,date ):
    record = action+";"+str(member_id)+";"+str(book_id)+";"+str(date) # creates new record with correct format
    f = open("Logfile.txt", "a")#opens file in append mode
    f.write("\n")# makes it so it writes on a new line
    f.write(record)#adds record to file

##Test cases
#add_record("Return","1009","20","23/10/22")
#print(Open_file("Logfile.txt"))

#books = Open_file("Book_Info.txt")
#print(books)
#num_books = books[len(books)-1][0]
#print(num_books)