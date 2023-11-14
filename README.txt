Menu.py
----------
1)Variable naming conventions:
    tk components are labelled as screen_component_componentNumber
    e.g the second button in the return screen is return_btn_2.
    (This is the back to menu screen button)

2)How menu navigation works
    after selecting a button from the menu screen,
    1) all of the current tk components are forgotten using
        hide_component() & hide_screen
    2) the program then creates all the components for the selected screen
    the process is the same for the back to menu button



3) Graph of selected titles
    i couldn't find a way to make it so the graph was embedded into the gui.
    as a result i left it as a pop up


Logfile.txt notes
----------------
format is as below:
include Loan-Return-Reserve;  Member_id; Book_id; CheckoutDate-ReturnDate;
#------------------
#example Loan; Book_id; Member_id; CheckoutDate
#example Return; Book_id; Member_id; ReturnDate
#example Reserve; Book_id; Member_id
#---------------------
