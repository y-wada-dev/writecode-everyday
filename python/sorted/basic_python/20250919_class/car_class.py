# クラスの練習

class Car:
    def __init__(self):
        self.make = "Nissan"
        self.model = "X-Trail"
        self.year = 2020
        self.color = "White"
        self.speed = 0

    def start_engine(self):
        self.start_engine = True
        print(f"{self.make}{self.model}のエンジンを始動します")

    def run(self):
        self.speed = 60
        if self.start_engine:
            print(f"{self.make}{self.model}が走行中です")
        else:
            print(f"{self.make}{self.model}はエンジンが始動していません")
    
    def brake(self):
        if self.speed > 0:
            self.speed = 0
            print(f"{self.make}{self.model}は停止しました")
        else:
            print(f"{self.make}{self.model}はすでに停止しています")
            
    def accelerate(self, increment):
        if self.start_engine:
            self.speed += increment
            print(f"{self.make}{self.model}の速度が{self.speed}km/hに加速しました")
        else:
            print(f"{self.make}{self.model}はエンジンが始動していません")

    def stop_engine(self):
        if self.speed > 0:
            print(f"{self.make}{self.model}は走行中です。エンジンを停止できません")
            return
        self.start_engine = False
        print(f"{self.make}{self.model}のエンジンを停止します")
    
def main():
    car = Car()
    car.start_engine()
    car.run()
    car.stop_engine()
    car.accelerate(20)
    car.brake()
    car.stop_engine()

if __name__ == "__main__":
    main()
