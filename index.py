# import urllib2
# import json



# locu_api = 'f4d783350e841a5a8e35966fd7f898f1d3213b98'

# url ='https://api.locu.com/v1_0/venue/search/?api_key='
# json_obj = urllib2.urlopen(url)

# locality = 'name=restaurants&locality=chicago'

# def locu_search(query):
#     api_key = locu_api
#     url = 'https://api.locu.com/v1_0/venue/search/?api_key=' + api_key
#     locality = query.replace('',"%20")
#     final_url = url + "&locality=" + locality + "name=restaurants"
#     json_obj = irllib2.urlopen(final_url)
#     date = json.load(json_obj)

# for item in data['objects']:
#     print item['name']
#     print item['locality']
#     print item['phone']


