import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
from bs4 import Comment

pos = ['QB', 'WR', 'RB', 'TE', 'DT', 'DE', 'LB', 'CB', 'S']
hold = []
for pos in pos:
    url = "http://www55.myfantasyleague.com/2014/top?L=53424&SEARCHTYPE=BASIC&COUNT=64&YEAR=2014&START_WEEK=1&END_WEEK=17&CATEGORY=CONFERENCE00A&POSITION={}&DISPLAY=points&TEAM=*"

    html = urlopen(url.format(str(pos)))
    print(url.format(str(pos)))

    soup = BeautifulSoup(html, "html.parser")

    print(type(soup))

    column_headers = [th.getText() for th in
                      soup.findAll('tr', limit=10)[3].findAll('th')]

    print(column_headers)

    data_rows = soup.findAll('tr')[3:]

    player_data = [[td.getText() for td in data_rows[i].findAll('td')]
                   for i in range(len(data_rows))]

    df = pd.DataFrame(player_data, columns=column_headers)
    hold.append(df[1:64])

save=pd.concat(hold)
save.to_csv('/Users/edwardgorelik/Desktop/Raw/MFL/2014.csv')
