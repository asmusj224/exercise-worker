from bs4 import BeautifulSoup
import requests

def main():
  BASE_URL = 'https://musclewiki.com'


  categories = ['shoulders', 'chest', 'traps', 'biceps', 'abdominals', 'obliques', 'quads', 'calves', 'hamstrings', 'glutes', 'forearms', 'lats', 'lowerback', 'traps_middle', 'triceps']

  type = 'plate'
  gender = 'female'

  URL = f'/{type}/{gender}/'

  for category in categories:
      print(BASE_URL + URL + category)
      req = requests.get(BASE_URL + URL + category)
      soup = BeautifulSoup(req.text, 'html.parser')
      spans = soup.find_all('span')

      button = soup.find('button', class_='btn btn-primary-second-page exercise-more-button')
      ordered_list = soup.find_all('ol')

      with open(f'{type}_{gender}_{category}_exercises.sql', 'w') as file:
          for span in spans:
              a = span.findChildren('a', recursive=False)
              for idx, child in enumerate(a):
                  description = ordered_list[idx].text.strip().replace("'", "''")
                  file.write(f"INSERT INTO exercise (name, description, category) VALUES ('{child.text.strip()}', '{description}', '{category}') ON CONFLICT (name) DO NOTHING;\n")
          while button is not None:
              next_page_url = button['onclick'].split("'")[1]
              print(next_page_url)
              next_page = requests.get(BASE_URL + next_page_url)
              next_soup = BeautifulSoup(next_page.text, 'html.parser')
              spans = next_soup.find_all('span')
              ordered_list = next_soup.find_all('ol')
              for span in spans:
                  a = span.findChildren('a', recursive=False)
                  for idx, child in enumerate(a):
                      description = ordered_list[idx].text.strip().replace("'", "''")
                      file.write(f"INSERT INTO exercise (name, description, category) VALUES ('{child.text.strip()}', '{description}', '{category}') ON CONFLICT (name) DO NOTHING;\n")
              button = next_soup.find('button', class_='btn btn-primary-second-page exercise-more-button')
      file.close()

if __name__ == "__main__":
    main()
