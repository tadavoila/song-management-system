def print_main_menu(menu):
    """
    Given a dictionary with the menu,
    prints the keys and values as the
    formatted options.
    Adds additional prints for decoration
    and outputs a question
    'What would you like to do?'
    """
    print('==========================')
    print('What would you like to do?')
    for key, value in menu.items(): #Iterates through dictionary
        print(key, '-', value)
    print('==========================')

######## LIST OPTION ########

def get_selection(action, suboptions, to_upper = True, go_back = False):
    """
    param: action (string) - the action that the user
            would like to perform; printed as part of
            the function prompt
    param: suboptions (dictionary) - contains suboptions
            that are listed underneath the function prompt.
    param: to_upper (Boolean) - by default, set to True, so
            the user selection is converted to upper-case.
            If set to False, then the user input is used
            as-is.
    param: go_back (Boolean) - by default, set to False.
            If set to True, then allows the user to select the
            option M to return back to the main menu

    The function displays a submenu for the user to choose from. 
    Asks the user to select an option using the input() function. 
    Re-prints the submenu if an invalid option is given.
    Prints the confirmation of the selection by retrieving the
    description of the option from the suboptions dictionary.

    returns: the option selection (by default, an upper-case string).
            The selection be a valid key in the suboptions
            or a letter M, if go_back is True.
    """
    selection = None
    if go_back: #If user selects to go back
        if 'm' in suboptions or 'M' in suboptions:
            print("Invalid submenu, which contains M as a key.")
            return None

    while selection not in suboptions: #Asks user for a option that is in the menu
        print(f"::: What would you like to {action.lower()}?")
        for key in suboptions:
            print(f"{key} - {suboptions[key]}")
        if go_back == True:
            selection = input(f"::: Enter your selection "
                              f"or press 'M' to return to the main menu\n> ")
        else:
            selection = input("::: Enter your selection\n> ")
        if to_upper:
            selection = selection.upper() # to allow us to input lower- or upper-case letters
        if go_back and selection.upper() == 'M':
            return 'M'

    if to_upper: #converts user sectiom from lower case to upper case   
        print(f"You selected |{selection}| to",
              f"{action.lower()} |{suboptions[selection].lower()}|.")
    else:
        print(f"You selected |{selection}| to",
          f"{action.lower()} |{suboptions[selection]}|.")
    return selection

def get_written_date(date_list):
    """
    The function takes as a parameter (date_list) a list of strings
    in the [MM, DD, YYYY] format
    and returns the resulting date (in the US format) as a string.
    """
    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    # Finishing the function
    date_string = ''
    date_string += month_names[int(date_list[0])] + ' ' + str(int(date_list[1])) + ', ' + str(int(date_list[2]))
    # Return the date string in written format
    return date_string

