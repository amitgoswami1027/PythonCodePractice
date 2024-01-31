from bs4 import BeautifulSoup
import lxml

with open("C:\Storage\AmitGoswami\Github\PythonCodePractice\WebDevelopment\Beautiful_Soup\website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "lxml")
print(soup.title)

all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)




