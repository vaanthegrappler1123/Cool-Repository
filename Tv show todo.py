#Nirvaan Jaitli
# Period 4
#To Do List
#1/19/24

x=["Dragon Ball Z", "Family Guy", "Naruto", "The Boys", "Impractical Jokers", "Loki", "Clone Wars"]

#Displays a list of movies and allows user to amend and mark movies as seen
def menu():
    global list
    global watchshow
    global showwatched
    global x
    while True:
        print("Welcome to the TV Show watch list")
        print("Please select an option using 1-5")
        print("1. Add a show to the list \n2. View the current watchlist \n3. Mark a show as watched \n4. Remove a show from the watchlist \n5. Exit the Program ")
        option = int(input("option: "))
        if option == 1:
            x.append(input("what TV Shows would you like to add?"))
        if option == 2:
            print(x)
        if option == 3:
            watchshow = str((input("What TV Show did you watch?")))
            showwatched = x.index(watchshow)
            x[showwatched] = (watchshow + " X")
        if option == 4:
            x.remove(input("What show do you want to remove?"))
        if option == 5:
            quit()
menu()
