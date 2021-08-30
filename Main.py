from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("/Users/apoorvelous/Downloads/chromedriver")
browser.get(START_URL)
time.sleep(10)
def scrape():
    headers = ["Name", "Distance", "Mass", "Radius"]
    planet_data = []
    for i in range(0, 428):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul"):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
            new_planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

final_planet_data = []

def scrape_more_data(hyperLink):
    page = requests.get(hyperLink)
    soup = BeautifulSoup(page.content, "htmp.parser")
    for tr_tag in soup.find("tr", attrs = {"class":"fact_row"}):
        td_tags = tr_tag.find_all("td")
        temp_list = []
        for td_tag in td_tags:
            try:
                temp_list.append(td_tag.find_all("div",attrs = {"class": "value"})[0].contents[0])
            except:
                temp_list.append("")
            new_planet_data.append(temp_list)

scrape()
for data in planet_data:
    scrape_more_data(data[5])

final_planet_data = []

for index, data in enumerate(planet_data):
    final_planet_data.append(data+ final_planet_data[index])

with open("final.csv","w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(final_planet_data)

    
with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrape()

df = df[df['column_name'].notna()]

data = []
with open("dataset_2.csv", "r") as f:
 csvreader = csv.reader(f)
 for row in csvreader:
  data.append(row)
headers = data[0]
planet_data = data[1:]

for data_point in planet_data:
 data_point[2] = data_point[2].lower()

planet_data.sort(key=lambda planet_data: planet_data[2])
with open("dataset_2_sorted.csv", "a+") as f:
 csvwriter = csv.writer(f)
 csvwriter.writerow(headers)
 csvwriter.writerows(planet_data)

 dataset_1 = []
dataset_2 = []
with open("dataset_1.csv", "r") as f:
 csvreader = csv.reader(f)
 for row in csvreader:
  dataset_1.append(row)
  with open("dataset_2_sorted.csv", "r") as f:
   csvreader = csv.reader(f)
   for row in csvreader:
    dataset_2.append(row)
    headers_1 = dataset_1[0]
    planet_data_1 = dataset_1[1:]
    headers_2 = dataset_2[0]
    planet_data_2 = dataset_2[1:]
    headers = headers_1 + headers_2
    planet_data = []
    for index, data_row in enumerate(planet_data_1):
        planet_data.append(planet_data_1[index] + planet_data_2[index])
        with open("final.csv", "a+") as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(headers)
            csvwriter.writerows(planet_data)

        import pandas as pd

        df = pd.read_csv('total_stars.csv')
        df.columns

        df.drop(['Unnamed: 0','Unnamed: 6', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1','Luminosity'],axis=1,inplace=True)
        final_data = df.dropna()
        final_data.reset_index(drop=True,inplace = True)
        final_data.to_csv('final_data.csv')

        import csv
        import plotly_express as px 

rows = []

with open("final.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)

headers = rows[0]
planet_data_rows = rows[1:]
print(headers)
print(planet_data_rows[0])

planet_masses = []
planet_radiuses = []
planet_names = []
for planet_data in planet_data_rows:
  planet_masses.append(planet_data[3])
  planet_radiuses.append(planet_data[7])
  planet_names.append(planet_data[1])
planet_gravity = []
for index, name in enumerate(planet_names):
  gravity = (float(planet_masses[index])*5.972e+24) / (float(planet_radiuses[index])*float(planet_radiuses[index])*6371000*6371000) * 6.674e-11
  planet_gravity.append(gravity)

fig = px.scatter(x=planet_radiuses, y=planet_masses, size=planet_gravity, hover_data=[planet_names])
fig.show()

low_gravity_planets = []
for index, gravity in enumerate(planet_gravity):
  if gravity < 10:
    low_gravity_planets.append(planet_data_rows[index])

print(len(low_gravity_planets))

planet_masses = []
planet_radiuses = []
for planet_data in low_gravity_planets:
  planet_masses.append(planet_data[3])
  planet_radiuses.append(planet_data[7])

fig = px.scatter(x=planet_radiuses, y=planet_masses)
fig.show()

fig = px.scatter(x=planet_gravity, y=planet_masses)
fig.show()

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
X = []
for index, planet_mass in enumerate(planet_masses):
 temp_list = [
planet_radiuses[index],
planet_mass
]
X.append(temp_list)
wcss = []
for i in range(1, 11):
 kmeans = KMeans(n_clusters=i, init='k-means++', random_state = 42)
kmeans.fit(X)
# inertia method returns wcss for that model
wcss.append(kmeans.inertia_)
plt.figure(figsize=(10,5))
sns.lineplot(range(1, 11), wcss, marker='o', color='red')

goldilock_planets = list(suitable_planets) 

temp_goldilock_planets = list(suitable_planets)
for planet_data in temp_goldilock_planets:
 if planet_data[8] < 0.38 or planet_data[8] > 2:
  goldilock_planets.remove(planet_data)

 print(len(suitable_planets))
 print(len(goldilock_planets))

 final_dict = {}
for index, planet_data in enumerate(planet_data_rows):
 features_list = []
 gravity = (float(planet_data[3])*5.972e+24)/(float(planet_data[7])*float(planet_data[7])*6371000*6371000) *6.674e-11
try:
  if gravity < 100:
       features_list.append("gravity")
except: pass



