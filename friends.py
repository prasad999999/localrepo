def count_lines():
    f=open("friends.txt","r")
    count_line=0
    for line in f:
        for word in line.split():
            for char in word:
                if char.isupper():
                    count_line+=1
    print(count_line)
count_lines()
