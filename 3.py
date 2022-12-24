#7#
class Internet():
    def __init__(self,tovar):
        self.tovar = tovar

    def cost(self, tovar):
        return 10.95 + 2.95 * (tovar-1)


print("Введите количество позиций: ")
n = int(input())
bum = Internet(n)
print(bum.cost(n))