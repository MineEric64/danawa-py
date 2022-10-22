# danawa-py
Danawa Unofficial API

- [한국어 README 문서](./README_ko.md)

## NOTE
Warning!

This danawa api is **unofficially** made by danawa user, not danawa developer.

So this danawa api developer does not assume any legal responsibility arising from using this api.

**Please consider using danawa official api.**

## Usage
|Method|Description|Parameter|
|:--:|:---:|:---:|
|`get_product_codes(keyword)`|get product code list from keyword (query). you can search product list by using it.|`keyword` type: str|
|`get_product(product_code)`|get product info from product code.|`product_code` type: int|
|`get_price_variance(product_code, by_month)`|get price variance list that has price information each date. `by_month` param is determined by how many info variance list has. `by_month` param has range (1, 3, 6, 12 only)|`product_code` type: int, `by_month` type: int|

### Example
```python
import danawa as dw

products = dw.get_product_codes("rtx 3060ti")
product = products[0]

print(product)
# {'code': 12822224, 'price': 593130, 'title': '이엠텍 지포스 RTX 3060 Ti STORM X Dual OC D6 8GB'}

product_code = product["code"]

variance = dw.get_price_variance(product_code, 1)
print(variance)
# {'min': '498440', 'max': '573590', 'prices': [{'price': 561500, 'date': '09-27', 'full_date': '22-09-27'}, {'price': 498440, 'date': '10-04', 'full_date': '22-10-04'} ...}
```
