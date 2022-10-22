import danawa as dw
import pandas as pd

from datetime import datetime
from forex_python.converter import get_rate

product = dw.get_product_codes("rtx 3060ti")[0]
product_code = product["code"]

variance1 = dw.get_price_variance(product_code, 3)
variance2 = dw.get_price_variance(product_code, 12)
variance3 = []

sub = variance1["prices"][0]["date"][0:2]

for v in variance2["prices"]:
    if v["date"].endswith(sub):
        break

    variance3.append({
        "full_date": v["date"] + "-01",
        "price": v["price"]
                      })

for v in variance1["prices"]:
    variance3.append({
        "full_date": v["full_date"],
        "price": v["price"]
    })


columns = ["price", "date", "rate"]
prices = [d["price"] for d in variance3]
dates1 = [d["full_date"] for d in variance3]
dates2 = []
rates = []

for i in dates1:
    i2 = i.split("-")

    t = datetime(2000 + int(i2[0]), int(i2[1]), int(i2[2]))
    rate1 = get_rate("USD", "KRW", t)
    rate2 = round(rate1, 2)

    rates.append(rate2)
    dates2.append("{}-{}-{}".format(t.year, t.month, t.day))

data = {
    "price": prices,
    "date": dates2,
    "rate": rates
}

df = pd.DataFrame(data, columns=columns)
df.to_csv("price_info.csv", float_format="%.2f", columns=columns, index=False)