#F220759


#Book_Info format
# ID;Genre;Title;Author;Purchase Price £; Purchase Dateimport datetime

from database import *
from bookCheckout import *

def Search(title):
    records=Open_file("Book_Info.txt")
    #print("Title, Author, Genre, Loan availability") the
    query = []
    for i in records:
        if title.lower() == i[2].lower(): # if title equals a record in book info
            format = str(i[2]) +" | "+ str(i[3])+" | "+ str(i[1]) +" | "+ get_book_state(i[0]) ## format it right
            query.append(format)# adds it to array

    #print(query)# for debugging
    return query # returns an array of Title, Author, Genre, Loan availability , that match title user selected

#test function
    #print(query)
#s=input("")
#Search(s)


def show_entries(record,search_lb_2):
    temp = ""
    for i in record:
        temp += i +"\n" # for each entry in array record add it to string
    search_lb_2.config(text = temp) # edit the label to display the search results



def get_text(txt,search_lb_2):
    # for text boxes .get() needs start and stop characters of the string to get
    title_to_search = str(txt.get("1.0","end"))# gets user input
    results = Search(title_to_search.strip()) #returs a queryr of all books that match parameter
    show_entries(results,search_lb_2) # shows results to screen
