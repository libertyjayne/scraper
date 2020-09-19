import sys
import csv
from csv import writer, reader, DictReader

class CSV:
  def __init__(self, data, filename):
    self.data = data
    self.filename = filename
    self.set_data()
    self.get_data()
  
  def set_data(self):
    with open(self.filename, 'w', newline='') as csvfile:
      writer = csv.DictWriter(csvfile, fieldnames=self.data[0].headers)
      writer.writeheader()

      for el in self.data:
        writer.writerow(el.data)

  # Verify data captured
  def get_data(self):
    with open(self.filename, newline='') as f:
      reader = csv.reader(f)
      try:
          for row in reader:
              print(row)
      except csv.Error as e:
          sys.exit('file {}, line {}: {}'.format(self.filename, reader.line_num, e))