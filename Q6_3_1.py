from Nigiri import katsuo
class katsuo(Nigiri):
    top = "かつお"
    topping = "生姜とねぎ"
    price = 100

    def show_attributes(self):
        super().show_attributes()
        print("topping: {}".format(self.topping))
 k1 = katsuo()
 k1.show_attributes

