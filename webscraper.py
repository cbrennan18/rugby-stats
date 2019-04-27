
import csv
import requests
from bs4 import BeautifulSoup


with open('./links.csv', 'r') as f:
    reader = csv.reader(f)
    lst = list(reader)
    for i in lst:
        url = "http://www.espn.co.uk/rugby/playerstats?gameId=290551&league=270557"
        page = requests.get(url)
        html = page.content
        soup = BeautifulSoup(html, 'html.parser')

        table = soup.find('tbody')

        list_of_rows = []
        for row in table.findAll('tr'):
            list_of_cells = []
            for cell in row.findAll('td'):
                text = cell.text.replace('&nbsp;', '')
                list_of_cells.append(text)
            list_of_rows.append(list_of_cells)

        outfile = open("./test.csv", "w")
        writer = csv.writer(outfile)
        writer.writerow(["Name", "Tries", "Try Assists", "Conversions", "Penalties", "Drop Goals", "Points"])
        writer.writerows(list_of_rows)











