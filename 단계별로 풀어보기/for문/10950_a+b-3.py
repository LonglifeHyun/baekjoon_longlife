def main():
    t = int(input())

    answer = []
    for i in range(t):
        a, b = map(int, input().split())
        answer.append(a+b)

    for ans in answer:
        print(ans)

if __name__ == "__main__":
    main()
    