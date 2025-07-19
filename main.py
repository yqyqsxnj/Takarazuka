import time
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

cardset = "https://shop.tca-pictures.net/shop/g/g0401260020072/"
poster_card = "https://shop.tca-pictures.net/shop/g/g0401260020058/"

def check_stock():
    url = cardset
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    buy_btn = soup.select_one("button.block-add-cart--btn")
    return buy_btn is not None  # 如果有“加入购物车”按钮就代表有货

def send_email():
    msg = MIMEText("商品有货啦！点击查看：https://shop.tca-pictures.net/shop/g/g0401260020058/")
    msg["Subject"] = "商品补货提醒"
    msg["From"] = "qsx.yqy.nj@gmail.com"
    msg["To"] = "qsx.yqy.nj@gmail.com"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("qsx.yqy.nj@gmail.com", "soos vume cmtt vilo")
        server.send_message(msg)

while True:
    try:
        if check_stock():
            send_email()
            break  # 发送一次就结束；如要持续提醒可以移除
        print("Still out of stock...")
    except Exception as e:
        print("Error:", e)

    time.sleep(300)  # 每5分钟检查一次
