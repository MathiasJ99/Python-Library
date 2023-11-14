import datetime
from database import *
#F220759

from bookCheckout import *

def get_date():#gets date

    temp = str(datetime.date.today())
    year = temp[2:4]
    month = temp[5:7]
    day = temp[8:11]

    date = day + "/" + month + "/" + year
    return(date)

def get_entry(txt):
    # for text boxes .get() needs start and stop characters of the string to get
    entry = str(txt.get("1.0","end")).strip()

    return entry

def process_return(return_t_1,return_lb_3):
    book_ids= get_entry(return_t_1)# gets book ids to return
    book_ids=book_ids.split(";")#splits them into an array


    available =""
    added = ""
    reserved = ""

    for i in book_ids:
        state = get_book_state(i)# returns state of book (Available, Out on loan, Reserved, or not in library
        if state == "Available":
            available+= ", "+ i ## cant return a book that already there

        else:
            if state == "Out on loan":
                memberid = get_member_id(i)# gets the memeber id of books most recent action
                add_record("Return",memberid,str(i),get_date())
                added+= ", "+ i

            if state == "Reserved":
                reserved += ", "+ i

    msg1 = "book ids " + available + " cant be returned as they are currently available" + "\n"
    msg2 = "book ids " + added +" have been returned"+ "\n"
    msg3 =  "book ids " + reserved + " cant be returned as they are currently reserved" + "\n"
    show = ""
    if len(available) >= 1: ## if available is  not empty show msg 1
        show+= msg1

    if len(added) >=1:## if added is  not empty show msg 2
        show+= msg2

    if len(reserved) >=1:## if reserved is  not empty show msg 3
        show+= msg3

    return_lb_3.config(text = show)# updtates label to show what it message
