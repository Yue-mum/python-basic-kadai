def total_price(price, tax):
    total = price + (price * tax /100)
    return total
print(total_price(110, 10))
