# 定義炸雞類別
class FriedChicken:
    # 建構子，初始化物件屬性
    def __init__(self, flavor, size, crispy_level, sauce, price):
        self.flavor = flavor         # 口味
        self.size = size             # 大小
        self.crispy_level = crispy_level  # 脆度
        self.sauce = sauce           # 醬料
        self.price = price           # 價格

    # 副函式1：顯示炸雞的基本資訊
    def display_info(self):
        print(f"炸雞資訊 - 口味: {self.flavor}, 尺寸: {self.size}, 脆度: {self.crispy_level}, 醬料: {self.sauce}, 價格: {self.price} 元")

    # 副函式2：調整炸雞的脆度
    def adjust_crispy_level(self, new_level):
        self.crispy_level = new_level
        print(f"酥脆程度已調整為 {new_level}")

    # 副函式3：計算炸雞的折扣價格
    def calculate_discounted_price(self, discount_rate):
        discounted_price = self.price * (1 - discount_rate)
        print(f"折扣後價格為 {discounted_price} 元")

# 四個炸雞物件
chicken1 = FriedChicken("香辣", "大份", "超級脆", "辣椒醬", 150)
chicken2 = FriedChicken("原味", "中份", "普通脆", "蜂蜜芥末醬", 120)
chicken3 = FriedChicken("椒麻", "小份", "極度脆", "麻辣醬", 100)
chicken4 = FriedChicken("蒜香", "大份", "酥脆", "蒜香醬", 160)

# 三個副函式
chicken1.display_info()  # 顯示炸雞資訊
chicken2.adjust_crispy_level("超酥脆")  # 調整脆度
chicken3.calculate_discounted_price(0.1)  # 計算折扣價格
