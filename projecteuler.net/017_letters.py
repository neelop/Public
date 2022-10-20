numbers = {"0": "", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven",
           "8": "eight", "9": "nine"}
teens = {"10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen", "15": "fifteen",
         "16": "sixteen", "17": "seventeen", "18": "eighteen", "19": "nineteen"}
tens = {"0": "", "2": "twenty", "3": "thirty", "4": "forty", "5": "fifty", "6": "sixty", "7": "seventy", "8": "eighty",
        "9": "ninety"}

number_list = [str(i) for i in range(1, 1001)]

score = 0
for word in number_list:
    word_count = 0
    if len(word) == 1:
        word_count += len(numbers[word])
    elif len(word) == 2:
        if word[0] == "1":
            word_count += len(teens[word])
        else:
            word_count += len(tens[word[0]] + numbers[word[1]])
    elif len(word) == 3:
        if word[1] == "0" and word[2] == "0":
            pass
        elif word[1] == "1":
            word_count += len("and" + teens[word[1:]])
            print("and" + teens[word[1:]])
        else:
            word_count += len("and" + tens[word[1]] + numbers[word[2]])
            print("and" + tens[word[1]] + numbers[word[2]])
        word_count += len(numbers[word[0]] + "hundred")
        print(numbers[word[0]] + "hundred\n", word_count,"\n")
    elif len(word) == 4:
        word_count += len("onethousand")

    score += word_count

print(score)
