def process_list(numbers):
    total = 0
    for num in numbers:
        total += num 
    return total


def main():
    data = [1, 2, 3, 4, 5]  
    result = process_list(data)
    print("Resultatet er:", result) 


if __name__ == "__main__":
    main()
    
