class Nigiri:
    def show_attributes(self):
        print("top: {}".format(self.top))
        print("rice: {}".format(self.rice))


class Katsuo(Nigiri):
    def __init__(self):
        self.top = "かつお"
        self.topping = "生姜とねぎ"
        self.price = 100

    def show_attributes(self):
        super().show_attributes()
        print("topping: {}".format(self.topping))


k1 = Katsuo()
k1.show_attributes()
