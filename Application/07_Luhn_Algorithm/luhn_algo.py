
def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]
    print(card_number_reversed)
    print(odd_digits)
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)
        sum_of_even_digits = 0
        print(digit)

def main():
    card_number = '4111-1111-4555-1142'
    print(card_number)
    card_translation =str.maketrans({"-": "", " ": ""})
    translated_card_number = card_number.translate(card_translation)
    print(translated_card_number)
    verify_card_number(translated_card_number)

main()

