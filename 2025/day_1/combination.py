def main():
    position = 50
    zero_count = 0

    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            direction = line[0]
            distance= int(line[1:])
            
            step = - 1 if direction == 'L' else 1    
            for _ in range(distance):
                position = (position + step ) % 100
                if position == 0:
                    zero_count += 1
            # if direction == 'L':
            #     position -= distance
            # else:
            #     position += distance

            # position %= 100
            
            # if position == 0:
            #     zero_count += 1

    print(zero_count)

if __name__ == "__main__":
    main()
    
