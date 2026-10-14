class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def get_info(self):
        return f"brand : {self.brand}  model : {self.model}  year : {self.year}"

car1=Car("Audi","a6","2020")
car2=Car("Porsche","gtr3","2024")

print(car1.get_info())
print(car2.get_info())



    