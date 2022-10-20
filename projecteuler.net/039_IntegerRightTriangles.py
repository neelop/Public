def main():
    counter = [0] * 1001
    # most likely can be sped up
    for p in range(12, 1001):
        for a in range(1, p // 3):
            a2 = a * a
            for b in range(a, (p - a) // 2):
                b2 = b * b
                c = p - a - b
                c2 = c * c
                if a2 + b2 == c2:
                    counter[p] += 1
    print(counter.index(max(counter)))


if __name__ == "__main__":
    main()
