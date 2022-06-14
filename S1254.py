string = input()

for i in range(len(string)):
    st_case = string + string[:i][::-1]

    if st_case == st_case[::-1]:
        print(len(st_case))
        break