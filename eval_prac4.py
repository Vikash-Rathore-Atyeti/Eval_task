class Car:
    def start_engine(self):
        print("Engine started ")

print("Before patching:")
car = Car()
car.start_engine() 

def new_start_engine(self):
    print("Engine started with a roar")

Car.start_engine = new_start_engine

print("After patching:")
car.start_engine()
