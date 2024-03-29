# python3
import os

def build_heap(data):
    d = len(data)
    swaps = []

    def heapsort(i):
        min = i
        a = 2 * i + 1
        b = 2 * i + 2
        
        if a < d and data[a] < data[min]:
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
    data = []
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    

    # input from keyboard
    test = input()
    
    if "I" in test:
         try:
            d = int(input())
            data = list(map(int, input().split()))
         except ValueError:
            print("Error")
            return
    
    elif  "F" in test:
        try:
            filen = input()
            with open(f"test/{filen}", 'r') as file:
                d = int(file.readline().strip())
                data = list(map(int, file.readline().strip().split()))
        except FileNotFoundError:
            print("Error")
            return
   
           
            
           

    # checks if lenght of data is the same as the said lenght
    assert len(data) == d
   

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
