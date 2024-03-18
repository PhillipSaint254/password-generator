from time import sleep
import random
import sys
import string
import math


def user_input_checker(choice):
    acceptable = ["y", 'n', 'yes', 'no']

    if choice.lower() in acceptable:
        pass
    else:
        print(f"You entered an invalid input '{choice}'")
        sys.exit(1)


def mixer(pass_value):
    if pass_value:
        pass_value = list(pass_value)
        random.shuffle(pass_value)
        return ''.join(pass_value)
    return ''


def weight(min_num, max_num):
    return random.uniform(min_num, max_num)


def generate_password(upper, lower, numbers, special, min_len, max_len):
    len_upper = 0  # atmost 35%
    len_digits = 0  # atleast 30%
    len_lower = 0  # atleast 20%
    len_special = 0  # atleast 15%

    pass_len = random.randint(minLen, maxLen)

    # edge case when the user specifies 0 for length or all no's
    if pass_len == 0 or (not upper and not lower and not numbers and not special):
        print("You must choose atleast one field as true and a sensible minimum length for password")
        return ''

    if upper and lower and numbers and special:
        if pass_len < 4 > min_len:
            print("Password unable to generate since too small minimum length was chosen")
            return ''

        # weight calculation
        upper_weight = weight(.25, .3)
        digits_weight = weight(.285, .325)
        special_weight = weight(.15, .2)

        len_upper = round(pass_len*upper_weight) if pass_len * \
            upper_weight > 1 else 1
        len_digits = int(pass_len*digits_weight) if pass_len * \
            digits_weight > 1 else 1
        len_special = int(pass_len*special_weight) if pass_len * \
            special_weight > 1 else 1
        len_lower = pass_len - (len_upper+len_digits+len_special) if pass_len - \
            (len_upper+len_digits+len_special) > 0 else 1

    elif lower and numbers and special:
        if pass_len < 3 > min_len:
            print("Password unable to generate since too small minimum length was chosen")
            return ''

        digits_weight = weight(.285, .325)
        special_weight = weight(.15, .2)

        len_digits = int(pass_len*digits_weight) if pass_len * \
            digits_weight > 1 else 1
        len_special = int(pass_len*special_weight) if pass_len * \
            special_weight > 1 else 1
        len_lower = pass_len - \
            (len_digits+len_special) if pass_len - \
            (len_digits+len_special) > 0 else 1

    elif upper and numbers and special:
        if pass_len < 3 > min_len:
            print("Password unable to generate since too small minimum length was chosen")
            return ''

        digits_weight = weight(.285, .325)
        special_weight = weight(.15, .2)

        len_digits = int(pass_len*digits_weight) if pass_len * \
            digits_weight > 1 else 1
        len_special = int(pass_len*special_weight) if pass_len * \
            special_weight > 1 else 1
        len_upper = pass_len - \
            (len_digits+len_special) if pass_len - \
            (len_digits+len_special) > 0 else 1

    elif lower and upper and numbers:
        if pass_len < 3 > min_len:
            print("Password unable to generate since too small minimum length was chosen")
            return ''

        upper_weight = weight(.25, .3)
        digits_weight = weight(.285, .325)

        len_upper = round(pass_len*upper_weight) if pass_len * \
            upper_weight > 1 else 1
        len_digits = int(pass_len*digits_weight) if pass_len * \
            digits_weight > 1 else 1
        len_lower = pass_len - \
            (len_digits+len_upper) if pass_len - \
            (len_digits+len_upper) > 0 else 1

    elif lower and upper and special:
        if pass_len < 3 > min_len:
            print("Password unable to generate since too small minimum length was chosen")
            return ''

        upper_weight = weight(.285, .325)
        special_weight = weight(.285, .325)

        len_upper = round(pass_len*upper_weight) if pass_len * \
            upper_weight > 1 else 1
        len_special = int(pass_len*special_weight) if pass_len * \
            special_weight > 1 else 1
        len_lower = pass_len - \
            (len_digits+len_upper) if pass_len - \
            (len_digits+len_upper) > 0 else 1

    elif lower and upper:
        if pass_len < 2 > min_len:
            print("Password unable to generate since too small minimum length was chosen")
            return ''

        upper_weight = weight(.385, .425)

        len_upper = round(pass_len*upper_weight) if pass_len * \
            upper_weight > 1 else 1
        len_lower = pass_len - len_upper if pass_len - len_upper > 0 else 1

    elif lower and numbers:
        if pass_len < 2 > min_len:
            print("Password unable to generate since too small minimum length was chosen")
            return ''

        digits_weight = weight(.3, .38)

        len_digits = int(pass_len*digits_weight) if pass_len * \
            digits_weight > 1 else 1
        len_lower = pass_len - len_digits if pass_len - len_digits > 0 else 1

    elif lower and special:
        if pass_len < 2 > min_len:
            print("Password unable to generate since too small minimum length was chosen")
            return ''

        len_special = int(pass_len*.35) if pass_len*.35 > 1 else 1
        len_lower = pass_len - len_digits if pass_len - len_digits > 0 else 1

    elif upper and numbers:
        if pass_len < 2 > min_len:
            print("Password unable to generate since too small minimum length was chosen")
            return ''

        len_digits = int(pass_len*.35) if pass_len*.35 > 1 else 1
        len_upper = pass_len - len_digits if pass_len - len_digits > 0 else 1

    elif upper and special:
        if pass_len < 2 > min_len:
            print("Password unable to generate since too small minimum length was chosen")
            return ''

        len_special = int(pass_len*.35) if pass_len*.35 > 1 else 1
        len_upper = pass_len - len_digits if pass_len - len_digits > 0 else 1

    elif special and numbers:
        if pass_len < 2 > min_len:
            print("Password unable to generate since too small minimum length was chosen")
            return ''

        len_digits = round(pass_len*.55) if pass_len*.3 > 1 else 1
        len_special = pass_len - len_digits if pass_len - len_digits > 0 else 1

    elif lower:
        if pass_len < 1 > min_len:
            print("Password unable to generate since too small minimum length was chosen")
            return ''

        len_lower = pass_len

    elif upper:
        if pass_len < 1 > min_len:
            print("Password unable to generate since too small minimum length was chosen")
            return ''

        len_upper = pass_len

    elif special:
        if pass_len < 1 > min_len:
            print("Password unable to generate since too small minimum length was chosen")
            return ''

        len_special = pass_len

    elif numbers:
        if pass_len < 1 > min_len:
            print("Password unable to generate since too small minimum length was chosen")
            return ''

        len_digits = pass_len

    pass_string = ''.join(random.choice(string.ascii_lowercase)
                          for i in range(len_lower))
    pass_string = mixer(pass_string)

    pass_string += ''.join(random.choice(string.ascii_uppercase)
                           for i in range(len_upper))
    pass_string = mixer(pass_string)

    pass_string += ''.join(random.choice(string.digits)
                           for i in range(len_digits))
    pass_string = mixer(pass_string)

    pass_string += ''.join(random.choice(string.punctuation)
                           for i in range(len_special))
    pass_string = mixer(pass_string)

    return pass_string


print("#"*10)
print("Welcome to Automatic Password Generator.")
print(" I will generate a random password for you if you specify the following information")
sleep(1)

minLen = int(input("Enter password minimum length eg 6: "))
maxLen = int(input("Enter password maximum length eg 10: "))

upper = input(
    "Enrter Y [for yes] or N [for no]. Should I include upper case letters in the password: ").strip()

user_input_checker(upper)

lower = input(
    "Enrter Y [for yes] or N [for no]. Should I include lower case letters in the password: ").strip()

user_input_checker(lower)

numbers = input(
    "Enrter Y [for yes] or N [for no]. Should I include numbers in the password: ").strip()

user_input_checker(numbers)

special = input(
    "Enrter Y [for yes] or N [for no]. Should I include special characters in the password: ").strip()

user_input_checker(special)

upper = True if upper.lower() == "y" or upper.lower() == "yes" else False
lower = True if lower.lower() == "y" or lower.lower() == "yes" else False
numbers = True if numbers.lower() == 'y' or numbers.lower() == "yes" else False
special = True if special.lower() == 'y' or special.lower() == "yes" else False

print(
    f"Password Genrated: '{generate_password(upper, lower, numbers, special, minLen, maxLen)}'")
