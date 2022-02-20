import re
#  define the building blocks

# zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen
# fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty, thirty, forty, fifty, sixty, seventy
# eighty, ninety, hundred, thousand, million

convertWord = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero" : 0,
    "ten" : 10,
    "eleven" : 11,
    "twelve" : 12,
    "thirteen" : 13,
    "fourteen" : 14,
    "fifteen" : 15,
    "sixteen" : 16,
    "seventeen" : 17,
    "eighteen" : 18,
    "nineteen" : 19,
    "twenty" : 20,
    "thirty" : 30,
    "forty" : 40,
    "fifty" : 50,
    "sixty" : 60,
    "seventy" : 70,
    "eighty" : 80,
    "ninety" : 90,
    "hundred" : 100,
    "thousand" : 1000,
    "million" : 1_000_000,
}


def calc_less_hundred(number):
    more_than_hundred = re.search(r"(hundred)|(thousand)", number)
    if more_than_hundred:
        return False
    zero = re.search(r"zero", number)
    if zero:
        return 0
    else:
        string = str(number).split("-")
        if len(string) == 1:
            return convertWord[string[0]]
        else:
            return convertWord[string[0]] + convertWord[string[1]]

def calc_less_thousand(number):
    less_hundred = calc_less_hundred(number)
    if less_hundred:
        return less_hundred
    else:
        multiplier = re.search(r"\w+(?= hundred)", number)
        if multiplier:
            hundred = convertWord[multiplier.group()] * 100
            left_over = re.sub(r"\w+(?= hundred) hundred (and )?", "", number)
            if len(left_over) > 0:
                less_hundred = calc_less_hundred(left_over)
                return hundred + less_hundred
            else:
                return hundred

def calc_less_million(number):
    more_than_thousand = re.search(r"thousand", number)

    if more_than_thousand == None:
        return calc_less_thousand(number)
    else:
        multiplier = re.search(r".+(?= thousand)", number)
        if multiplier:
            multiplier = calc_less_thousand(multiplier.group())
            num = multiplier * 1000
            less_thousands = re.search(r"(?<= thousand ).+", number)
            if less_thousands:
                less_thousands = re.sub(r"(and )?", "", less_thousands.group())
                less_thousand = calc_less_thousand(less_thousands)
                return num + less_thousand
            else: 
                return num
            
def parse_int(string):
    zero = re.search(r"zero", string)
    if zero:
        return 0
    else:
        million = re.search(r".+million", string)
        if million:
            return 1000000
        else:
            return calc_less_million(string)






# result = word_to_int("nine thousand")
# print(result)