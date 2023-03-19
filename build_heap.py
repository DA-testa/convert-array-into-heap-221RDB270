# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    d = len(data)
    
    def heapsort(i):
        min = i
        a = 2 * i + 1
        b = 2 * i + 2
        
        if a < d and data[b] < data[min]:
            min = a
       
        if b < d and data[b] < data[min]:
            min = b
            
        if min != i:
            data[i], data[min] = data[min], data[i]
            swaps.append((i, min))
            heapsort(min)
            
    for i in range(d//2-1, -1, -1):
        heapsort(i)



    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    

    # input from keyboard
    while True:
        inp = input()
        if inp == 'I':
            n = int(input())
            data = list(map(int, input().split()))
            test = input().strip()
            break
        elif inp == 'F':
            file = input()
            try:
                with open(file, 'r') as f:
                    input = f.readlines()
                    data = list(map(int, input_lines[1].strip().split()))
                    test = input_lines[2].strip()
                    break
            except FileNotFoundError:
                print()
                continue

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
