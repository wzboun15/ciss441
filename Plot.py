from bs4 import BeautifulSoup
import requests
import os
import pandas as pd 
import matplotlib.pyplot as plt
### references
### 'https://www.geeksforgeeks.org/different-ways-to-create-pandas-dataframe/'
### https://datatofish.com/sort-pandas-dataframe/
### https://kite.com/python/answers/how-to-rotate-axis-labels-in-matplotlib-in-python

### downloading the website data collapse1 tag
URL = 'https://www.city-data.com/coronavirus/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results_parent = soup.find(id='card-content')
results_collapse1 = soup.find(id='collapse1')
# print(results_collapse1.prettify())

### scrape and save 
state_elems = results_collapse1.find_all('tr')
state_data = [ ] ### for collecting each row for making a df
for s_ct, state_row in enumerate(state_elems):
    columns_col = state_row.find_all('td')
    if columns_col:
        state_tag, confirmed_tag, recovered_tag, active_tag, deaths_tag = columns_col
        state_data.append([
            str(state_tag.text),
            int(confirmed_tag.text.replace(',','')),
            int(deaths_tag.text.replace(',',''))
            ])
df = pd.DataFrame(state_data, columns = ['State', 'Confirmed', 'Deaths'])
df.to_csv('C:\\Users\\Wathe\\Desktop\\Classes\\Spring 2020 Classes\\Business Intelligence\\Case Worksheets\\Case 12\\city_covid_data.csv')
### visualize make pretty
df.sort_values(by=['Confirmed'], inplace=True, ascending=False)
print(df.head(10))
ax = df.head(10).plot.bar(x='State',y={'Confirmed','Deaths'}, rot=0)
plt.xticks(rotation=45)
plt.show()