def print_song(song, rating_map, title_only = False, showid=False):
    """
    param: song (dict) - a single song dictionary
    param: rating_map (dict) - a dictionary object that is expected
            to have the string keys that correspond to the "rating"
            integer values stored in the song; the stored value is displayed for the
            rating field, instead of the numeric value.
    param: title_only (Boolean) - by default, set to False.
            If True, then only the name of the song is printed.
            Otherwise, displays the formatted song fields.
    param: show_id (Boolean) - by default, set to False.
            If False, then the id number of the song is not displayed.
            Otherwise, displays the id number.

    returns: None; only prints the song values

    Helper functions:
    - get_written_date() to display the 'duedate' field
        You created a similar function in a previous lab.
    """
    if title_only: #if user selects only title
        if showid:
            print(f'{"ID:":>9} {song["uid"]} |{"TITLE:":>9} {song["title"]}')
        else:
            print(f'{"TITLE:":>9} {song["title"]}')
    else:
        if showid: #if user wants us to show id
            print(f'{"ID:":>9} {song["uid"]} |{"TITLE:":>9} {song["title"]}')
        else:
            print(f'{"TITLE:":>9} {song["title"]}')
        for key, value in song.items(): #prints correct song information in correct format
            if key != 'uid' and key != 'title' and value != '': 
                if key == 'genre': #for genre
                    if (len(song['genre'])) == 0:
                        continue
                    else:
                        print(f"{key.upper():>8}: ", end = "")
                        for count in range(len(song['genre'])):
                            if (count + 1) < len(song['genre']):
                                print(f"{song['genre'][count].title()}", end = ', ')
                            else:
                                print(f"{song['genre'][count].title()}")
                elif key == 'rating': #for rating
                    print(f"{key.upper():>8}: {rating_map[str(song['rating'])]}") 
                elif key == 'released': #for release date
                    split_release_date = song['released'].split('/')
                    release_date = get_written_date(split_release_date)
                    print(f'{key.upper():>8}: {release_date}')
                else: #for all other info
                    print(f'{key.upper():>8}: {value}')
            else: #no need to print uid and title again, and prints for artist, favorite, and rating if blank value
                if key == 'artist':
                    print(f'{key.upper():>8}: {value}')
                elif key == 'favorite':
                    print(f'{key.upper():>8}: {value}')
                elif key == 'rating':
                    print(f'{key.upper():>8}: {value}')
                continue
        if not title_only:
            print("*"*42)

def print_songs(song_dict, rating_map, title_only = False, show_id = False, fave = False, get_genre = False):
    """
    param: song_dict (dict) - a dictionary containing dictionaries with
            the song data
    param: rating_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "rating"
            integer values stored in the song; the stored value is displayed 
            for the rating field, instead of the numeric value.
    param: title_only (Boolean) - by default, set to False.
            If True, then only the title of the song is printed.
            Otherwise, displays the formatted song fields.
    param: show_id (Boolean) - by default, set to False.
            If False, then the key (unique ID number) of the song is not displayed.
            Otherwise, displays the id number.
    param: fave (Boolean) - by default, set to False, and prints all songs.
            Otherwise, if it is set to True, prints only the songs marked as favorite.
            This parameter is meant to be used exclusive of get_genre
            (i.e. if fave=True, then get_genre should be False, and vice versa).
    param: get_genre (Boolean) - by default, set to False, and prints all songs.
            If set to True, then the function should ask the user for a
            genre keyword (string) and print only those songs that contain that string in its genre value.
            This parameter is meant to be used exclusive of fave (i.e. if fave=True, then get_genre should be False, and vice versa).
            NOTE: If a song has multiple instances of that genre keyword, you should only print the song once.

    returns: None; only prints the song values from the song_list

    Helper functions:
    - print_song() to print individual songs
    """
    print("*"*42)
    # Check to see if get_genre is True, so asking for the genre keyword can happen
    if get_genre == True:
       the_user_genre = input('Enter genre:: ')  
    # Go through all the songs in the song dictionary:
    for a_song in song_dict.values(): 
        # if not asking for favorites or specific genres: print everything
        if fave == False and get_genre == False:
            print_song(a_song, rating_map, title_only, show_id)
        # otherwise: if asking for favorites, print just those:
        elif fave and get_genre == False:
            if a_song['favorite'] == True:
                print_song(a_song, rating_map, title_only, show_id)
            else:
                continue
        # otherwise: if asking for a specific genre, print just those:
        elif get_genre:
            # search all the songs' genres for the genre keyword
            # and print only those songs, once, where that keyword appears in the genre value
            for element in a_song['genre']:
                if the_user_genre.strip().lower() in element.lower():
                    print_song(a_song, rating_map, title_only, show_id)
                    break
                else:
                    continue

######## ADD OPTION ########
def is_valid_addlist(input_list):
    """
    param: input_list (list) - a list of values that user provides for the song info fields

    The function checks if input_list is list made entirely of strings.

    return:
    return True if every element in input_list is a string
    return False if an element in input_list is not a string 
    """
    if len(input_list) != 9: #checks if length of list is 9
        return False
    is_valid_addlist_bool = None
    for entry in input_list:
        if type(entry) == str: #checks every entry in list is a string
            is_valid_addlist_bool = True
        else:
            return False
    return is_valid_addlist_bool

