from bs4 import BeautifulSoup


with open ("blank/index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

#title = soup.title
#print(title)
#print(title.text)
#print(title.string)

# .find()  .find_all()
#page_h1 = soup.find("h1")
#print(page_h1)

#page_all_h1 = soup.find_all("h1")
#print(page_all_h1)

#for item in page_all_h1:
#    print(item.text)

#user_name = soup.find("div", class_="user__name")
#print(user_name.text.strip())

#user_name = soup.find("div", class_="user__name").find("span").text
#print(user_name)

#user_name = soup.find("div", {"class": "user__name", "id": "iii"}).find("span").text
#print(user_name)

#find_all_spans_in_user_info = soup.find(class_="user__info").find_all("span")
#print(find_all_spans_in_user_info)

#for item in find_all_spans_in_user_info:
#    print(item.text)

#print(find_all_spans_in_user_info[0])
#print(find_all_spans_in_user_info[0].text)

