class Car:
    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def say_state(self):
        print("Estou indo a {} kph!".format(self.speed))

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        if self.time != 0:
            return self.odometer / self.time
        else:
            pass


if __name__ == '__main__':

    celtinha = Car()
    print("Eu sou um Celtinha!")
    while True:
        action = input("O que eu deveria fazer? [A]celerar, [F]rear"
                       ", mostrar [H]odômetro, ou mostrar [V]elocidade Média?  ").upper()
        if action not in "AFHV" or len(action) != 1:
            print("Eu não sei fazer isso.")
            continue
        if action == 'A':
            celtinha.accelerate()
        elif action == 'F':
            celtinha.brake()
        elif action == 'H':
            print("Estou dirigindo a {} kilometers".format(celtinha.odometer))
        elif action == 'V':
            print("Minha velocidade média é {0:4.2f} kph".format(
                celtinha.average_speed()))
        celtinha.step()
        celtinha.say_state()
