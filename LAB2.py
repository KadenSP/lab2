
def main():
    display_main_menu()
    UI=get_user_input()
    calc_average(UI)
    find_min_max(UI)

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    userinput = input()
    userinput = userinput.split(",")
    floatinput = [float(x) for x in userinput]
    return floatinput

def calc_average(UI):
    average=sum(UI)/len(UI)
    print("average =", average)

    
def find_min_max(UI):
    min_v = min(UI)
    max_v = max(UI)
    print("Minimum value:", min_v)
    print("Maximum value:", max_v)

main()

