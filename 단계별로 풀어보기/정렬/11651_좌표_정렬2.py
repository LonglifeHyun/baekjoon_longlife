n = int(input())

coordinates = []

for _ in range(n):
    coordinates.append(tuple(map(int, input().split())))

coordinates.sort(key=lambda x: (x[1],x[0]))

for point in coordinates:
    print(point[0],point[1])