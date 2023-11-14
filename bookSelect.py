#F220759

from database import *


def get_budget(select_t_1):
    temp = int(select_t_1.get("1.0","end").strip()) # gets input
    return temp


def popular_books():
    book_info_records = Open_file("Book_Info.txt")
    log_file_records = Open_file("Logfile.txt")

    book_ids = []# ids of books from book_info ( 1 - 23)
    book_names = []
    book_genres = []
    book_prices = []
    ids = [] # record of all ids in log_file
    id_count = [] # frequnceny of each id in log_file

    book_infos = [] # [name,count,genre,price,No of copies]


    for i in book_info_records:#
        book_ids.append(i[0])
        book_genres.append(i[1])
        book_names.append(i[2])
        book_prices.append(i[4])

    for j in log_file_records:#gets a list of all the ids in each line of logfile.txt
        ids.append(j[2])


    for k in book_ids:#gets the frequency of each id in log file and creates list with indexs = book ids
        id_count.append(ids.count(str(k)))

    for i in range(0,len(book_ids)):## loops through all book ids and
        title = book_names[i] # gets the name of current book
        exists = False

        for j in range(0,len(book_infos)):
            if str(title) == str(book_infos[j][0]):# when trying to add record to book_info check if book already in it
                exists = True
                break;

        if exists == True:# if the book is a duplicate it increases the count of its existing record
            current_count = int(book_infos[j][1])
            book_infos[j][1] = current_count + int(id_count[i])

            current_copies = book_infos[j][4]
            book_infos[j][4] = current_copies + 1
        else:
            book_infos.append([book_names[i],id_count[i],book_genres[i],book_prices[i],1])
            #else creates new record with count 1

    sorted_books = sort_desc(book_infos) # calls function to sort books
    return sorted_books


def sort_desc(book_infos):
    print("###")
    n = sorted(book_infos, key=lambda book_infos: book_infos[1], reverse = True) # sorts books based off of count
    return n


def get_rec_title(book_infos,budget):## gets a list of books with the highes count
    # that are under the budget
    recommendations = []
    #print(budget)
    #print(book_infos)
    counter = 0
    while budget >0:
        new_budget = budget-float(book_infos[counter][3]) #budget - price of next book
        if new_budget >=0: #if above budget add it
            recommendations.append(book_infos[counter])
            budget-=float(book_infos[counter][3])
            counter+=1
        else:# else stop
            break;


    return recommendations ### returns recommendations of books to buy according
    # to the highest transaction log and within budget



def display_recommended_books(books,select_lb_3):
    msg1 = "The books to buy :"
    msg2 = "name, genre, price,count"
    format = ""
    for i in books:
        #[name,count,genre,price,No of copies]
        format += str(i[0]) + " | " + str(i[2]) +" | " +str(i[3]) +" | " +str(i[1]) + "\n"
        #formats string
    select_lb_3.config(text = msg1 + "\n"+ msg2 + "\n"+ format)# displays messages



def get_graph_info(books):
    genres = []
    count = []
    for i in books: # loops throw list of books
        book_genres = i[2].split(",")# a book can have multiple genres separated by commas
        for j in book_genres: # loops through the book's genres
            if j not in genres: # if the book's genres isn't in the genres list, append it
                genres.append(j)
                count.append(1)
            else:
                count[genres.index(j)] = int(count[genres.index(j)]) + 1 # otherwise add 1 to the genre

    return [genres,count]


#testing
#popular_books()

#todo
#get decending list of most popular books
#get bar chart of genres and