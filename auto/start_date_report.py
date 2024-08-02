import csv
import datetime
import requests
from collections import defaultdict

FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"

def get_start_date():
  print()
  print('Getting the first start date to query for.')
  print()
  print('The date must be greater than Jan 1st, 2018')
  year = int(input('Enter a value for the year: '))
  month = int(input('Enter a value for the month: '))
  day = int(input('Enter a value for the day: '))
  print()

  return datetime.datetime(year, month, day)

def get_file_lines(url):
  response = requests.get(url, stream=True)
  lines = []

  for line in response.iter_lines():
    lines.append(line.decode("UTF-8"))
  return lines

def get_employees_by_date():
  data = get_file_lines(FILE_URL)
  reader = csv.reader(data[1:])
  employees_by_date = defaultdict(list)

  for row in reader:
    start_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')
    employee_name = "{} {}".format(row[0], row[1])
    employees_by_date[start_date].append(employee_name)

  return employees_by_date

def get_same_or_newer(start_date, employees_by_date):
  if start_date in employees_by_date:
    return start_date, employees_by_date[start_date]
  else:
    future_dates = [date for date in employees_by_date if date > start_date]
    if future_dates:
      next_date = min(future_dates)
      return next_date, employees_by_date[next_date]
    else:
      return None, []

def list_newer(start_date):
  employees_by_date = get_employees_by_date()

  while start_date and start_date < datetime.datetime.today():
    start_date, employees = get_same_or_newer(start_date, employees_by_date)
    if start_date is None:
      break
    print("Started on {}: {}".format(start_date.strftime("%b %d, %Y"), employees))
    start_date = start_date + datetime.timedelta(days=1)

def main():
  start_date = get_start_date()
  list_newer(start_date)

if __name__ == "__main__":
  main()