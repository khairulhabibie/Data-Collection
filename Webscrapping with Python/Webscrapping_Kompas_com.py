# import library / package
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# alamat 
alamat = "https://www.kompas.com/"
html = urlopen(alamat)
soup = BeautifulSoup(html, 'html.parser')

# mengambil data perbaris

table = soup.find("div", {"class":"most ga--most mt1 clearfix"})
#print(table)
rows = table.find_all("h4", {"class":"most__title"})
#print(rows)
konten = [row.get_text() for row in rows]
#print(konten)
df_konten = pd.DataFrame(konten, columns=['berita_populer'])
#df_konten

# simpan  data frame ke csv

df_konten.to_csv('hasil_Webscrapping_Kompas_com.csv', index=False)