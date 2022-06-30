require 'net/http'
require 'uri'
require 'json'
require 'logger'

#logger = Logger.new('./iget_scrap.log')


cookie = {"connect.sid": "s%3A0vNTbCxCKgn_EyGUUv_HtAbYdXS8OUAY.uK7cVPvif%2FtTTsAh9PWmW3F21xaGydXaVCOGqAL81Bg"}

#cookie = "connect.sid="s%3A0vNTbCxCKgn_EyGUUv_HtAbYdXS8OUAY.uK7cVPvif%2FtTTsAh9PWmW3F21xaGydXaVCOGqAL81B""
url = URI.parse("https://scrapbox.io/api/pages/netprotections/search/titles")

#data = {headers: {
#		'Cookie' => cookie
#	}}
https = Net::HTTP.new(url.host, url.port)
# httpsで通信する場合、use_sslをtrueにする
https.use_ssl = true
# 3.リクエストを作成する
req = Net::HTTP::Get.new(url.path)
req["Cookie"] = cookie
# 4.リクエストを投げる/レスポンスを受け取る
res = https.request(req)
# 5.データを変換する
hash = JSON.parse(res.body)
# 結果を出力
puts hash
