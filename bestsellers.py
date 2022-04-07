#CS 175L-01
#Jelissa Reyes, Kevin Botwinick, Anthony Pastorelli
#Best Sellers project

def main():
   book = []
   best_sellers = open("bestsellers.txt" ,"r")
   for line in best_sellers:
        line=line.strip().split("\t")
        book.append(line)
        run = False
        while run == False:
            menu()
def showBooks(books):
    data = books
    for book in books:
        data = books
        print("title: : " ,data[0], "author : " ,data[1], "publisher: " ,data[2], "date: " ,data[3], "fiction/nonfiction: " ,data[4])
def menu(b):
    choice = input("What would you like to do? \n 1: look up year range \n 2:Look uo month/year \n 3: Search for author \n 4: Search for title \n Q: Quit")
    if choice == "1":
        year_range()
        menu()
    if choice == "2":
        month_year()
        menu()
    if choice == "3":
        author()
        menu()
    if choice == "4":
        title()
        menu()
    if choice == "Q":
        quit
def year_range():
    year1 = input("Enter start year")
    year2 = input("Enter end year")
    with open("bestsellers.txt" ,"r") as file_object:
        processed_file = file.object.read().split("\n")
        for year in range(int(year1),int(year2))+ 1:
            a = []
            for sublist in processed_file:
                if str(year) in sublist:
                    a.appen(sublist.split("\t"))
            for item in a:
                print(item)
                            
def month_year():
    specific_month = input("Enter month (1-12)")
    specific_year = input("Enter year:")
    for line in books:
        date = line[3].split('/')
        year = int(date[2])
        month = int(date[0])
        if month >= specific_month and month <= specific_month:
            if year >= specific_year and year <= specific_year:
                print(line[0], "by:" ,line[1], "(pub date:" ,line[3],")")
def author():
    author_search = input("Enter search string:").lower()
    for line in books:
        if author in line[1].lower():
            print(line[0],"by:",line[1],"(pub date:" ,line[3],")")
def title():
    title_search = input("Enter search string:")
    for line in books:
        if title in line[0].lower():
            print(line[0],"by:" ,line[1],"(pub date:" ,line[3],")")
main()    
