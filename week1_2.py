n, m = map(int, input().split())
jealous = list(int(input()) for _ in range(m))

jealous.sort()

a = sum(jealous)/n
b = sum(jealous)%n