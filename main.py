# #Import Selenium
# from selenium import webdriver
# import pandas as pd
# import time
#
# #Writing our First Selenium Python Test
# web = 'https://1xstavka.ru/en/line/Football/1841614-UEFA-European-Championship-2020/' #you can choose any other league (update 1)
# driver = webdriver.Chrome()
# driver.get(web)
#
# #Make ChromeDriver click a button
# time.sleep(5) #add implicit wait, if necessary
#
# #Initialize your storage
# teams = []
# x12 = [] #3-way
# odds_events = []
#
# #scroll down to the bottom to load upcoming matches (update 2: not necessary anymore)
# #driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# #time.sleep(3) #add implicit wait to let the driver load the elements of the upcoming matches section.
#
# #select only upcoming matches box
# box = driver.find_element_by_xpath('//*[@id="games_content"]/div/div[2]/div/div') #update 3
# #Looking for 'sports titles'
# sport_title = box.find_elements_by_class_name('c-events__item')
#
# for sport in sport_title:
#     # selecting only football
#     parent = sport.find_element_by_xpath('//*[@id="games_content"]/div/div[2]/div/div') #immediate parent node
#     #Looking for single row events
#     single_row_events = parent.find_elements_by_class_name('c-events__item c-events__item_col')
#     #Getting data
#     for match in single_row_events:
#         #'odd_events'
#         odds_event = match.find_elements_by_class_name('c-bets')
#         odds_events.append(odds_event)
#         # Team names
#         for team in match.find_elements_by_class_name('c-events__name'):
#             teams.append(team.text)
#     #Getting data: the odds
#     for odds_event in odds_events:
#         for n, box in enumerate(odds_event):
#             rows = box.find_elements_by_xpath('.//*')
#             if n == 0:
#                 x12.append(rows[0].text)
#
# driver.quit()
# #Storing lists within dictionary
# dict_gambling = {'Teams': teams, '1x2': x12}
# #Presenting data in dataframe
# df_gambling = pd.DataFrame.from_dict(dict_gambling)
# print(df_gambling)
#
#

#Import Selenium
import xlwt as xlwt
from selenium import webdriver
import pandas as pd
import time

import xlwt

#Writing our First Selenium Python Test
web = 'https://sports.tipico.de/de/alle/fussball/irland/premier-division?mode=tc' #you can choose any other league (update 1)
driver = webdriver.Chrome()
driver.get(web)

#Initialize your storage
teams = []
x12 = [] #3-way
odds_events = []

#Looking for 'sports titles'
sport_title = driver.find_elements_by_class_name('SportTitle-styles-sport')

for sport in sport_title:
    # selecting only football
    parent = sport.find_element_by_xpath('./..') #immediate parent node

    grandparent = parent.find_element_by_xpath('./..') #grandparent node = the whole 'football' section

    #Looking for single row events
    single_row_events = grandparent.find_elements_by_class_name('EventRow-styles-event-row')

    #Getting data
    for match in single_row_events:
        #'odd_events'
        odds_event = match.find_elements_by_class_name('EventOddGroup-styles-odd-groups')
        odds_events.append(odds_event)
        # Team names
        for team in match.find_elements_by_class_name('EventTeams-styles-titles'):
            teams.append(team.text)

    #Getting data: the odds
    for odds_event in odds_events:
        for n, box in enumerate(odds_event):
            rows = box.find_elements_by_xpath('.//*')
            if n == 0:
                x12.append(rows[0].text)

driver.quit()
#Storing lists within dictionary
dict_gambling = {'Teams': teams, '1x2': x12}
#Presenting data in dataframe
df_gambling = pd.DataFrame.from_dict(dict_gambling)
print(df_gambling)

#
# import xlwt
#
# book = xlwt.Workbook()
#
# # Add a sheet to the workbook
# sheet1 = book.add_sheet("Sheet1")
#
# # The data
# cols = ["A", "B"]
# txt = [teams, x12]
#
# # Loop over the rows and columns and fill in the values
# for num in range(4):
#     row = sheet1.row(num)
#     for index, col in enumerate(cols):
#         value = str(txt[index])
#         row.write(index, value)
# # Save the result
# book.save("test.xls")

file = open('parsing.txt', 'w', encoding='utf-8')
for i in range(len(teams)):
    print(teams[i] + "\n" + x12[i])
    file.write(teams[i] + "\n" + x12[i] + "\n")
file.close()

