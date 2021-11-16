price = 19.95
discountPercent = 30
markdown = (discountPercent / 100) * price
price = price - markdown
price = price - (price%.01)
print("The discounted price is $", price, sep = "")
