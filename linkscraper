from bs4 import BeautifulSoup
import requests
import csv
from selenium import webdriver

match_links = []
final = []
results = []

sub = 'gameId='
n = 2016

while n < 2017:
    n += 1
    match_links.append(n)
rows = list(match_links)
for i in rows:  # Number of pages plus one
    url = 'http://www.espn.co.uk/rugby/results/_/team/25925/season/{}'.format(i)
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")

    urls = soup.find_all('a', href=True)
    list_of_rows = []
    for link in urls:
        list_of_rows.append(link['href'])

    style = [s for s in list_of_rows if sub.lower() in s.lower()]
    style = set(style)
    style = list(style)
    start = 'http://www.espn.co.uk'
    full = [start + x for x in style]
    full.sort()
    a = [item.replace('report', 'playerstats').replace('match', 'playerstats') for item in full]
    final.append(a)

outfile = open("./links.csv", "w", newline='')
writer = csv.writer(outfile)
writer.writerows(final)

outfile.close()

x = 0
outfile = open("./test.csv", "w", newline='')
writer = csv.writer(outfile)
writer.writerow(["Name", "Tries", "Try Assists", "Conversions", "Penalties", "Drop Goals", "Points",
                 "Kick", "Pass", "Run", "Metres", "Clean Breaks", "Defenders Beaten", "Offloads", "Lineouts Stolen",
                 "Turnovers", "Tackles", "Missed Tackles", "Lineouts Won",
                 "Penalties", "Yellows", "Reds"])
with open('./links.csv') as f:
    reader = csv.reader(f)
    for rec in reader:
        while x < len(rec):

            print(rec[x])

            driver = webdriver.Chrome(executable_path="/Users/ciaranbrennan/Documents/DevTools/chromedriver")
            driver.get(rec[x])
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            list_of_rows = []
            table_scoring = soup.find_all('thead')
            for row in soup.find_all('tr'):
                list_of_cells = []
                for cell in row.find_all('td'):
                    text = cell.text.replace('&nbsp;', '')
                    list_of_cells.append(text)
                list_of_rows.append(list_of_cells)
            writer.writerows(list_of_rows)
            print(list_of_rows)

            driver.execute_script("window.scrollTo(0, 380)")

            xpath_attacking = '//*[@id="main-container"]/div/div[2]/div[1]/div[1]/div[1]/ul/li[2]/span'
            driver.find_element_by_xpath(xpath_attacking).click()

            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            list_of_rows = []
            table_attacking = soup.find_all('thead')
            for row in soup.find_all('tr'):
                list_of_cells = []
                for cell in row.find_all('td'):
                    text = cell.text.replace('&nbsp;', '')
                    list_of_cells.append(text)
                list_of_rows.append(list_of_cells)
            writer.writerows(list_of_rows)
            print(list_of_rows)
            xpath_defending = '//*[@id="main-container"]/div/div[2]/div[1]/div[1]/div[1]/ul/li[3]/span'
            driver.find_element_by_xpath(xpath_defending).click()

            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            list_of_rows = []
            table_defending = soup.find_all('thead')
            for row in soup.find_all('tr'):
                list_of_cells = []
                for cell in row.find_all('td'):
                    text = cell.text.replace('&nbsp;', '')
                    list_of_cells.append(text)
                list_of_rows.append(list_of_cells)
            writer.writerows(list_of_rows)
            print(list_of_rows)
            xpath_discipline = '//*[@id="main-container"]/div/div[2]/div[1]/div[1]/div[1]/ul/li[4]/span'
            driver.find_element_by_xpath(xpath_discipline).click()

            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            list_of_rows = []
            table_discipline = soup.find_all('thead')
            for row in soup.find_all('tr'):
                list_of_cells = []
                for cell in row.find_all('td'):
                    text = cell.text.replace('&nbsp;', '')
                    list_of_cells.append(text)
                list_of_rows.append(list_of_cells)
            writer.writerows(list_of_rows)
            print(list_of_rows)

            x += 1