def is_valid_title(title_value):
    """
    param: title_value (string) - a string value for the title of the song

    The function checks if title_value is a string that is between 2 and 40
    characters long (inclusive).

    return:
    return True if title_value is a string between 2 and 40 character long (inclusive)
    return False if title_value is not a string between 2 and 40 characters long (inclusive)
    """

    if type(title_value) == str: 
        if 2 <= len(title_value) <= 40: #checks if length of title_value is between 2 and 40
            return True
        else:
            return False
    else:
        return False
    

def is_valid_time(time_value):
    """
    param: time_value (string) - a string containing the length of the song

    The function checks if time_value is a string that has 2 digits,
    followed by a colon, followed by 2 more digits.

    return:
    return True if time_value is a string that is in the format that's
        2 digits followed by a colon followed by 2 more digits - ex: "00:00"
    return False if time_value is not a string in the "00:00" format
    """

    if type(time_value) == str: #checks time_value is a string
        if len(time_value) == 5: #checks length of time_value is 5 characters
            if (time_value[2]) == ":": #checks third character is a :
                if time_value[0:2].isdigit() == True and time_value[3:5].isdigit() == True: #checks all characters but the : are digits
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

def is_valid_month(date_list):
    """
    The function takes the parameter date_list (a list of strings in the [MM, DD, YYYY] format)
    and returns True if month number is a possible month in the U.S.
    """
    if type(date_list[0]) == str: #checks type of the month value of date_list to ensure it's string
        if len(date_list[0]) == 2: #checks if month value of date_list has exactly 2 entries
            if date_list[0].isdigit() == True: #checks if month value of date_list has all digits
                if 0 < (int(date_list[0])) <= 12:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
        
def is_valid_day(date_list):
    """
    The function takes the parameter date_list (a list of strings in the [MM, DD, YYYY] format)
    and returns True if the provided day is a possible day for the given month.
    """
    #dictionary of max days in a month
    num_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    if is_valid_month(date_list) == True: #checks if the month value is valid 
        if date_list[1].isdigit() == True: #checks if the date is made of digits
            if int(date_list[1]) <= num_days[int(date_list[0])]: #checks that date is less than the number of max days in a month
                if int(date_list[1]) > 0: #checks that date is greater than 0
                    if type(date_list[1]) == str: #checks date is a string
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

def is_valid_year(date_list):
    """
    The function takes the parameter date_list (a list of strings in the [MM, DD, YYYY] format)
    and returns True if the provided year is a possible year: an integer & > 1000.
    """
    if type(date_list[2]) == str: #checks year is a string
        if str(date_list[2]).isdigit() == True: #checks year is made of digits
            if int(date_list[2]) > 1000: #checks year is greater than 1000
                return True
            else:
                return False
        else:
            return False  
    else:
        return False

def is_valid_date(released_value):
    """
    param: released_value (string) - a string containing a release date for a song

    The function checks if released_value is in MM/DD/YYYY format.

    return:
    return True if released_value is in MM/DD/YYYY format
    return False if released_value is not in MM/DD/YYYY format
    """
    #validating released_value type, length, and slash placement
    if type(released_value) != str: 
        return False
    if len(released_value) != 10:
        return False
    if released_value[2] != "/" or released_value[5] != "/":
        return False
    count_slash = 0 #validating slash amount (should be 2)
    for n in range(len(released_value)):
        if released_value[n] == '/':
            count_slash += 1
    if count_slash != 2:
        return False
    if released_value[0:2].isdigit() == False or released_value[3:5].isdigit() == False or released_value[6:10].isdigit() == False: #checking entry for digit placement
        return False
    
    date_list = released_value.split('/') #splits the released_value into a list

    #valid month?
    if is_valid_month(date_list) == False:
        return False
    
    #valid day?
    if is_valid_day(date_list) == False:
        return False

    #valid year?
    if is_valid_year(date_list) == False:
        return False

    #return True if all validation above passes
    return True     
    
