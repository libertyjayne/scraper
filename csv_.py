import sys
import csv
from csv import writer, reader, DictReader

class CSV:
  def __init__(self, data, filename):
    self.data = data
    self.filename = filename
    self.set_data()


  # def create_row_list(self):
  #   row = []
  #   for key in self.data_dict:
  #     row.append(self.data_dict[key])
  #   return row

    # To do - check for headers/try/catch
  # def set_data(self):
  #   with open(self.filename, 'w') as csv_file:
  #     csv_writer = writer(csv_file)
  #     csv_writer.writerow(self.create_row_list())
  
  # Verify data captured
  # def get_data(self):
  #   with open(self.filename, newline='') as f:
  #     reader = csv.reader(f)
  #     try:
  #         for row in reader:
  #             print(row)
  #     except csv.Error as e:
  #         sys.exit('file {}, line {}: {}'.format(self.filename, reader.line_num, e))

  def set_data(self):
    with open(self.filename, 'w', newline='') as csvfile:
      writer = csv.DictWriter(csvfile, fieldnames=self.data.headers)
      writer.writeheader()

      # for el in self.data:
      #   writer.writerow(el)