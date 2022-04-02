print("hello,world")


for i in range(1, 10):
    for j in range(1, i+1):
        aaa = i*j
        print(j, "*", i, "=", i*j, '\t', end="",)
        j += 1
    i += 1
    print("")
