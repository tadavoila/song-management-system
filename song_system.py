from song_functions import *
#dictionary of menu options
the_menu = {"L" : "List",
            "A" : "Add",
            "E" : "Edit",
            "D" : "Delete",
            "M" : "Show statistical data on",
            "S" : "Save the data to file",
            "R" : "Restore data from file",
            "Q" : "Quit this program"}
#Dictionary of song information for ease of testing
all_songs = {
   "12332": {
      "title": "Cardigan",
      "artist": "Taylor Swift",
      "length": "03:59",
      "album": "Folklore",
      "genre": ["folk", "indie rock"],
      "rating": 4,
      "released": "07/27/2020",
      "favorite": True,
      "uid" : 12332
   },
   "14567": {
      "title": "Soul Meets Body",
      "artist": "Death Cab for Cutie",
      "length": "",
      "album": "Plans",
      "genre": ["indie pop", "indie rock"],
      "rating": 5,
      "released": "07/16/2005",
      "favorite": True,
      "uid":14567
      },
   "78210": {
      "title": "Fake Love",
      "artist": "BTS",
      "length": "04:02",
      "album": "",
      "genre": ["hip hop", "electro pop", "Korean pop"],
      "rating": 3,
      "released": "05/18/2018",
      "favorite": False,
      "uid":78210
      },
    "99105": {
      "title": "Foil",
      "artist": "'Weird Al' Yankovic",
      "length": "02:22",
      "album": "Mandatory Fun",
      "genre": ["pop", "parody"],
      "rating": 5,
      "released": "07/15/2014",
      "favorite": True,
      "uid": 99105
      }
}
#list_menu contains "List" menu sub-options
list_menu = {
    "A": "all songs - full",
    "B": "all songs - titles only",
    "F": "favorite songs",
    "G": "songs of a specific genre"
}

#stats_menu contains "Show statistical data on" menu sub-options
stats_menu = {
    "A": "Mean value of all song ratings",
    "B": "Median value of all song ratings",
    "C": "Standard Deviation value of all song ratings",
    "D": "Histogram of all song ratings"
}

#rating_map contains the meaning of each rating
rating_map = {
    "1": "Hate",
    "2": "Dislike",
    "3": "Neutral",
    "4": "Like",
    "5": "Love!"
}
opt = None

