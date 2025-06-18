def print_multiplication_tables():
    print("Multiplication Tables")
    print("______________________")

    for i in range(1, 11):
        print(f"Table for {i}:")
        for j in range(1, 11):
            result = i * j
            print(f" {i} x {j} = {result}")
            
            pritnt("")
print_multiplication_tables()