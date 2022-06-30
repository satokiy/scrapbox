import requests
import json
import datetime
import urllib.parse
import sys

#引数に自分のCookieを指定する
my_cookie = sys.argv[1]
cookie  = {"connect.sid": my_cookie }

# 自分のuser情報を取得
my_url  = "https://scrapbox.io/api/users/me"
my_res  = requests.get(my_url, cookies= cookie).json()
my_id   = my_res["id"]
my_name = my_res["name"]

# 最初の1,000件を取得
url          = "https://scrapbox.io/api/pages/netprotections/search/titles"
r            = requests.get(url, cookies= cookie)
following_id = r.headers["X-Following-Id"]

for res in r.json():
	quote        = urllib.parse.quote(res["title"]).replace('/', '%2F')
	title_url    = "https://scrapbox.io/api/pages/netprotections/" + str(quote)
	page_content = requests.get(title_url, cookies= cookie).json()
	list = []
	for collab in  page_content["collaborators"]:
		if "name" in collab:
			list.append(collab["name"])
	if "name" in page_content["user"] and page_content["user"]["name"] == my_name:
		print(str(datetime.datetime.fromtimestamp(page_content["updated"])))
		print(page_content["title"])
	elif my_name in list:
		print(page_content["title"])
		print(str(datetime.datetime.fromtimestamp(page_content["updated"])))

# 例えば、「Scrapbox」のリンクがあるページを取得するならこう
#for res in r.json():
#        if "Scrapbox" in res["links"]:
#               result = res["title"] + " 最終更新: " + str(datetime.datetime.fromtimestamp(res["updated"]))
#               print(result)

# 1,001件目からループ
# todo 引数で指定できるとBetter
number = 1
while number < 100:
	next_url = "https://scrapbox.io/api/pages/netprotections/search/titles?followingId=" + str(following_id)
	next_res  = requests.get(next_url, cookies= cookie)
	for resp in next_res.json():
		quote        = urllib.parse.quote(resp["title"]).replace('/', '%2F')
		title_url    = "https://scrapbox.io/api/pages/netprotections/" + str(quote)
		page_content = requests.get(title_url, cookies= cookie).json()
		list = []
		#print(page_content["title"])
		for collab in  page_content["collaborators"]:
			if "name" in collab:
				list.append(collab["name"])
		if "name" in page_content["user"] and page_content["user"]["name"] == my_name:
			print(str(datetime.datetime.fromtimestamp(page_content["updated"])))
			print(page_content["title"])
		elif my_name in list:
			print(page_content["title"])
			print(str(datetime.datetime.fromtimestamp(page_content["updated"])))
	
	next_id      = next_res.headers["X-Following-Id"]
	following_id = next_id
	number      += 1
	now          = str(number * 1000) + "件目まで取得完了"
	print(now)
