#comment the is valid days/months/years

from song_functions import *

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

rating_map = {
    "1": "Hate",
    "2": "Dislike",
    "3": "Neutral",
    "4": "Like",
    "5": "Love!"
}

#GET_WRITTEN_DATE
assert get_written_date(["01", "02", "2022"]) == 'January 2, 2022'
assert get_written_date(["01", "12", "1970"]) == 'January 12, 1970'
assert get_written_date(["04", "14", "2020"]) == 'April 14, 2020'
assert get_written_date(["06", "19", "2000"]) == 'June 19, 2000'


######## RESTORE OPTION ########

save_to_csv(all_songs, 'music_songs.csv')
new_dict = {}
assert load_from_csv('musicseihfelsifhlsfe.csv', new_dict, rating_map, all_songs.keys()) == None
assert load_from_csv('music_songs', new_dict, rating_map, all_songs.keys()) == -1

########ADD OPTION########
addlist1 = ["Cardigan - Extended Version", "Taylor Swift", "07:59", "Folklore", "folk,indie rock", "3", "07/27/2020", "True", "12333"]
addlist2 = ["Cardigan - Extended Version", "Taylor Swift", "07:59", "Folklore", "folk,indie rock", 3, "07/27/2020", True, "12333"]
addlist3 = ["Cardigan - Extended Version", "Taylor Swift", "b7:59", "Folklore"]

assert is_valid_addlist(addlist1) == True
assert is_valid_addlist(addlist2) == False
assert is_valid_addlist(addlist3) == False

assert is_valid_title(12) == False
assert is_valid_title(12.5) == False
assert is_valid_title("a") == False
assert is_valid_title("aa") == True
assert is_valid_title("0123456789012345678901234567890123456789") == True
assert is_valid_title("01234567890123456789012345678901234567890") == False

assert is_valid_time(addlist1[2]) == True
assert is_valid_time(addlist3[2]) == False
assert is_valid_time("00:000") == False
assert is_valid_time("1:111") == False
assert is_valid_time("00:d5") == False

# test incorrect types
assert is_valid_month([12, 31, 2021]) == False
assert is_valid_day([12, 31, 2021]) == False
assert is_valid_year([12, 31, 2021]) == False
    
# test the correct input
assert is_valid_month(["01", "01", "1970"]) == True
assert is_valid_month(["12", "31", "2021"]) == True
assert is_valid_day(["02", "03", "2000"]) == True
assert is_valid_day(["12", "31", "2021"]) == True
assert is_valid_year(["10", "15", "2022"]) == True
assert is_valid_year(["12", "31", "2021"]) == True

### test the edge cases
assert is_valid_month(["21", "01", "1970"]) == False
assert is_valid_month(["-2", "31", "2021"]) == False
assert is_valid_month(["March", "31", "2021"]) == False
assert is_valid_day(["02", "33", "2000"]) == False
assert is_valid_day(["02", "31", "2021"]) == False
assert is_valid_day(["02", "1st", "2021"]) == False
assert is_valid_day(["14", "1st", "2021"]) == False
assert is_valid_year(["10", "15", "22"]) == False
assert is_valid_year(["12", "31", "-21"]) == False
assert is_valid_year(["12", "31", "1000"]) == False

assert is_valid_date("07/14/2022") == True
assert is_valid_date(7/14/2022) == False
assert is_valid_date("7/14/2022") == False
assert is_valid_date("07014/2022") == False
assert is_valid_date("07/0142022") == False
assert is_valid_date("07/014/22/") == False
assert is_valid_date("a7/14/2022") == False
assert is_valid_date("07/1h/2022") == False
assert is_valid_date("07/14/20y2") == False
assert is_valid_date("13/14/2022") == False
assert is_valid_date("00/14/2022") == False
assert is_valid_date("07/32/2022") == False
assert is_valid_date("07/14/999") == False

