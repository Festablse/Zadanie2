print("------------------------------------------------------")
print("Часть7 №1")
import bs4
import requests
import matplotlib.pyplot as plt
response = requests.get("http://mfd.ru/currency/?currency=USD")
stranica_text = response.text
soup = bs4.BeautifulSoup(response.text, "lxml")
table_kurs_usd = soup.find_all("table", {"class": "mfd-table mfd-currency-table"})
table = [usd.text for usd in table_kurs_usd]
table = table[0].split("\n")
table = [i for i in table if i != ""]
        elif mid_element > to_search:
            new_posicion = id_index - 1
            last_index = new_posicion
usd_table_dict = {}
for data in range(3, len(table), 3):
    usd_table_dict[table[data]] = table[data + 1]
print(usd_table_dict)
dates = [i for i in reversed(usd_table_dict)]
znach_usd = [usd_table_dict[i] for i in dates]
for i in range(len(znach_usd)):
    znach_usd[i] = float(znach_usd[i].replace(",", "."))
plt.plot(dates, znach_usd)
plt.show()
print("------------------------------------------------------")
print("Часть7 №2")
import bs4
import requests
import matplotlib.pyplot as plt
response = requests.get("https://yandex.ru/news/quotes/1.html")
stranica_text = response.text
soup = bs4.BeautifulSoup(response.text, "lxml")
table_kurs_usd = soup.find_all("div", {"class": "news-stock-table__cell"})
table = [usd.text for usd in table_kurs_usd]
usd_table_dict = {}
for data in range(3, len(table), 3):
    usd_table_dict[table[data]] = table[data + 1]
dates = [i for i in reversed(usd_table_dict)]
znach_usd = [usd_table_dict[i] for i in dates]
for i in range(len(znach_usd)):
    znach_usd[i] = float(znach_usd[i].replace(",", "."))
plt.plot(dates, znach_usd)
plt.show()
print("------------------------------------------------------")
