
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep
import warnings
warnings.filterwarnings("ignore")

from dotenv import load_dotenv
load_dotenv()

os.environ['EMAIL'] = 'yousefeldaly23@gmail.com'
os.environ['PASSWORD'] = '#0141922425HHeeyy'


driver = webdriver.Chrome()
driver.get('https://www.linkedin.com/login')
print(driver.title)


email = driver.find_element(By.ID, 'username')
email.send_keys(os.environ['EMAIL'])

password = driver.find_element(By.ID, 'password')
password.send_keys(os.environ['PASSWORD'])

password.submit()

url = "https://www.linkedin.com/in/laxmimerit"
driver.get(url)

profile_data = {}

print(driver.title)

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')

name = soup.find('h1', {'class': 'text-heading-xlarge inline t-24 v-align-middle break-words'})

name = name.get_text().strip()

profile_data['name'] = name
profile_data['url'] = url

print(profile_data)