assert is_valid_uid("12333", all_songs.keys()) == True
assert is_valid_uid("12332", all_songs.keys()) == False
assert is_valid_uid(12333, all_songs.keys()) == False
assert is_valid_uid("123333", all_songs.keys()) == False
assert is_valid_uid("12d33", all_songs.keys()) == False
assert is_valid_uid("02333", all_songs.keys()) == False
assert is_valid_uid("10000", all_songs.keys()) == True
assert is_valid_uid("99999", all_songs.keys()) == True
assert is_valid_uid("9999", all_songs.keys()) == False
assert is_valid_uid("100000", all_songs.keys()) == False

song_info1 = ['I Love You', "Barney & Friends", "01:00", "Barney's Favorites, Volume 1", "Children's Music, nursery rhyme", "5", "04/06/1992", "True", "10000"]
assert get_new_song(song_info1, rating_map, all_songs.keys()) == {'title': 'I Love You',
                                                                  'artist': 'Barney & Friends',
                                                                  'length': '01:00',
                                                                  'album': "Barney's Favorites, Volume 1",
                                                                  'genre': ["Children's Music", 'nursery rhyme'],
                                                                  'rating': 5,
                                                                  'released': '04/06/1992',
                                                                  'favorite': True,
                                                                  'uid': 10000}
song_info2 = ['I Love You', "Barney & Friends", "01:00", "Barney's Favorites, Volume 1", "Children's Music, nursery rhyme", 5, "04/06/1992", "True", "10000"]
assert get_new_song(song_info2, rating_map, all_songs.keys()) == ("Bad list. Found non-string, or bad length", 0)
song_info3 = ['I', "Barney & Friends", "01:00", "Barney's Favorites, Volume 1", "Children's Music, nursery rhyme", "5", "04/06/1992", "True", "10000"]
assert get_new_song(song_info3, rating_map, all_songs.keys()) == ("Bad Title length", -1)
song_info4 = ['I Love You', "Barney & Friends", "01:p0", "Barney's Favorites, Volume 1", "Children's Music, nursery rhyme", "5", "04/06/1992", "True", "10000"]
assert get_new_song(song_info4, rating_map, all_songs.keys()) == ("Invalid time format for Length", -2)
song_info5 = ['I Love You', "Barney & Friends", "01:00", "Barney's Favorites, Volume 1", "Children's Music, nursery rhyme", "A", "04/06/1992", "True", "10000"]
assert get_new_song(song_info5, rating_map, all_songs.keys()) == ("Invalid Rating value", -3)
song_info6 = ['I Love You', "Barney & Friends", "01:00", "Barney's Favorites, Volume 1", "Children's Music, nursery rhyme", "6", "04/06/1992", "True", "10000"]
assert get_new_song(song_info6, rating_map, all_songs.keys()) == ("Invalid Rating value", -3)
song_info7 = ['I Love You', "Barney & Friends", "01:00", "Barney's Favorites, Volume 1", "Children's Music, nursery rhyme", "5", "04/006/1992", "True", "10000"]
assert get_new_song(song_info7, rating_map, all_songs.keys()) == ("Invalid date format for Release Date", -4)
song_info8 = ['I Love You', "Barney & Friends", "01:00", "Barney's Favorites, Volume 1", "Children's Music, nursery rhyme", "5", "04/06/1992", "Awesome", "10000"]
assert get_new_song(song_info8, rating_map, all_songs.keys()) == ("Invalid value for Favorite", -5)
song_info9 = ['I Love You', "Barney & Friends", "01:00", "Barney's Favorites, Volume 1", "Children's Music, nursery rhyme", "5", "04/06/1992", "True", "12332"]
assert get_new_song(song_info9, rating_map, all_songs.keys()) == ("Unique ID is invalid or non-unique", -6)

