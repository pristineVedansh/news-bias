import os, json, pandas as pd

from selenium import webdriver

chromedriver = "chromedriver.exe"

os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver)
url = 'https://timesofindia.indiatimes.com/topic/bharatiya-janata-party/news/'

timestampCol = ["Published"]
linkCol = ["Link"]
titleCol = ["Title"]
snippetCol = ["Snippet"]


for i in range(1, 10):
    driver.get(url+str(i))
    content = driver.find_elements_by_css_selector('div.content')
    for person in content:
        link = person.find_element_by_xpath('(.//a)').get_attribute('href')
        timestamp = person.find_element_by_xpath('(.//span[@class = "meta"])').get_attribute('rodate')
        title = person.find_element_by_xpath('(.//span[@class = "title"])').text
        snippet = person.find_element_by_xpath('(.//p)').text
        #print(person.text)
        timestampCol.append(timestamp)
        linkCol.append(link)
        titleCol.append(title)
        snippetCol.append(snippet)
        print(timestamp)
        print(link)
        print(title)
        print(snippet)
        print("\n")

    articles = pd.DataFrame()
    timestampCol = pd.Series(timestampCol)
    linkCol = pd.Series(linkCol)
    titleCol = pd.Series(titleCol)
    snippetCol = pd.Series(snippetCol)

    articles['Published'] = timestampCol.values
    articles['Link'] = linkCol.values
    articles['Title'] = titleCol.values
    articles['Snippets'] = snippetCol.values
    articles.to_csv('toi.csv',mode='a', header=False)

    timestampCol = []
    linkCol = []
    titleCol = []
    snippetCol = []
