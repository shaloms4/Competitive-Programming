def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    n = int(data[0])
    phone_book = {}

    for i in range(1, n + 1):
        name, number = data[i].split()
        phone_book[name] = number

    queries = data[n + 1:]
    for query in queries:
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")

if __name__ == "__main__":
    main()
