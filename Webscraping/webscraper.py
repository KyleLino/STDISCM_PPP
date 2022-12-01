import requests
import csv
from bs4 import BeautifulSoup

#URL
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

#URL PARSER
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
#print(results.prettify())

#VARIABLES
list_1 = []
list_2 = []
list_3 = []
list_4 = []

#WEB SCRAPING
job_elements = results.find_all("div", class_="card-content") # list length
for job_element in job_elements: # loop
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    date_element = job_element.find("p", class_="is-small has-text-grey")
    print(title_element.text)
    print(company_element.text)
    print(location_element.text)
    print(date_element.text)
    print()
    list_1.append(title_element.text)
    list_2.append(company_element.text)
    list_3.append(location_element.text)
    list_4.append(date_element.text)

#WRITE INTO CSV
with open('dlsu_info.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    list_length = len(list_1)
    for i in range(list_length):
        writer.writerow([list_1[i].strip(), list_2[i].strip(), list_3[i].strip(), list_4[i].strip()])
