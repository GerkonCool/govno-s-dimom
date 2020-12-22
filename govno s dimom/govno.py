import random
text = "С новым годом!"
govno = "говно С дымом!"
a = []
num = 0
for i in text:
    a.append(text[num])
    num += 1
print(a)
counter = 0
attempts = 0
while True:
    counter += 1
    random.shuffle(a)
    result = ""
    num = 0
    for i in a:
        result = result + str((a[num]))
        num += 1
    print(result)
    if result != govno:
        print(counter)
    elif result == govno:
        print("Слово: ", result, " понадобилось попыток: ", counter)