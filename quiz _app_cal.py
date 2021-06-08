#quiz calculator:

d = {}

print("lets play a quiz:")
print()
correct = []
x = True
while x == True:
    que  = str(input("enter question    :"))
    print()
    ans = str(input("enter ans  :")).split()
    print()
    actual_ans = input("enter actual answer :")
    if actual_ans not in ans:
        print("error/")
    else:
        d[que] = ans
        correct.append(actual_ans)

    quit = input("press 2 to quit program :")
    if quit == str(2):
        x = False
    else:
        pass

for i in range(2):
    print()
################################################quiz created
print("answer the following questions of the quiz created:")
print()
i = 0
for k in d.keys():
    print()
    print("question :",k)
    print()
    print("options :", "    ".join(d[k]))
    print()
    enter_ans = input("enter your choice :")
    print()
    if enter_ans == correct[i]:
        print("correct")
    else:
        print("incorrect")
        print("correct answer to the question :" + str(correct[i]))
    i += 1




