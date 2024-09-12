import requests
from bs4 import BeautifulSoup
import pandas as pd

# 請調整網址變成你的 Google 試算表網址
url=""

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

table = soup.find_all("table")[0]

rows = []
for row in table.find_all("tr"):
    rows.append([cell.get_text() for cell in row.find_all(["th", "td"])])

df = pd.DataFrame(rows)

# 自行調整輸出檔案名稱
# 註：這個檔案會輸出到你執行這個程式的資料夾
df.to_csv("spreadsheet_data.csv", index=False)
