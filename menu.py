#F220759
from tkinter import *
from tkinter import Tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


from bookSearch import *
from database import *
from bookCheckout import *
from bookReturn import *
from bookSelect import *

window = Tk()
window.title("Coursework") #title of window
window.geometry("700x1000") #window dimensions

Menu_frame = Frame(window)
Menu_frame.pack(expand=True, fill="both")


#######functions used by all screens
def hide_component(x):#removes components from screen e.g buttons, labels etc
    x.pack_forget()

#used to delete all on screen components and go to next screen
def hide_screen(*args):
    for i in args:
        if i == "Search" or i =="Menu" or i =="Checkout" or i =="Return" or i == "Select":
            next_screen(i)
        else:
            hide_component(i)


##goes to respective screen
def next_screen(screen):
    if screen == "Search":
        create_search()# goes to search screen

    if screen == "Checkout":
        create_checkout()# goes to checkout screen

    if screen == "Menu":
        create_menu()#goes to menu screen

    if screen == "Return":
        create_return()# goes to return screen

    if screen == "Select":
        create_select()# goes to select screen


def get_date():# a function to get current date

    temp = str(datetime.date.today()) # get current date but uses -
    year = temp[2:4] # gets the year
    month = temp[5:7]# gets month
    day = temp[8:11] # gets day

    date = day + "/" + month + "/" + year # creates date in correct format
    return(date)


def get_entry(txt):# gets user input for entry boxes
    # for text boxes .get() needs start and stop characters of the string to get
    entry = str(txt.get("1.0","end")).strip()#formats input to get just input

    return entry

####### END of functions used by all

def create_menu():# creates title and buttons that points the user to their intended functionality
    menu_lb_1 = Label(Menu_frame,text="Menu screen for library", font = 20)
    menu_btn_1 = Button(Menu_frame, text="Search for Books",
                        command=lambda:hide_screen(menu_lb_1,menu_btn_1,menu_btn_2,menu_btn_3,menu_btn_4,"Search"))
    menu_btn_2 = Button(Menu_frame, text="Checkout  Books",
                        command=lambda:hide_screen(menu_lb_1,menu_btn_1,menu_btn_2,menu_btn_3,menu_btn_4,"Checkout"))
    menu_btn_3 = Button(Menu_frame, text="Return Books",
                        command=lambda:hide_screen(menu_lb_1,menu_btn_1,menu_btn_2,menu_btn_3,menu_btn_4,"Return"))
    menu_btn_4 = Button(Menu_frame, text="Select Books",
                        command=lambda:hide_screen(menu_lb_1,menu_btn_1,menu_btn_2,menu_btn_3,menu_btn_4,"Select"))
    ## when one of the above buttons are clicked it calls hide_screen which deletes
    ## all current buttons and calls the next function to create the next screen

    menu_lb_1.pack()
    menu_btn_1.pack()
    menu_btn_2.pack()
    menu_btn_3.pack()
    menu_btn_4.pack()
    ## displays button to screen


def create_search():# Menu Screen -> Search Screen

    search_lb_1 = Label(Menu_frame, text="Search screen for library", font=20)
    search_t_1 = Text(Menu_frame, height = 2, width = 30)# creates text box for user input
    search_btn_1 = Button(Menu_frame, text="Enter",
                          command = lambda:get_text(search_t_1,search_lb_2))#calls function in booksearch.py
                            #gets the text inputted  and eventually updates search_lb_2 to show relevant data
    search_btn_2 = Button(Menu_frame, text="back to menu",
                          command=lambda:hide_screen(search_lb_1,search_t_1,search_btn_1,search_lb_2,search_btn_2,"Menu"))
                            # goes back to menu screen
    search_lb_2 = Label(Menu_frame, text="")



    search_lb_1.pack()
    search_t_1.pack()
    search_btn_1.pack()
    search_lb_2.pack()
    search_btn_2.pack()
    ## displays button to screen


