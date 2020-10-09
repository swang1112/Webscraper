from bs4 import BeautifulSoup
import pandas as pd
import webbot

my_url = "https://alternative.me/crypto/fear-and-greed-index/"
my_web = webbot.Browser()
my_web.go_to(my_url)

# crawler
page = my_web.get_page_source()
soup = BeautifulSoup(page, "html.parser")