def is_valid_uid(uid_str, key_list):
    """
    param: uid_str (str) - the "uid" value as a string (should be a string)
    param: key_list (list) - a list of all the keys in the song dictionary

    The function checks if the uid_str is an unique
    string of 5 digits whose range is between "10000" and "99999".
    
    return:
    return True if uid_str is a string made up of 5 digits whose range is between "10000" and "99999"
        and if the uid_str is unique to the current song_dictionary (all_songs)
    return False if uid_str is not a unique string made of 5 digits with a range between
        "10000" and "99999"
    """
    if type(uid_str) != str: #checks uid_str is string or not  
        return False
    elif len(uid_str) != 5: #checks uid_str length is 5 or not
        return False
    elif uid_str.isdigit() == False: #checks uid_str has all digits or not
        return False
    elif uid_str[0] == '0': #checks if uid_str first character is 0 or not
        return False
    elif uid_str in key_list: #checks uid_str is within key_list or not
        return False
    else:
        return True

def get_new_song(string_list, rating_map, key_list):
    """
    param: string_list (list) - a list of  of all needed song dictionary values stored as strings
    param: rating_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "rating"
            integer values stored in the song; the stored value is displayed 
            for the rating field, instead of the numeric value.
    param: key_list (list) - a list of all the keys in the song dictionary 

    The function first calls some of its helper functions
    to validate the provided values. If the validation passes,
    the values are added to a new dictionary with respective keys.
    Otherwise, an error message and number is displayed.

    return:
    If entire input list is not made up of strings,
        return a tuple containing message string "Bad list. Found non-string, or bad length" and the integer 0.
    If title is not a string that is at least 2 characters and at most 40 characters long,
        return a tuple containing the message string "Bad Title length" and the integer -1.
    If the length value is not in "00:00" format (string with 2 digits, a colon, and 2 digits),
        return a tuple containing the message string "Invalid time format for Length" and the integer -2.
    If the rating value is not a string that is a digit between 1 and 5 (inclusive),
        return a tuple containing the message string "Invalid Rating value" and the integer -3.
    If the released value is not in MM/DD/YYYY format,
        return a tuple containing the message string "Invalid date format for Release Date" and the integer -4.
    If favorite value is not a value that starts with "T", "t", "F", or "f",
        return a tuple containing the message string "Invalid value for Favorite" and the integer -5.
    If uid value is not a string made up of exactly 5 digits whose range is between "10000" and "99999" and/or is not unique to any other uid value,
        return a tuple containing the message string "Unique ID is invalid or non-unique" and the integer -6. 
    Otherwise, if validated,
        return a new dictionary with the song keys from key_list and the corresponding values from string_list
        
    Helper functions:
    The function calls the following helper functions:
    - is_valid_addlist()
    - is_valid_title()
    - is_valid_time()
    - is_valid_date()
    - is_valid_uid()
    """
    #validates input list of values, title, time_value, rating value, release date, favorite value, and uid value
    if is_valid_addlist(string_list) == False: 
        return ("Bad list. Found non-string, or bad length", 0)
    elif is_valid_time(string_list[2]) == False:
        return ("Invalid time format for Length", -2)
    elif type(string_list[5]) != str or string_list[5].isdigit() == False or int(string_list[5]) > 5 or int(string_list[5]) < 1:
        return ("Invalid Rating value", -3)
    elif is_valid_date(string_list[6]) == False:
        return ("Invalid date format for Release Date", -4)
    elif string_list[7] == '':
        return ("Invalid value for Favorite", -5)
    elif string_list[7][0].upper() != 'T' and string_list[7][0].upper() != 'F':
        return ("Invalid value for Favorite", -5)
    elif is_valid_uid(string_list[8], key_list) == False:
        return ("Unique ID is invalid or non-unique", -6)
    elif is_valid_title(string_list[0]) == False:
        return ("Bad Title length", -1)
    else: #validation passes, process of adding a new song begins
        user_song_info = {}
        key_inner = ['title', 'artist', 'length', 'album', 'genre', 'rating', 'released', 'favorite', 'uid']

        for counter in range(0, 9): #adds appropriate key and value to a song dictionary
            if key_inner[counter] == 'rating' or key_inner[counter] == 'uid':
                user_song_info[key_inner[counter]] = int(string_list[counter]) #converts rating and uid values to integer
            elif key_inner[counter] == 'favorite': #converts favorite value to bool
                favorite_bool = None
                if string_list[counter][0].upper() == 'T':
                    favorite_bool = True
                elif string_list[counter][0].upper() == 'F':
                    favorite_bool = False
                user_song_info[key_inner[counter]] = favorite_bool
            elif key_inner[counter] == 'genre': #formats string genre values
                new_list = []
                x = string_list[counter].split(',')
                for n in x:
                    y = n.strip() 
                    new_list.append(y)
                user_song_info[key_inner[counter]] = new_list
            else:
                user_song_info[key_inner[counter]] = string_list[counter] #adds other keys and values that don't need modification before adding
        return user_song_info
        
   
