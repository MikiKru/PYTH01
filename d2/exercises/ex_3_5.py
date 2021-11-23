import math

x = y = 0

while True:
    command = input("Wprowadź polecenie kierunek (N,S,E,W) i krok (1,2,3,...)")
    if not command:
        distance = math.hypot(x,y)
        print(f"Odległość od (0,0) wynosi {distance:.2f}")
        break
    direction, step = command.split()
    if(direction == 'N'):
        y += int(step)
    if(direction == 'S'):
        y -= int(step)
    if(direction == 'W'):
        x -= int(step)
    if(direction == 'E'):
        x += int(step)
    print(f"Współrzędne robota: ({x},{y})")