def create_checkout():# Menu Screen -> checkout Screen

    checkout_lb_1 = Label(Menu_frame, text="Checkout screen for library", font=20)
    checkout_lb_2 = Label(Menu_frame, text="Enter below your member id")
    checkout_t_1 = Text(Menu_frame, height = 2, width = 30)
    checkout_lb_3 = Label(Menu_frame, text="Enter below the id of the book(s) to be taken out separated by a \";\" ")
    checkout_t_2 = Text(Menu_frame, height=2, width=30)

    checkout_btn_1 = Button(Menu_frame, text="Enter",
                            command = lambda:process_checkout(checkout_t_1,checkout_t_2,
                                                              checkout_lb_4,checkout_btn_1))
    # above line calls function in bookCheckout.py to process checkout

    checkout_lb_4 = Label(Menu_frame, text="")
    checkout_btn_2 = Button(Menu_frame, text="back to menu",
                            command=lambda:hide_screen(checkout_lb_1,checkout_lb_2,checkout_t_1,checkout_lb_3,
                                                       checkout_t_2,checkout_btn_1,checkout_lb_4,checkout_btn_2,"Menu"))
    # above line hides all tk components and creates the menu screen again


    #displays tk components to screen
    checkout_lb_1.pack()
    checkout_lb_2.pack()
    checkout_t_1.pack()
    checkout_lb_3.pack()
    checkout_t_2.pack()

    checkout_lb_4.pack()
    checkout_btn_1.pack()
    checkout_btn_2.pack()


#--------Return screen

def create_return():# Menu Screen -> return Screen

    return_lb_1 = Label(Menu_frame, text="Return screen for library", font=20)
    return_lb_2 = Label(Menu_frame, text="Enter below the book id(s) separated by a \";\" ")
    return_t_1 = Text(Menu_frame, height = 2, width = 30)

    return_btn_1 = Button(Menu_frame, text="Enter",command = lambda:process_return(return_t_1,return_lb_3))

    return_lb_3 = Label(Menu_frame, text="")
    return_btn_2 = Button(Menu_frame, text="back to menu",
                          command=lambda:hide_screen(return_lb_1,return_lb_2,
                                                     return_t_1,return_lb_3,return_btn_1,return_btn_2,"Menu"))


    #displays tk components to screen
    return_lb_1.pack()
    return_lb_2.pack()
    return_t_1.pack()
    return_lb_3.pack()
    return_btn_1.pack()
    return_btn_2.pack()


#-Select screen----------

def create_graph(genres,count):
    lns1 = plt.bar(genres,count)
    plt.ylabel("transaction number")
    plt.xlabel("genres")
    plt.legend([lns1],["Bar"])
    plt.draw()
    plt.show()


def process_select(select_t_1,select_lb_3):
    budget = get_budget(select_t_1)
    popular= popular_books()
    recommendations = get_rec_title(popular,budget)
    display_recommended_books(recommendations,select_lb_3)

    graph_info = get_graph_info(recommendations)
    create_graph(graph_info[0],graph_info[1]) ## creates graph



def create_select():# creates the select sreen
    #creates components
    select_lb_1 = Label(Menu_frame, text="Select books to order screen for library", font=20)
    select_lb_2 = Label(Menu_frame, text="Enter your budget below (£)")
    select_t_1 = Text(Menu_frame, height=2, width=30)

    select_btn_1 = Button(Menu_frame, text="Enter", command=lambda: process_select(select_t_1,select_lb_3))
    # when pressed goes to process select function

    select_lb_3 = Label(Menu_frame, text="")
    select_btn_2 = Button(Menu_frame, text="back to menu",
                          command=lambda: hide_screen(select_lb_1, select_lb_2, select_t_1, select_lb_3, select_btn_1,
                                                      select_btn_2, "Menu"))
    #displays tk components to screen
    select_lb_1.pack()
    select_lb_2.pack()
    select_t_1.pack()

    select_btn_1.pack()
    select_lb_3.pack()
    select_btn_2.pack()





create_menu()## calls create_menu function

window.mainloop()


