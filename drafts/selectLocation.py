import urllib2
import requests
import json


url = 'http://bigbasket.com/choose-city/'

client = requests.session()
client.get(url)

print client.cookies.get_dict()

csrftoken = client.cookies['csrftoken']
sessionid = client.cookies['sessionid']
_bb_ftvid = client.cookies['_bb_ftvid']
_bb_pop = client.cookies['_bb_pop']
_bb_rd = client.cookies['_bb_rd']
_bb_rdt = client.cookies['_bb_rdt']
_bb_tc = client.cookies['_bb_tc']
_bb_vid = client.cookies['_bb_vid']
_ga = 'GA1.2.1570234640.1448914023'
_gat = 1


headers = dict()
headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
headers['Accept-Encoding'] = 'gzip, deflate'
headers['Accept-Language'] = 'en-US,en;q=0.8,ru;q=0.6,hi;q=0.4'
headers['Cache-Control'] = 'max-age=0'
headers['Connection'] = 'keep-alive'
headers['Content-Type'] = 'application/x-www-form-urlencoded'
headers['Cookie'] = '_bb_ftvid=%s; _bb_pop=%s; _bb_vid=%s; _bb_tc=%s; _bb_rdt=%s; csrftoken=%s; _ga=%s; _gat=%s; sessionid=%s; _bb_rd=%s' %(_bb_ftvid,_bb_pop, _bb_vid, _bb_tc, _bb_rdt, csrftoken, _ga, _gat, sessionid, _bb_rd)
headers['Host'] = 'bigbasket.com'
headers['Origin'] = 'http://bigbasket.com'
headers['Referer'] = 'http://bigbasket.com/choose-city/'
headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'

print headers

data = dict()
data['csrfmiddlewaretoken'] = csrftoken
data['address_id'] = ''
data['places'] = {"city":3,"display_name":"Gachibowli","name":"gachibowli","hub":4,"area":152,"pincode":"500032","area_location":[17.4400802,78.3489168],"city_name":"Hyderabad","pincode_location":[17.4359437,78.3416731]}
data['city_id'] = 3
data['next'] = '/'

print data

r = requests.post(url, data=json.dumps(data), headers=headers)
print r.content