######## EDIT OPTION ########
def edit_song(song_dict, songid, rating_map, field_key, field_info, allkeys):
    """
    param: song_dict (dict) - dictionary of all songs
    param: songid (str) - a string that is expected to contain the key of
            a song dictionary (same value as its unique id)
    param: rating_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "rating"
            integer values stored in the song; the stored value is displayed 
            for the rating field, instead of the numeric value.
    param: field_key (string) - a text expected to contain the name
            of a key in the song dictionary whose value needs to 
            be updated with the value from field_info
    param: field_info (string) - a text expected to contain the value
            to validate and with which to update the dictionary field
            song_dict[field_key]. The string gets stripped of the
            whitespace and gets converted to the correct type, depending
            on the expected type of the field_key.
    param: allkeys (key_list) - a key_list of all keys in the song dictionary.

    The function first calls some of its helper functions
    to validate the provided field.
    If validation succeeds, the function proceeds with the edit.

    return:
    If song_dict is empty, return 0.
    If the field_key is not a string, return -1.
    If the remainder of the validation passes, return the dictionary song_dict[songid].
    Otherwise, return the field_key.

    Helper functions:
    The function calls the following helper functions depending on the field_key:
    - is_valid_title()
    - is_valid_time()
    - is_valid_date()
    - is_valid_uid()
    """
    field_info = field_info.strip() #strips field_info of leading/trailing white space
    if len(song_dict) == 0: #checks if song_dict is empty
        return 0
    elif type(field_key) != str: #checks if field_key is a string
        return -1
    #returns corresponding field_key if validation for field_info fails
    elif field_key == 'title':
        if not is_valid_title(field_info):
            return field_key
    elif field_key == 'length':
        if not is_valid_time(field_info):
            return field_key
    elif field_key == 'rating':
        if field_info.isdigit() == False or int(field_info) > 5 or int(field_info) < 1:
           return field_key
    elif field_key == 'released':
        if not is_valid_date(field_info):
            return field_key
    elif field_key == 'uid':
        if not is_valid_uid(field_info, allkeys):
            return field_key
        
    #if validation passes, edits the song_dict at the field_key value and adds field_info as the correct type   
    if field_key == 'uid' or field_key == 'rating':
        song_dict[songid][field_key] = int(field_info)
    elif field_key == 'favorite': #converts favorite value into a boolean
        favorite_bool = None
        if field_info != '': #validates favorite
            if field_info[0].upper() == 'T':
                favorite_bool = True
            elif field_info[0].upper() == 'F':
                favorite_bool = False
            else:
                return field_key 
        else:
            return field_key
        song_dict[songid][field_key] = favorite_bool
    elif field_key == 'genre': #edits genre values
        if field_info != '': #validates genre
            new_list = []
            x = field_info.split(',')
            for n in x:
                y = n.strip() 
                new_list.append(y)
            song_dict[songid][field_key] = new_list
        else:
            return field_key 
    else:
        song_dict[songid][field_key] = field_info
    return song_dict[songid] #returns a single song dictionary
        
