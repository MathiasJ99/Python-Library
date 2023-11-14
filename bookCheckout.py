#F220759

from database import *
import datetime


def get_entry(txt):# gets user input for entry boxes
    # for text boxes .get() needs start and stop characters of the string to get
    entry = str(txt.get("1.0","end")).strip()#formats input to get just input

    return entry

def get_date():# a function to get current date

    temp = str(datetime.date.today()) # get current date but uses -
    year = temp[2:4] # gets the year
    month = temp[5:7]# gets month
    day = temp[8:11] # gets day

    date = day + "/" + month + "/" + year # creates date in correct format
    return(date)# returns  date in correct format



def get_book_state(book_id):
    records = Open_file("Logfile.txt")# gets a 2d array of all data in logfile
    #print("Loan-Return-Reserve; Member_id; Book_id; CheckoutDate-ReturnDate; " -- format of records in the Logfile
    query = [] #



    for i in range(0,len(records)):# iterates through all records

        if str(book_id) == str(records[i][2]):
            query.append(records[i])# this gets all records of a book using their book id
            # and adds it to query array

    books = Open_file("Book_Info.txt")
    num_books = books[len(books)-1][0] ## this gets the highest book_id
    ## used to find if book id entered by user is in the database

    f = len(query) -1 # gets index of most recent record
    if  int(book_id) <=int(num_books):#make sure it is in range of book ids
        if f ==-1: # if it hasnt been checked out yet
            return "Available" # if the book isnt in the log files it hasnt been loaned out so its available
        else:
            state = query[f][0] # finds the first element of the record which will be Return or Reserve or Loan
            #print(query[f][0])# test case
            if state == "Return":
                return "Available"

            if state == "Loan":
                return "Out on loan"

            if state == "Reserve":
                return "Reserved"

    else:
        return "Not in library"

def get_member_id(book_id):#gets the member id of the most recent action to the book
    records = Open_file("Logfile.txt")
    # print("Loan-Return-Reserve; Member_id; Book_id; CheckoutDate-ReturnDate; ") the format of records in the Logfile
    query = []

    # print(records)

    for i in range(0, len(records)):## gets all records where the book id is involved
        # print(records[i][2])
        if str(book_id) == str(records[i][2]):
            query.append(records[i])  # this gets all records of a book using their book id

    f = len(query) - 1 # gets index of latest action

    return str(query[f][1]) # returns member id of latest action on bookid

#get_member_id(20)
#get_book_state(20)

def check_member_id(id):#####
    try:# if user entered anything other than int would fail and return false
        id = int(id)
    except:
        id = id
        return False

    if id >=1000  and id<= 9999:# if it is int checks if its in range
        return True
    else:
        return False

def checkout_multiple(book_ids,member_id):
    book_ids = str(book_ids).split(";")# creates array of book ids
    states = []
    for i in book_ids:
        states.append(get_book_state(i))# for each book id gets its state and appends it to new array

    count = 0

    On_Loan_indexs = []
    str_On_Loan_indexs = "" # for output

    Available_indexs = []
    str_Available_indexs = "" # for output

    Reserved_indexs = []
    str_Reserved_indexs = ""# for output

    Not_in_Lib = []
    str_Not_in_Lib = ""

    for j in states:
        if j == "Available":# if the state is available add  it to corresponding array and add id to output msg
            Available_indexs.append(book_ids[count])#
            str_Available_indexs += book_ids[count] +","
        if j == "Out on loan":
            On_Loan_indexs.append(book_ids[count])
            str_On_Loan_indexs +=  book_ids[count] +","

        if j == "Reserved":
            Reserved_indexs.append(book_ids[count])
            str_Reserved_indexs += book_ids[count] +","

        if j == "Not in library":
            Not_in_Lib.append(book_ids[count])
            str_Not_in_Lib +=  book_ids[count] +","

        count += 1 # used as a tracker for indexs of array states and array book ids

    msg1 = "book ids " + str_Available_indexs + " have been withdrawn \n"
    msg2 = "book ids " + str_On_Loan_indexs + " can be reserved, would you like to reserve them, " \
                                              "if so press enter button again\n"
    msg3 = "book ids " + str_Reserved_indexs + " are unavailable \n"
    msg4 = "book ids " + str_Not_in_Lib + " are not in the library \n"
    outputmsg = ""

    if len(Available_indexs) >= 1: # if at least one book is available then show it in output
        outputmsg += msg1

    if len(On_Loan_indexs) >= 1:# if at least one book is on loan  then show it in output
        outputmsg += msg2

    if len(Reserved_indexs) >= 1:# if at least one book is reserved  then show it in output
        outputmsg += msg3

    if len(Not_in_Lib) >= 1:# if at least one book is reserved  then show it in output
        outputmsg += msg4

    for i in Available_indexs:
        ##print(i)
        add_record("Loan", member_id, i, get_date()) #updates logfile to loan all availabe books

    return [outputmsg,On_Loan_indexs]

def process_checkout(checkout_t_1,checkout_t_2, checkout_lb_4,checkout_btn_1):
    # args are member id, book id to get info and  label, enter button to be config based on inputs
    member_id = str(get_entry(checkout_t_1)).strip()#gets the text from first entry box
    book_ids = str(get_entry(checkout_t_2)).strip()#gets the text from second entry box
    #print(book_ids)

    if check_member_id(member_id) == False:## first check if it is a valid memebr id
        checkout_lb_4.config(text = "this is not a valid member id", foreground = "red")
    else:
            temp = checkout_multiple(book_ids,member_id)
            #above line calls func which creates temp array of [outputmsg,On_Loan_indexs]
            outputmsg = temp[0]
            On_Loan_indexs = temp[1]

            checkout_lb_4.config(text= outputmsg, foreground = "black")
            if len(On_Loan_indexs) >= 1:# if a book is on loan  text  will ask them if they want to reserve
                # by clicking on the enter button again
                # this line below changes the command of enter button from process checkout to reserve book
                checkout_btn_1.config(command=lambda: reserve_book(checkout_lb_4, member_id, On_Loan_indexs))


def reserve_book(checkout_lb_4,member_id,book_ids):
    for i in book_ids:## reserves all books in onloan which user selefcted
        add_record("Reserve", str(member_id), str(i), get_date())
    if len(book_ids)>=2:# display msg
        checkout_lb_4.config(text="Books have been reserved", foreground="green")
    else:
        checkout_lb_4.config(text="Book has been reserved", foreground="green")
