def valid_cradit(cradit_number):
    return True

def get_accunt_info():
    return 555566661111


def main():
    while True:
        user_input = input("please enter a number: ")
        if not valid_cradit(user_input):
            continue
        
        print(get_accunt_info())
main()