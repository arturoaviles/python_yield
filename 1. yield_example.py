for i in range(10):
    print(i)

def get_first_10():
    for j in range(10):
        yield j


my_list = get_first_10()

print("\n\n")

for k in my_list:
    print(k)



