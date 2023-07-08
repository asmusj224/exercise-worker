from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver import Chrome

def main():
  BASE_URL = 'https://musclewiki.com'
  driver = Chrome()
  driver.get(BASE_URL + '/directory')
  soup = BeautifulSoup(driver.page_source, 'html.parser')

  tables = soup.find_all('table')
  print(len(tables), 'number of tables')
  with open(f'exercises.sql', 'w') as file:
      for table in tables:
          table_body = table.find('tbody')
          rows = table_body.find_all('tr')
          print(len(rows), 'number of rows')
          for row in rows:
              columns = row.find_all('td')
              for column in columns:
                  a = column.find_all('a', href=True)
                  a = [element['href'] for element in a if element.text.strip().lower() not in ('male' and 'female')]
                  if len(a) > 0:
                      next_url = BASE_URL + a[0] 
                      print(next_url)
                      next_page = requests.get(next_url)
                      if 'yoga' in next_url:
                          continue
                      driver.get(next_url)
                      next_soup = BeautifulSoup(driver.page_source, 'html.parser')
                      h1 = next_soup.find('h1')
                      name = '' if h1 is None else h1.text.strip()
                      if '404' in name:
                          continue
                      div = next_soup.find('div', {"class": "tw-p-4 tw-border-gray-200 tw-bg-white tw-col-span-2"})
                      span = div.find('span')
                      category = span.text.strip()

                      videos = next_soup.find_all('video')
                      videos = '{' + ','.join([element['src'].strip() for element in videos]) + '}'
                      li = next_soup.find_all('li')
                      description = '\n'.join([element.text.strip().replace("'", "''")[1:] for element in li])
                      sql = f"INSERT INTO exercise (name, description, category, videos) VALUES('{name}', '{description}', '{category}', '{videos}');"
                      print(sql)
                      file.write(sql)
  file.close()

if __name__ == "__main__":
    main()
