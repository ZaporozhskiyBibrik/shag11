mport sqlite3
import time
import requests
from bs4 import BeautifulSoup

conn = sqlite3.connect("temp.sl3")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS weather_data (date TEXT, temperature REAL)''')
temperature = "N/A" 
temperature2 = "0" 
for _ in range(10):
    response = requests.get("https://weather.com/uk-UA/weather/today/l/35a741555bbfc8bc576be864b0b64af6d1b2ad1328d2ee729f0de0ae00098e85")
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("div", {"class": "CurrentConditions--primary--2DOqs"})
    if soup_list:
        temperature = soup_list[0].find("span").text
        c.execute("INSERT INTO weather_data (date, temperature) VALUES (?, ?)", (time.strftime('%Y-%m-%d %H:%M:%S'), temperature))
        conn.commit()
        print(temperature,"-The temperature for today in Kiev.", temperature2, "- The temperature for tommorow in Kiev")  
    else:
        print("Unable to find temperature data on the webpage")
    time.sleep(1800)
c.execute("SELECT * FROM weather_data")
for row in c.fetchall():
    print(row)
c.close()
conn = sqlite3.connect("temp.sl3")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS weather_data2 (date TEXT, temperature REAL)''')
temperature2 = "0"  
for _ in range(10):
    response = requests.get("https://weather.com/uk-UA/weather/weekend/l/c431c8e36d43dc4952f66e4fd8bf4e5e72a3c2a787261be7b7826f0321204b84")
    soup2 = BeautifulSoup(response.text, features="html.parser")
    soup_list2 = soup2.find_all("div", {"class": "CurrentConditions--primary--2DOqs"})
    if soup_list2:
        temperature2 = soup_list2[0].find("span").text
        c.execute("INSERT INTO weather_data (date, temperature) VALUES (?, ?)",(time.strftime('%Y-%m-%d %H:%M:%S'), temperature2))
        conn.commit()
        print(temperature2,"- The temperature for ten days in Kiev.")
    else:
        print("Unable to find temperature data on the webpage")
    time.sleep(1800)
print('----------------')
c.execute("SELECT * FROM weather_data2")
for row in c.fetchall():
    print(row)
c.close()
