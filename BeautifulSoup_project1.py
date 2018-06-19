# -*- coding: utf-8 -*-
import requests
import bs4
import os
import time

# 対象のURL
url = "https://downloads.khinsider.com/game-soundtracks/album/7th-dragon"

# URLの情報を取得
r = requests.get(url)
soup = bs4.BeautifulSoup(r.content)

# imgタグを取得
tag = soup.select('a[href*="/game-soundtracks/album/7th-dragon"]')
#tag = soup.find_all("a", class_="link", href="/link")
media_urls = [item.get('href') for item in tag]

# カレントディレクトリを設定
os.chdir("./download2")
print os.getcwd()

# ダウンロード開始
index = 0
for i in range(9/3):    
    # ファイル情報読み取り
    file_name = media_urls[index].split("/")[-1]
    inner_r = requests.get(url+"/"+file_name)
    inner_soup = bs4.BeautifulSoup(inner_r.content)
    inner_tag = inner_soup.select('a[style*="color"]')
    download_url = [item.get('href') for item in inner_tag][0]
    print download_url
    download_r = requests.get(download_url)
    
    # ファイルの保存
    if download_r.status_code == 200:
        print "begin download"
        f = open(file_name, 'w')
        f.write(download_r.content)
        f.close()
    
    index += 3
