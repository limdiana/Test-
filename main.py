class BeeElephant():
    def __init__(self, bee, elephant):
        self.bee = bee
        self.elephant = elephant

    def fly(self):
        if self.bee >= self.elephant:
            return True
        else:
            return False

    def trumpet(self):
        if self.bee > self.elephant:
            return  "tu-tu-doo-doo!"
        else:
            return "wzzzzz"

    def eat(self, meal, value):
        if (meal=="nectar") and (self.elephant - value >= 0) and (self.bee + value <= 100):
            self.elephant -= value
            self.bee += value
            return self.bee
        elif (meal=="grass") and (self.bee - value >= 0) and (self.elephant + value <= 100):
            self.bee -= value
            self.elephant += value
            return self.elephant
        else:
            return "Что-то тут не так😳"

    def get_parts(self):
        lists = [self.bee, self.elephant]
        return lists