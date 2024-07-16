class Market:
    def __init__(self, name:str, address:str, balance:float = 0, products = {}) -> None:
        self.name = name
        self.address = address
        self.balance = 0
        self.products = {}
    def get_product_info(self):
        print("Bozorda mavjut mahsulotlar:")
        for i in self.products:
            print(f"{i} - {self.products[i][0]} so'm, {self.products[i][1]} dona")
    def add_product(self, product:str, price:float, quantity:int) -> None:
        self.products [product] = [price, quantity]


    def remove_product(self, product:str):
        del self.products[product]


    def add_money(self, amount:int) -> None:
        self.balance += amount


    def sell(self, product:str, quantity) -> None:
        self.add_money(self.products[product][0] * quantity)
        self.products[product][1] -= quantity

bozor = Market("Super", "Toshkent, O'zbekiston")
bozor.add_product("olma", 5000, 10)
bozor.add_product("banan", 7000, 5)
print("")

bozor.get_product_info()
bozor.sell("olma", 3)
print("")
bozor.get_product_info()

bozor.add_money(100)

# print(bozor.balance)

print("")

bozor.get_product_info()
bozor.remove_product("banan")
print("")
bozor.get_product_info()
