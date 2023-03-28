import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = "mirvaliyevsunnat@gmail.com"
MY_PASSWORD = "bkqkhmxfnsrgvkox"

amazon_url = "https://www.amazon.com/dp/B07XHQKM6W/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0"

web_age_header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "en-RU,en;q=0.9"
}

amazon_page = requests.get(url=amazon_url, headers=web_age_header )
website_html = amazon_page.text

soup = BeautifulSoup(website_html, "lxml")
product_price = soup.select(".a-span12 span .a-offscreen")
price_as_float = float(product_price[0].getText().split("$")[1])
print((price_as_float))

product_title = soup.find(name="span", class_="a-size-large product-title-word-break")
product_title_string = str(product_title.getText().strip())
print(product_title_string)

if price_as_float <= 40:
    connection = smtplib.SMTP_SSL("smtp.gmail.com")
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="hayrullamirvaliyev@gmail.com",
        msg=f"Subject: Amazon price alert\n\n Headline: AROMA 12-Cup (Cooked) Digital Rice & Grain Multicooker (ARC-966BD) is now ${price_as_float}"
    )
    connection.close()
