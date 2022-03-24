import pandas as pd
from paginas import clasipar
from paginas import hendyla
from paginas import facebook
from paginas import instagram
from article import make_article_list
from user import get_user_info
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(executable_path="driver\\chromedriver.exe")


article_list = []
make_article_list(article_list)
user_info = get_user_info()
facebook.post(browser,user_info,article_list)
clasipar.post(browser,user_info,article_list)
hendyla.post(browser,user_info,article_list)
instagram.post(user_info,article_list)