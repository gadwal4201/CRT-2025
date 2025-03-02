def pascals_triangle(row):
    a=1
    for i in range(1,row):
        for j in range(1,row-i):
            print(" ")
            j=j+1
        for k in range(1,i):
            print(a)
            a=a*(i-k)/k
            k=k+1
        a=a+1
        print("\n")
        i=i+1
        
        
pascals_triangle(5)