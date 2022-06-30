import requests
import json
import datetime
import urllib.parse

#todo 引数で受け取れるようにする
cookie = {"connect.sid": "s%3A0vNTbCxCKgn_EyGUUv_HtAbYdXS8OUAY.uK7cVPvif%2FtTTsAh9PWmW3F21xaGydXaVCOGqAL81Bg"}

# 自分のuser情報を取得
my_url  = "https://scrapbox.io/api/users/me"
my_res  = requests.get(my_url, cookies= cookie).json()
my_id   = my_res["id"]
my_name = my_res["name"]
url = "https://scrapbox.io/api/pages/netprotections/search/titles"

r  = requests.get(url, cookies= cookie)
following_id = r.headers["X-Following-Id"]

#例えば、「Scrapbox」のリンクがあるページを取得するならこう
no = 0
for res in r.json():
#	if "Scrapbox" in res["links"]:
#		result = res["title"] + " 最終更新: " + str(datetime.datetime.fromtimestamp(res["updated"])) 
#		print(result)
	print(no)
	no += 1

# todo 引数で時間指定できるとBetter
number = 1
while number < 100:
	next_url = "https://scrapbox.io/api/pages/netprotections/search/titles?followingId=" + str(following_id)
#	print(next_url)
	next_res  = requests.get(next_url, cookies= cookie)
	for resp in next_res.json():
		if "Scrapbox" in resp["links"]:
			print(resp["title"])
#			print(datetime.datetime.fromtimestamp(resp["updated"]))

			quote        = urllib.parse.quote(resp["title"]).replace('/', '%2F')
			title_url    = "https://scrapbox.io/api/pages/netprotections/" + str(quote)
			print(title_url)
			page_content = requests.get(title_url, cookies= cookie).json()
			list = []
			for collab in  page_content["collaborators"]:
				list.append(collab["name"])

			if page_content["user"]["name"] == my_name:
				print(page_content["title"])
			elif my_name in list:
				print(page_content["title"])
#			print(str(all_res.json()["user"]))
#			print(str(all_res.json()["collaborators"]))
	next_id = next_res.headers["X-Following-Id"]
	following_id = next_id
	number += 1
	print(number)

#json = r.json()
#pages = json["pages"]
#for page in pages:
#	if page["user"]["id"] == my_id:
#		title = page["title"]
#		created_at = datetime.datetime.fromtimestamp(page["created"])
#		print(title)
#		print(created_at)