while True:
    print_main_menu(the_menu) #prints the menu
    opt = input("::: Enter a menu option\n> ")
    opt = opt.upper() # to allow us to input lower- or upper-case letters

    if opt not in the_menu.keys(): #Checks if the character stored in opt is in the_menu dictionary
        print(f"WARNING: {opt} is an invalid menu option.\n")
        continue

    print(f"You selected option {opt} to > {the_menu[opt]}.")

    if opt == 'Q': #Option to quit the program
        print("Goodbye!\n")
        break # exit the main `while` loop

    elif opt == 'L': #Option to list songs
        if all_songs == {}:
            print("WARNING: There is nothing to display!")
            # Pause before going back to the main menu
            input("::: Press Enter to continue")
            continue

        subopt = get_selection(the_menu[opt], list_menu) #calls get_selection, and based on user response, prints songs accordingly
        if subopt == 'A':
            print_songs(all_songs, rating_map, show_id = True)
        elif subopt == 'B':
            print_songs(all_songs, rating_map, title_only = True)
        elif subopt == 'F':
            print_songs(all_songs, rating_map, fave = True)
        elif subopt == 'G':
            print_songs(all_songs, rating_map, get_genre = True)

    elif opt == 'D': #Option to delete song
       continue_action = 'y'
       while continue_action == 'y': #runs unless there's a break or user wants to end
           if len(all_songs) == 0: #breaks if empty list
               print("WARNING: There is nothing to delete!")
               break
           
           print_songs(all_songs, rating_map, title_only = True, show_id = True)
           print("Which song would you like to delete?") #asks user for how they want to delete songs
           print("X - Delete all songs at once")
           print("::: OR Enter the number corresponding to the song ID")
           print("::: OR press 'M' to cancel and return to the main menu.")
           delete_option = input('> ')
           if delete_option == 'X': #if user wants to delete all songs
               print("::: WARNING! Are you sure you want to delete ALL songs?")
               print("::: Type Yes to continue the deletion.")
               Yes_or_not_Yes = input('> ')
               if Yes_or_not_Yes == 'Yes': #Makes sure user actually wants to delete all songs
                   for a_song in all_songs.copy():
                       delete_song(all_songs, a_song)
                   print("Deleted all songs.")
                   break
           elif delete_option.isdigit() == True: #if user wants to enter song id
               if delete_option not in all_songs: #if not valid song id
                   print(f"WARNING: |{delete_option}| is an invalid song ID!")
               else:
                   result = delete_song(all_songs, delete_option)
                   print("Success!")
                   print(f"Deleted the song |{result}|")
           elif delete_option.upper() == 'M': #if user wants to go back to main program
                break
           else: #if user inputs an invalid menu option
                print(f"WARNING: |{delete_option}| is an invalid menu option")
                         
           print("::: Would you like to delete another song? Enter 'y' to continue.") #asks the user if they want to continue
           continue_action = input("> ")
           if continue_action == "y":
               continue

    elif opt == 'A': #Option to add songs
        continue_action = 'y'
        while continue_action == 'y': 
            song_info = []
            print("::: Enter each required field:")
            #Get user inputs for all 9 song info fields (i.e. keys) as strings. 
            title = input("Title: ")
            artist = input("Artist: ") 
            length = input("Length (00:00 format): ")
            album = input("Album: ")
            genre = input("Genres (separate them with commas): ")
            rating = input("Rating (1-5): ")
            released = input("Release Date (MM/DD/YYYY format): ")
            favorite = input("Favorite (T/F): ")
            uid = input("Unique ID: ")

            song_info = [title, artist, length, album, genre, rating, released, favorite, uid] #creates a list of strings with the user's inputs
            
            result = get_new_song(song_info, rating_map, all_songs.keys()) #attempt to create a new song
            if type(result) == dict:
                all_songs[str(uid)] = result #add a new song to the list of songs
                print(f"Successfully added a new song!")
                print_song(result, rating_map)
            elif type(result) == tuple: #if get new song returns error
                print(f"WARNING: invalid data!")
                print(f"Error: {result[0]}")

            print("::: Would you like to add another song?", end=" ") #asks user if they want to continue
            continue_action = input("Enter 'y' to continue.\n> ")
            continue_action = continue_action.lower() 
            # ----------------------------------------------------------------
    
    elif opt == 'S': #Option to save data to .csv file
        continue_action = 'y'
        while continue_action == 'y':
            print("::: Enter the filename ending with '.csv'.")
            filename = input("> ")
            result = save_to_csv(all_songs, filename) #attempts to save data to csv
            if result == -1: #if save_to_csv returns error
                print(f"WARNING: |{filename}| is an invalid file name!") 
                print("::: Would you like to try again?", end=" ")
                continue_action = input("Enter 'y' to try again.\n> ")
            else:
                print(f"Successfully stored all the songs to |{filename}|") #prints a success statement if save_to_csv passed
                continue_action = 'n'
     #--------------------------------------------------------------------------
    elif opt == 'R': #Option to restore data from a .csv file
        continue_action = 'y'
        while continue_action == 'y': 
            print("::: Enter the filename ending with '.csv'.") #asks user for filename
            filename = input("> ")
            result = load_from_csv(filename, all_songs, rating_map, all_songs.keys()) #Calls the function with appropriate inputs and capture the output
            if result == -1: #if user didn't say a file that ends in .csv
                print(f"WARNING: invalid input - must end with '.csv'") 
                print("::: Would you like to try again?", end=" ")
                continue_action = input("Enter 'y' to try again.\n> ")
            elif result == None: #if user's file they requested to restore from does not exist
                print(f"WARNING: |{filename}| was not found!") 
                print("::: Would you like to try again?", end=" ")
                continue_action = input("Enter 'y' to try again.\n> ")
            elif result == []: #if every row in the csv file was sucessfully restored
                print(f"Successfully restored all songs from |{filename}|")
                continue_action = 'n'
            else: #if there was invalid data
                print(f"WARNING: |{filename}| contains invalid data!")
                print(f"The following rows from the file were not loaded:")
                print(result)
                print("::: Would you like to try again?", end=" ")
                continue_action = input("Enter 'y' to try again.\n> ")
     #--------------------------------------------------------------------------
    elif opt == 'E':
        continue_action = 'y'
        while continue_action == 'y':
            if all_songs == {}: #loop exits if dictionary of song dictionaries is empty
                print("WARNING: There is nothing to edit!")
                break
            print("::: Song list:")
            print_songs(all_songs, rating_map, title_only = True, show_id = True) #prints all possible songs to edit
            print("::: Enter the song ID you wish to edit.")
            user_option = input("> ")
            if user_option in all_songs: #check to see if the user-inputted ID is in the song dictionary
                subopt = get_selection("edit", all_songs[user_option], to_upper = False, go_back = True) #asks user which part of the song they want to edit
                if subopt == 'M': # if the user changed their mind
                    break
                print(f"::: Enter a new value for the field |{subopt}|") 
                field_info = input("> ")
                result = edit_song(all_songs, user_option, rating_map, subopt, field_info, all_songs.keys()) #edits the song dictionary if successful
                if type(result) == dict: #if edit_song() is successful 
                    print(f"Successfully updated the field |{subopt}|:") 
                    print_song(result, rating_map)  
                else: # edit_song() returned an error
                    print(f"WARNING: invalid information for the field |{subopt}|!")  
                    print(f"The song was not updated.")
            else: # song ID is incorrect/invalid
                print(f"WARNING: |{user_option}| is an invalid song ID!")  

            print("::: Would you like to edit another song?", end=" ") #asks user if they want to continue
            continue_action = input("Enter 'y' to continue.\n> ")
            continue_action = continue_action.lower()      
            # ----------------------------------------------------------------     
    elif opt == 'M':
        continue_action = 'y'
        while continue_action == 'y':
            if all_songs == {}: #loop exits if dictionary of song dictionaries is empty
                print("WARNING: There is nothing to show statistical data on!")
                break
            #gives user options on what rating stats they want to calculate (mean, median, standard deviation, or histogram)
            subopt = get_selection("show statistical data on", stats_menu, to_upper = True, go_back = False) 
            do_stats(all_songs, subopt) #calculates the stat the user requested and prints it
            print("::: Would you like to get different statistics?", end=" ") #asks user if they want to continue
            continue_action = input("Enter 'y' to continue.\n> ")
            continue_action = continue_action.lower()
    # Pause before going back to the main menu
    input("::: Press Enter to continue")

print("Have a nice day!")
