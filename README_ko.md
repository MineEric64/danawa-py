# danawa-py
다나와 비공식 API

- [English README Documentation](./README.md)

## 공지
주의!

이 다나와 API는 다나와 개발자가 아닌 다나와 유저가 만든 **비공식** API입니다.

따라서 다나와 API 개발자는 이 API를 사용하므로써 어느 법적 책임도 지지 않습니다.

**다나와 공식 API를 사용하는 것을 권장합니다.**

## 사용법
|함수|설명|매개 변수|
|:--:|:---:|:---:|
|`get_product_codes(keyword)`|키워드 (쿼리)를 통해 제품 코드 배열을 가져옵니다. 사용하여 제품들을 검색할 수 있습니다.|`keyword` 타입: str|
|`get_product(product_code)`|제품 코드를 통해 제품 정보를 가져옵니다.|`product_code` 타입: int|
|`get_price_variance(product_code, by_month)`|날마다 가격 정보가 있는 가격 변동 배열을 가져옵니다. `by_month` 변수는 변동 배열이 얼마나 많은 정보를 가지고 있는지에 따라 결정됩니다. `by_month` 변수는 범위가 있습니다. (1, 3, 6, 12만 가능)|`product_code` 타입: int, `by_month` 타입: int|

### 
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
