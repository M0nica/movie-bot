import config
import time
from twython import Twython, TwythonError
import requests
imdb_key = config.imdb_key

# create a Twython object by passing the necessary secret passwords
twitter = Twython(config.api_key, config.api_secret, config.access_token, config.token_secret)

# get two most recent mentions from twitter
response = twitter.get_mentions_timeline(count =2, since_id=14927799)
# print(response)


# the expected format is:
#line = "@TheMovieFacts_ revenue [movie name]"

# strip beginning of string to only have the movie name
movie_query = line[24:]
# print(movie_query)


# search for the id number of the movie that was tweeted at us
response = requests.get('https://api.themoviedb.org/3/search/movie?api_key=' +  imdb_key  + '&language=en-US&page=1&include_adult=false&query=' + movie_query)

movies = response.json()

#assume the first result is the correct movie
print(movies['results'][0])

#  get movie id from the first movie
movie_id = movies['results'][0]['id']

# get detailed info for the movie, incl. revenue

movie = response.json()

# print(movie)

revenue = movie['revenue']


import humanize

#format revenue to be printed how we expect money to be printed (in millions and not a billion digits)


revenue_formatted = "$" + humanize.intword(revenue)
# revenue_formatted

# print(id)

# movie['original_title'] + " has earned " + revenue_formatted + " in revenue."
# 'Home Alone 3 has earned $79.1 million in revenue.'
twitter.update_status(status=movie['original_title'] + " has earned " + revenue_formatted + " in revenue.", in_reply_to_status_id_str=id)_

## expect in_reply_to_status_id_str to not be blank!!!!!

# {'contributors': None,
#  'coordinates': None,
#  'created_at': 'Thu Mar 29 01:30:02 +0000 2018',
#  'entities': {'hashtags': [], 'symbols': [], 'urls': [], 'user_mentions': []},
#  'favorite_count': 0,
#  'favorited': False,
#  'geo': None,
#  'id': 979168773004505088,
#  'id_str': '979168773004505088',
#  'in_reply_to_screen_name': None,
#  'in_reply_to_status_id': None,
#  'in_reply_to_status_id_str': None,
#  'in_reply_to_user_id': None,
#  'in_reply_to_user_id_str': None,
#  'is_quote_status': False,
#  'lang': 'en',
#  'place': None,
#  'retweet_count': 0,
#  'retweeted': False,
#  'source': '<a href="http://www.aboutmonica.com" rel="nofollow">imdb-api</a>',
#  'text': 'Home Alone 3 has fearnedd $79.1 million in revenue.',
#  'truncated': False,
#  'user': {'contributors_enabled': False,
#   'created_at': 'Thu Mar 29 00:17:32 +0000 2018',
#   'default_profile': True,
#   'default_profile_image': True,
#   'description': '',
#   'entities': {'description': {'urls': []}},
#   'favourites_count': 0,
#   'follow_request_sent': False,
#   'followers_count': 0,
#   'following': False,
#   'friends_count': 0,
#   'geo_enabled': False,
#   'has_extended_profile': False,
#   'id': 979150529837371394,
#   'id_str': '979150529837371394',
#   'is_translation_enabled': False,
#   'is_translator': False,
#   'lang': 'en',
#   'listed_count': 0,
#   'location': '',
#   'name': 'Movie Facts',
#   'notifications': False,
#   'profile_background_color': 'F5F8FA',
#   'profile_background_image_url': None,
#   'profile_background_image_url_https': None,
#   'profile_background_tile': False,
#   'profile_image_url': 'http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png',
#   'profile_image_url_https': 'https://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png',
#   'profile_link_color': '1DA1F2',
#   'profile_sidebar_border_color': 'C0DEED',
#   'profile_sidebar_fill_color': 'DDEEF6',
#   'profile_text_color': '333333',
#   'profile_use_background_image': True,
#   'protected': False,
#   'screen_name': 'TheMovieFacts_',
#   'statuses_count': 4,
#   'time_zone': None,
#   'translator_type': 'none',
#   'url': None,
#   'utc_offset': None,
#   'verified': False}}
#