######## DELETE OPTION ########

def delete_song(song_dict, songid):
    """
    param: song_dict - a dictionary of songs (dict of dict)
    param: songid (str) - a string that is expected to
            contain the key to a song dictionary (i.e. same as its unique ID)

    The function first checks if the dictionary of songs is empty.
    The function then validates the song ID to verify
    that the provided ID key can access an element from song_dict
    On success, the function saves the item's "title" from song_dict
    and returns that string ("title" value)
    after the item is deleted from song_dict.

    returns:
    If the input list is empty, return 0.
    If the ID is not valid (i.e. not found in the song_dict), return -1.
    Otherwise, on success, the entire song is removed from song_dict
    and the function returns the title of the deleted song.
    """
    if len(song_dict) == 0: #checks if song_dict is empty, and if so, returns 0
        return 0
    elif songid not in song_dict: #checks if the song id is not in song_dict, and if so, returns -1
        return -1
    else: #otherwise, deletes the song and returns the deleted song's title
        title = song_dict[songid]['title']
        del song_dict[songid]
        return title

######## SHOW STATISTICAL DATA ON OPTION ########

def do_stats(song_dict, opt):
    """
    param: song_dict - a dictionary of songs (dict of dict)
    param: opt (str) - an option from the menu
    to do one of the following statistical calculations:
        "A" - find the mean (average) of all song ratings values
        "B" - find the median of all song ratings values
        "C" - find the standard deviation of all song ratings values
        "D" - print out a histogram of all song ratings values

    Helpful hint: see example on top of page in
    zyBook Ch. 8.4 to see how to do mean and stddev calculations.

    returns: Nothing! This function only PRINTS out results.    
    """

    #calculate the mean
    summation = 0
    total_entries = 0
    new_list = []
    for key1, value1 in song_dict.items():
        for key2, value2 in value1.items():
            if key2 == 'rating':
                new_list.append(value2) #puts all ratings into a list
                summation += value2 #calculates sum of all ratings
                total_entries += 1 #calculates total entries
    mean = summation/total_entries
    
    #calculate the median
    new_list.sort()
    if total_entries % 2 == 1: #calculates median if odd number of ratings
        idx = int(total_entries // 2)
        median = new_list[idx]
    elif total_entries % 2 == 0: #calculates median if even number of ratings
        idx1 = int((total_entries / 2) - 1)
        idx2 = int(total_entries / 2)
        option1 = new_list[idx1]
        option2 = new_list[idx2]
        median = (option1 + option2) / 2

    #calculate the standard deviation
    tmp = 0
    for key1, value1 in song_dict.items():
        for key2, value2 in value1.items():
            if key2 == 'rating':
                tmp += (value2 - mean)**2
    std_dev = (tmp/total_entries)**0.5
        
    if opt == 'A': #prints the mean
        print(f"The mean value of all ratings is: {mean:.2f}")
    elif opt == 'B': #prints the median
        print(f"The median value of all ratings is: {median:.2f}")
    elif opt == 'C': #prints the standard deviation
        print(f"The standard deviation value of all ratings is: {std_dev:.2f}")
    elif opt == 'D': #prints a histogram of the ratings
        one = ""
        two = ""
        three = ""
        four = ""
        five = ""
        for element in new_list:
            if element == 1:
                one += "*"
            elif element == 2:
                two += "*"
            elif element == 3:
                three += "*"
            elif element == 4:
                four += "*"
            elif element == 5:
                five += "*"
        print(f"1 {one}\n2 {two}\n3 {three}\n4 {four}\n5 {five}")
######## SAVE OPTION ########

def save_to_csv(song_dict, filename):
    """
    param: song_dict(dict of dict) - The dictionary of songs stored 
    param: filename (str) - A string that ends with '.csv' which represents
               the name of the file to which to save the songs. This file will
               be created if it is not present, otherwise, it will be overwritten.

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv` as well as `import os`.

    The function will use the `with` statement to open the file `filename`.
    After creating a csv writer object, the function uses a `for` loop
    to loop over every song in the dictionary and creates a new dictionary
    containing only strings - this dictionary is saved into the file by the csv writer
    object. The order of the elements in the dictionary is:

    * title
    * artist
    * length
    * album
    * genre (all element in the original list are converted to string
        joined with commas separating)
    * rating (converted to string)
    * released (written as string, i.e, "06/06/2022", NOT "June 6, 2022")
    * favorite (converted to string)
    * uid

    returns:
    -1 if the last 4 characters in `filename` are not '.csv'
    None if we are able to successfully write into `filename`
    """
    import csv #imports csv module to help write csv files
    if filename[-4:] != '.csv': #checks if last 4 characters in filename are .csv or not
        return -1
    with open(filename, 'w', newline='') as csvfile: #opens the csvfile for writing
        writerObj = csv.writer(csvfile)
        new_list = [] #initializs a new list 
        for song in song_dict.values():
            for key, value in song.items():
                if key == 'genre':
                    new_list.append(','.join(element for element in song[key])) #appends dictionary values, if key is genre, to a new list
                else:
                    new_list.append(str(value)) #appends the dictionary values to a new list
            writerObj.writerow(new_list) #writes the list to a csv file row
            new_list = [] #resets the list

######## RESTORE OPTION ########

def load_from_csv(filename, in_dict, rating_map, allkeys):
    """
    param: filename (str) - A string variable which represents the
            name of the file from which to read the contents.
    param: in_dict (dict of dict) - A dictionary of songs (dictionary objects) to which
            the songs read from the provided filename are added.
            If in_dict is not empty, the existing songs are not dropped.
    param: rating_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "rating"
            integer values stored in the song; the stored value is displayed 
            for the rating field, instead of the numeric value.
    param: allkeys (key_list) - a key_list of all keys in the song dictionary

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv` and `import os`.

    If the file exists, the function will use the `with` statement to open the
    `filename` in read mode. For each row in the csv file, the function will
    proceed to create a new song using the `get_new_song()` function.
    - If the function `get_new_song()` returns a valid song object,
    it gets added to `in_dict`.
    - If the `get_new_song()` function returns an error, the 1-based
    row index gets recorded and added to the NEW list that is returned.
    E.g., if the file has a single row, and that row has invalid song data,
    the function would return [1] to indicate that the first row caused an
    error; in this case, the `in_dict` would not be modified.
    If there is more than one invalid row, they get excluded from the
    in_dict and their indices will be appended to the new list that's
    returned.

    returns:
    * -1, if the last 4 characters in `filename` are not '.csv'
    * None, if `filename` does not exist.
    * A new empty list, if the entire file is successfully read from `in_dict`.
    * A list that records the 1-based index of invalid rows detected when
      calling get_new_song().

    Helper functions:
    - get_new_song()
    """
    import csv #imports csv file to read
    import os #imports os module to help check if the filename exists
    if filename[-4:] != '.csv': #checks if last four characters of filename is .csv
        return -1
    elif os.path.isfile(filename) == False: #checks if filename exists or not
        return None
    else: #if validation passes, restores data from csv file
        with open(filename, 'r') as myfile:
            reader = csv.reader(myfile, delimiter = ',')
            new_list = [] #initalizes new list
            for index, row in enumerate(reader):
                counter = 0 #counts times a row is appended
                x = get_new_song(row, rating_map, allkeys) #gets a song to restore
                if type(x) == tuple:
                    if counter >= 1: #make sure each row, if appended, is appended only once
                        continue
                    else:
                        new_list.append(index+1) #appends invalid rows
                        counter += 1
                else:
                    in_dict[row[8]] = x #appends song to dictionary
        return new_list
