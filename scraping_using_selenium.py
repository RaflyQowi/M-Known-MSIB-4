from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

website = 'https://www.adamchoi.co.uk/btts/detailed'
path = '/chrome driver/chromedriver'

driver = webdriver.Chrome(path)
driver.get(website)

driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]').click()
matches = driver.find_elements(By.TAG_NAME, 'tr')

date = []
home_team = []
score = []
away_team =[]

for match in matches:
    date.append(match.find_element(By.XPATH,'./td[1]').text)
    home_team.append(match.find_element(By.XPATH,'./td[2]').text)
    score.append(match.find_element(By.XPATH,'./td[3]').text)
    away_team.append(match.find_element(By.XPATH,'./td[4]').text)
driver.quit()

df = pd.DataFrame({'date':date, 'home_team':home_team, 'score':score, 'away_team':away_team})
print(df.head())
