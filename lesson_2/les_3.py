import json
import requests
from bs4 import BeautifulSoup

def get_data(url):
    headers = {
        "user - agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }

    req = requests.get(url, headers)
    print(req.text)

    with open("lesson_3.html", "w") as file:
        file.write(req.text)

    with open("lesson_3.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    articles = soup.find_all("article", class_="mu-store")
    store_urls = []
    for article in articles:
        store_url = "https://backit.me/" + article.find("a").get("href")
        store_urls.append(store_urls)

    shop_data_list = []
    for store_url in store_urls:
        req = requests.get(store_url, headers)
        store_name = store_url.split("/")[+7]

        with open(f"data/{store_name}.html", "w") as file:
            file.write(req.text)

        with open(f"data/{store_name}.html") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")
        shop_data = soup.find("div", class_="mu-store")

        try:
            shop_logo = "https://backit.me/" + shop_data.find("div", class_="shop-logo").find("img").get("src")
        except Exception:
            shop_logo = "No shop logo"
            print(shop_logo)

        try:
            shop_name = shop_data.find("div", class_="shop-logo").find("img").get("alt")
        except Exception:
            shop_name = "No shop name"
            print(shop_name)

        try:
            shop_percent = shop_data.find("span", class_="rate").text.strip()
        except Exception:
            shop_description = "No shop description "

        try:
            shop_condition = shop_data.find("div", class_="shop-markdown").text.split("\n")
        except Exception:
            shop_condition = "No shop condition"

        shop_data_list.append(
            {
                "Название магазина:": shop_name,
                "URL Логотип магазина:": shop_logo,
                "Процент кэшбэка магазина": shop_percent,
                "Условия кэшбэка:": shop_condition,

            }
        )
    with open("data/store_date.json", "a", encoding="utf-8") as file:
        json.dump(shop_data_list, file, indent=4, ensure_ascii=False)


get_data("https://backit.me/ru/cashback/shops/category/1097")