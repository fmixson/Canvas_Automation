from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import lxml
import requests

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get('C:/Users/family/Desktop/Dashboard.html')
element = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, 'screenreader-only')))
page_source = driver.page_source
# page = requests.get('C:/Users/family/Desktop/Dashboard.html')
soup = BeautifulSoup(page_source, 'lxml')
tag = soup.body.h2
dashboard = soup.find('div', {'class', 'ic-DashboardCard__box__container'})
term = dashboard.find_all('div', {'class', 'ic-DashboardCard__header-term ellipsis', 'title='''})
canvas_courses = []
for dash in dashboard:
    # print(dash)
    # print()
    term = dash.find('div', {'class', 'ic-DashboardCard__header-term ellipsis', 'title='''})
    course = dash.find('a', {'class', 'ic-DashboardCard__link external'})
    print(term)
    print(course)
    print()
    # # print(term)
    # if '2021 Fall' in term:
    #     # print('in term')
    #     canvas_courses.append(dash)
    #     print(canvas_courses)
    # print()
# print(term)
# print(dashboard)
# print(type(term))
# print(len(term))
# canvas_courses = []
# for t in term:
#     print(t)
#     term = t.get_text(strip=True)
#     print(term)
#     if term == '2021 Fall':
#         canvas_courses.append(t)
# print(canvas_courses)



#
# for dash in dashboard:
#     print(dash)
#     print()

# # dashboard = soup.find_all('div', {'id': 'DashboardCard_Container'})
# cards = soup.find_all('a', {'class': 'ic-DashboardCard__link external'})
# print(dashboard)
# card_count = 1
# card_list = []
# print(len(cards))
# card_count = 1
# for card in cards:
#     string_card = str(card)
#     split_string_card = string_card.split()
#     print(split_string_card)
#     print(len(split_string_card))
#     for item in split_string_card:
#         print(item)
#         print(card_count)
#         if 'title="2017' in item:
#             print('2017')
#             # // *[ @ id = "DashboardCard_Container"] / div / div[1] / h2
#             # // *[ @ id = "DashboardCard_Container"] / div / div[2] / div / div[1] / div / a / div / div[1]
#             click_on_course = driver.find_element(By.XPATH, '//*[@id="DashboardCard_Container"]/div/div[1]/ div/ div[' + str(card_count) + ']/div/a').click()
#             element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'dialog_for_help_134')))
#     card_count += 1
#
#     # print(split_string_card)
#     print()
# #
# #     card_list.append(card)
# # for card in cards2:
# #     print(card)
#     print()

# for card in card_list:
#     print(card)
#     print(type(card))

