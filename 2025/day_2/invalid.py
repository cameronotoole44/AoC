def is_invalid_id(n: int) -> bool:
    s = str(n)
    if len(s) % 2 != 0:
        return False
    mid = len(s) // 2
    return s[:mid] == s[mid:]

with open("input.txt") as f:
    text = f.read().strip()

parts = [p.strip() for p in text.split(",") if p.strip()]
ranges = []
for part in parts:
    start_str, end_str = part.split("-")
    start = int(start_str)
    end = int(end_str)
    ranges.append((start, end))


def main():
    invalid_count = 0
    invalid_sum = 0

    for start, end in ranges:
        for n in range(start, end + 1):
            if is_invalid_id(n):
                invalid_count += 1
                invalid_sum += n

    print(invalid_sum)

if __name__ == "__main__":
    main()
