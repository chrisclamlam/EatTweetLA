from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

auth = Oauth1Authenticator(
    consumer_key="wzUhnPsbgmWx5cNjvKfBig",
    consumer_secret="pLiVA3od4VGARO-gbU8IxhrMyF4",
    token="xgf3E37cDhgJR8Zmn6kdixGp8dObGbdz",
    token_secret="ydb-LoTSmNFvnIXn9i4KlB3c988"
	)

client = Client(auth)

	#userinput = raw_input("wats da move?    ")

params = {
    'term': 'food',
    'lang': 'en',
}

j= client.search_by_coordinates(34.052235, -118.243683, **params)

import random
number=random.randrange(0,10)
	#print number
result = "Hey! You should check out " + j.businesses[number].name + (" at ") + j.businesses[number].mobile_url


from TwitterAPI import TwitterAPI
api = TwitterAPI("szCuah1wTiHrykp9XO8TFtMig", "zqcj1gqktW9eIbmDFai3kkjYQxr1JMIb67KhoMyQ2i3zPQDFVj", "831393767164764160-u3bVfMq0qEqJVj1P71ZqMLtv4xCxLWx", "UqOZUsNBen2kcQZXxxn2Mz0jzqvBwklZhhqYzJwjiJ5ep")

r = api.request('user')
for item in r.get_iterator():
	if 'text' in item and item['user']['id'] != 831393767164764160:
		resp = '@' + item['user']['screen_name'] + " " + result
		r = api.request('statuses/update', {'status': resp, "in_reply_to_status_id":item['id']})
	print(r.status_code)