######## EDIT OPTION ########
zero_dict = {}
assert edit_song(zero_dict, '99105', rating_map, 'title', 'My Song', all_songs.keys()) == 0
assert edit_song(all_songs, '99105', rating_map, 1, 'My Song', all_songs.keys()) == -1
assert edit_song(all_songs, '99105', rating_map, 'title', 'M', all_songs.keys()) == 'title'
assert edit_song(all_songs, '99105', rating_map, 'length', 'd1:22', all_songs.keys()) == 'length'
assert edit_song(all_songs, '99105', rating_map, 'rating', '6', all_songs.keys()) == 'rating'
assert edit_song(all_songs, '99105', rating_map, 'released', '25/12/2025', all_songs.keys()) == 'released'
assert edit_song(all_songs, '99105', rating_map, 'uid', '565', all_songs.keys()) == 'uid'

assert edit_song(all_songs, '99105', rating_map, 'title', 'My Song', all_songs.keys()) == {'title': 'My Song', 'artist': "'Weird Al' Yankovic", 'length': '02:22', 'album': 'Mandatory Fun', 'genre': ['pop', 'parody'], 'rating': 5, 'released': '07/15/2014', 'favorite': True, 'uid': 99105}
assert edit_song(all_songs, '99105', rating_map, 'rating', '2', all_songs.keys()) == {'title': 'My Song', 'artist': "'Weird Al' Yankovic", 'length': '02:22', 'album': 'Mandatory Fun', 'genre': ['pop', 'parody'], 'rating': 2, 'released': '07/15/2014', 'favorite': True, 'uid': 99105}
assert edit_song(all_songs, '99105', rating_map, 'artist', 'Al', all_songs.keys()) == {'title': 'My Song', 'artist': "Al", 'length': '02:22', 'album': 'Mandatory Fun', 'genre': ['pop', 'parody'], 'rating': 2, 'released': '07/15/2014', 'favorite': True, 'uid': 99105}
assert edit_song(all_songs, '99105', rating_map, 'length', '01:20', all_songs.keys()) == {'title': 'My Song', 'artist': "Al", 'length': '01:20', 'album': 'Mandatory Fun', 'genre': ['pop', 'parody'], 'rating': 2, 'released': '07/15/2014', 'favorite': True, 'uid': 99105}
assert edit_song(all_songs, '99105', rating_map, 'album', 'Sweet', all_songs.keys()) == {'title': 'My Song', 'artist': "Al", 'length': '01:20', 'album': 'Sweet', 'genre': ['pop', 'parody'], 'rating': 2, 'released': '07/15/2014', 'favorite': True, 'uid': 99105}
assert edit_song(all_songs, '99105', rating_map, 'released', '01/01/1901', all_songs.keys()) == {'title': 'My Song', 'artist': "Al", 'length': '01:20', 'album': 'Sweet', 'genre': ['pop', 'parody'], 'rating': 2, 'released': '01/01/1901', 'favorite': True, 'uid': 99105}
assert edit_song(all_songs, '99105', rating_map, 'genre', 'country, pop', all_songs.keys()) == {'title': 'My Song', 'artist': "Al", 'length': '01:20', 'album': 'Sweet', 'genre': ['country', 'pop'], 'rating': 2, 'released': '01/01/1901', 'favorite': True, 'uid': 99105}
assert edit_song(all_songs, '99105', rating_map, 'favorite', 'False', all_songs.keys()) == {'title': 'My Song', 'artist': "Al", 'length': '01:20', 'album': 'Sweet', 'genre': ['country', 'pop'], 'rating': 2, 'released': '01/01/1901', 'favorite': False, 'uid': 99105}
assert edit_song(all_songs, '99105', rating_map, 'uid', '99106', all_songs.keys()) == {'title': 'My Song', 'artist': "Al", 'length': '01:20', 'album': 'Sweet', 'genre': ['country', 'pop'], 'rating': 2, 'released': '01/01/1901', 'favorite': False, 'uid': 99106}

######## DELETE OPTION ########
assert delete_song(zero_dict, '12332') == 0
assert delete_song(all_songs, '45646') == -1
assert delete_song(all_songs, '12332') == 'Cardigan'

######## SAVE OPTION ########

assert save_to_csv(all_songs, 'song_file.csv') == None
assert save_to_csv(all_songs, 'song_file.pdf') == -1



