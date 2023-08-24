class Nigiri:
    def __init__(self):
        self.base = "しゃり"
        self.category = "にぎり"

    def show_attributes(self):
        print(
            "top: {}, base: {}, category: {}".format(self.top, self.base, self.category)
        )
        print("price: {}円".format(self.price))


class Katsuo(Nigiri):
    top = "かつお"
    topping = "生姜とねぎ"
    price = 100

    def show_attributes(self):
        super().show_attributes()
        print("topping: {}".format(self.topping))


k1 = Katsuo()
k1.show_attributes()
