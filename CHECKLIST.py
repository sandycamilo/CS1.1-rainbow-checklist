print('Hello World')
#
# def print_something(say_this):
#     print(say_this)
#
# print_something("HI")
#
# checklist = list()
# checklist.append('Blue')
# print(checklist)
# checklist.append('Orange')
# print(checklist)
#
# checklist = ['Blue', 'Orange']
# checklist[1] = 'Cats'
# print(checklist)


# Create our checklist

checklist = list()

# CREATE


def create(item):
    checklist.append('item')

# READ


def read(index):
    return checklist[index]

# UPDATE


def update(index, item):
    checklist[index] = item

# DESTROY


def destroy(index):
    checklist.pop(index)


def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + list_item)
        index += 1

def mark_completed(index):
    checklist[index] = "√" + checklist[index]
    list_all_items()

# def user_input(prompt):
#     user_input = input(prompt)
#     return user_input


def select(function_code):
    if function_code == "C":
        input_item = user_input("input item")
        create(input_item)

    elif function_code == "R":
        item_index = user_input("Index number")
        print(read(int(item_index)))

    elif function_code == "P":
        list_all_items()

    elif function_code == "Q":
        return False

    else:
        print("Unknown option")
        return True


def user_input(prompt):
    user_input = input(prompt)
    return user_input


# TESTING
def test():
    create("purple sox")
    create("red cloak")

    # print(read(0))
    # print(read(1))
    #
    # update(0, "purple socks")
    # destroy(1)
    #
    # print(read(0))
    # print(read(1))


test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, and Q to quit")
    running = select(selection)
