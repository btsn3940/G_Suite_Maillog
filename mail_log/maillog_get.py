# Selenium + Python + Chrome
#
# Google Adminの「メールログ検索」にてログを取得するスクリプト

# 必要なライブラリのインポートを行う
import sys
import time
from datetime import datetime, date, timedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# コマンドラインからの引数を拾う
args = sys.argv

# 初期値作成
login_id = "(your gmail address)"
password = "(your gmail password)"
# 初期値作成（時間部分）
today = datetime.today()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
today_str = datetime.strftime(today, '%Y/%m/%d')
tomorrow_str = datetime.strftime(tomorrow, '%Y/%m/%d')
yesterday_str = datetime.strftime(yesterday, '%Y/%m/%d')

# Chrome用のWebDriverインスタンスを作成し認証画面を開く
# （ここでは c:\driver\chromedriver.exe で配置するものとします）
driver = webdriver.Chrome("c:/driver/chromedriver.exe")
driver.get('https://accounts.google.com')

# 以下の要素名はGoogle側の仕様で変更される場合がある為、メールログを抽出出来ない場合
# コマンドプロンプト上から当pythonを直接実行しどの要素名で引っかかっているか確認する。

# 認証部分
time.sleep(2)
driver.find_element_by_xpath("//*[@id='identifierId']").send_keys(login_id)
driver.find_element_by_xpath("//*[@id='identifierNext']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@class='whsOnd zHQkBf']").send_keys(password)
driver.find_element_by_xpath("//*[@id='passwordNext']").click()

# G Suite管理ページへの遷移
time.sleep(3)
driver.get('https://admin.google.com')
time.sleep(3)
driver.get('https://admin.google.com/AdminHome?pli=1&fral=1')
time.sleep(3)
driver.get('https://admin.google.com/AdminHome?pli=1&fral=1#Reports:subtab=email-log-search')

# 「メールログ検索」ページにて必要な値を選択しログを抽出する
time.sleep(10)
for i in range(0, 11):
    driver.find_element_by_tag_name("body").send_keys(Keys.TAB)

time.sleep(1)
elem = driver.find_element_by_class_name("goog-button-base-content")
elem.click()

time.sleep(1)
driver.find_element_by_xpath("//*[@id='gwt-uid-1632']").click()

for i in range(0, 46):
    driver.find_element_by_tag_name("body").send_keys(Keys.TAB)

time.sleep(1)
if args[1] == '1':
    driver.find_element_by_xpath("//*[@class='inline']/input[1]").send_keys(today_str + " 2:00")
elif args[1] == '2':
    driver.find_element_by_xpath("//*[@class='inline']/input[1]").send_keys(today_str + " 10:00")
elif args[1] == '3':
    driver.find_element_by_xpath("//*[@class='inline']/input[1]").send_keys(yesterday_str + " 16:00")

time.sleep(1)
driver.find_element_by_xpath("//*[@class='inline']/input[1]").send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element_by_tag_name("body").send_keys(Keys.TAB)
time.sleep(1)
if args[1] == '1':
    driver.find_element_by_xpath("//*[@class='inline']/input[2]").send_keys(today_str + " 10:00")
elif args[1] == '2':
    driver.find_element_by_xpath("//*[@class='inline']/input[2]").send_keys(today_str + " 16:00")
elif args[1] == '3':
    driver.find_element_by_xpath("//*[@class='inline']/input[2]").send_keys(today_str + " 2:00")
time.sleep(1)
driver.find_element_by_xpath("//*[@class='inline']/input[2]").send_keys(Keys.ENTER)

time.sleep(1)
elem = driver.find_element_by_class_name("KIOVIAD-fd-m")
elem.click()

# csvファイルをローカルにダウンロードする
time.sleep(10)
driver.find_element_by_xpath("//*[@class='html-face']/img").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@class='popupContent']/div/div/div[2]").click()

# 終了
time.sleep(15)
driver.close()