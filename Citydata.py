from bs4 import BeautifulSoup
import requests
### references
### 'https://www.city-data.com/coronavirus/'
URL = 'https://www.city-data.com/coronavirus/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results_parent = soup.find(id='card-content')
results_collapse1 = soup.find(id='collapse1')
# print(results_collapse1.prettify())


state_elems = results_collapse1.find_all('tr')
print("{0:<30}{1:<20}{2:<20}{3:<20}{4:<20}".format(
    "State",
    "Confirmed",
    "Recovered",
    "Active",
    "Deaths"
    ))
for s_ct, state_row in enumerate(state_elems):
    columns_col = state_row.find_all('td')
    if columns_col:
        state_tag, confirmed_tag, recovered_tag, active_tag, deaths_tag, = columns_col
        print("{0:<30}{1:<20}{2:<20}{3:<20}{4:<20}".format(
            state_tag.text,
            confirmed_tag.text,
            recovered_tag.text,
            active_tag.text,
            deaths_tag.text
            ))