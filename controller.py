import requests
import logging
from bs4 import BeautifulSoup
from plant import Plant
from csv_ import CSV

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

plants = []

# To Do
# for each page
# for num in range(1,449):
response = requests.get('https://www.monrovia.com/plant-catalog/search/?start_page=14')
soup = BeautifulSoup(response.text, 'html.parser')

# Go through each link on page and create a plant object
# Add plant to plant list
plant_links = soup.find_all(class_='list-plant')
for i in range(0,len(plant_links)):
  link = plant_links[i].find('a')['href']

  logging.debug(i)
  logging.debug('Link: ' + link)
# plant = Plant()
  plant = Plant(link)
  plants.append(plant)

# Create CSV with plant data
logging.debug('Plant data')
logging.debug(plants)
new_csv = CSV(plants, 'test.csv')
