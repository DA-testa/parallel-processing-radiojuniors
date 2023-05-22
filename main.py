# python3

def parallel_processing(n, m, data):
    threads = [(0, i) for i in range(n)]
    output = []
    for i in range(m):
        time, thread = threads[i % n]
        output.append((thread, time))
        threads[i % n] = (time + data[i], thread)
    return output

def main():
    n, m = [int(i) for i in input().split()]
    data = list(map(int, input().split()))
    result = parallel_processing(n,m,data)
    for i in result:
        print(i[0], i[1])

if __name__ == "__main__":
    main()
