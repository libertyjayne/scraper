import requests
from bs4 import BeautifulSoup
from csv import writer
# Mock data
from plant_html import html_doc

class Plant:
  def __init__(self):
  # response = requests.get(link)
    self.soup = BeautifulSoup(html_doc, 'html.parser')
    self.data = self.set_data()
    self.headers = self.set_headers()

  def set_headers(self):
    headers = []
    for key in self.data:
      headers.append(key)
    return headers

  def set_data(self):
    # Page Header Info
    data = {}
    data['Common Name'] = self.soup.find(class_='page-title').get_text().strip()
    data['Scientific Name'] = self.soup.find(class_='info-main').contents[3].get_text().strip()
    data['Light'] = self.soup.find(class_='plan-modal-trigger').get_text().strip()
    data['Zone'] = self.soup.find(class_='zone-data').find('a').get_text().strip()

    # Adding inconsistent keys
    data['Growth habit:'] = None
    data['Patent Act:'] = None
    data['Companion Plants'] = None
    data['Garden style'] = None
    data['Sunset climate zones:'] = None
    data['Foliage color:'] = None
    data['Flower attributes'] = None

    # Remaining details
    data['Companion Plants'] = self.soup.find(class_='attribute details clear paragraph').find(class_='left').get_text().strip()
    data['Care'] = self.soup.find(id='Care').find(class_='attribute care paragraph').contents[2].strip()


    attr_d_c = self.soup.find_all(class_='attribute details clear')
    for i in range(0,len(attr_d_c)):
      if (attr_d_c[i].find_all('a')):
        list = []
        for el in attr_d_c[i].find_all('a'):
          list.append(el.get_text().strip())
        data[attr_d_c[i].find(class_='label').get_text().strip()] = list
      else:
        data[attr_d_c[i].find(class_='label').get_text().strip()] = attr_d_c[i].find(class_='left').get_text().strip()
    
    return data

