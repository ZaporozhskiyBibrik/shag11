import requests
from bs4 import BeautifulSoup
import sqlite3
import time
conn = sqlite3.connect("temp.sl3")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS weather_data (date TEXT, temperature REAL)''')
temperature = "N/A"  # Default value
for _ in range(10):
    response = requests.get("https://weather.com/uk-UA/weather/today/l/28d2ee729f0de0ae00098e85")
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("div", {"class": "CurrentConditions--primary--2DOqs"})
    if soup_list:
        temperature = soup_list[0].find("span").text
        c.execute("INSERT INTO weather_data (date, temperature) VALUES (?, ?)", (time.strftime('%Y-%m-%d %H:%M:%S'), temperature))
        conn.commit()
        print(temperature)
    else:
        print("Unable to find temperature data on the webpage")
    print(temperature)
    time.sleep(1800)
print('----------------')
c.execute("SELECT * FROM weather_data")
for row in c.fetchall():
    print(row)
c.close()
