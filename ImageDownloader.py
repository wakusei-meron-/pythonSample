# パッケージのimport
import os
import sys
import re
import urllib2


# 変数
url      = "WebページのURL"				# WebページのURL
title    = ""						# Webページのタイトル
img_tag  = []						# imgタグのリスト
img_url  = []						# 画像URLのリスト
img_path = os.getcwd() + "/downloads"			# ダウンロードした画像の保存パス

# 正規表現
pat_title  = re.compile('<title>(.*?)</title>')		# ページタイトルを抜き出す
pat_a1     = re.compile('<a[\s]*href[\s]*=.*?>')	# aタグを抜き出す
pat_a2     = re.compile('href[\s]*="(.*?)"')		# URL先を抜き出す
pat_img1   = re.compile('<img[\s]*src[\s]*=.*?>')	# imgタグを抜き出す
pat_img2   = re.compile('src[\s]*="(.*?)"')		# 画像元URLを抜き出す
pat_img3   = re.compile('.+/(.*)')			# 画像ファイル名をURLから決定
img_format = [".jpg", ".png", ".gif", ".bmp"]		# 画像ファイル形式

# 関数定義
# 画像をダウンロードする関数
def image_download(url, output):
	opener = urllib2.build_opener()
	req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
	img_file = open(output, 'wb')
	img_file.write(opener.open(req).read())
	img_file.close()



"""
これ以降はHTMLページの取得画像のダウンロード処理
"""

# HTMLページを取得しリストに格納
req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
con = urllib2.urlopen(req)
html = con.read()

# ページタイトルを取得
m = pat_title.search(html)
title = m.group(1)

# 画像をダウンロードするディレクトリ名
dl_path = img_path + "/" + title

# ページタイトルと同名のディレクトリを作成する
if not os.path.exists(dl_path):
	os.makedirs(dl_path)

# ディレクトリ権限の変更
os.chmod(img_path, 0777)
os.chmod(dl_path, 0777)

# 正規表現を利用してaタグ, imgタグを抜き出してリストに格納
a_tag   = pat_a1.findall(html)
img_tag = pat_img1.findall(html)

# aタグのリストから画像のURLを抜き出す
for i in a_tag:
	# URLを抜き出す
	m = pat_a2.search(i)

	# 取得オブジェクトがNoneでない場合に処理を行う
	if not m is None:
		# URLの取得
		tmp = m.group(1)

		# 画像フォーマットが一致すればリストに追加
		for j in img_format:
			if tmp.find(j) > -1:
				img_url.append(tmp)
				break


# imgタグのリストから画像のURLを抜き出す
for i in img_tag:
	# URLを抜き出す
	m = pat_img2.search(i)

	# 取得オブジェクトがNoneでない場合に処理を行う
	if not m is None:
		tmp = m.group(1)

		# 画像フォーマットが一致すればリストに追加
		for j in img_format:
			if tmp.find(j) > -1:
				img_url.append(tmp)
				break


# 画像URLのリストから実際の画像をダウンロードする
for i in img_url:
	# 画像ファイル名を決定
	m = pat_img3.search(i)
	name = m.group(1)
	output = dl_path + "/" + name

	# 画像のダウンロード
	image_download(i, output)
