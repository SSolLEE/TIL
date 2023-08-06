# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup

def main():
    # index.html을 불러와서 BeautifulSoup 객체 초기화
    soup = BeautifulSoup(open("html/index.html", encoding="utf-8"), "html.parser")
    # print(type(soup))
    # print(soup.title)
    # print(soup.find("title"))
    story2_str = soup.find('div', class_ = "story2").find_all('p')
    print(story2_str[1].get_text())

if __name__ == "__main__":
    main()