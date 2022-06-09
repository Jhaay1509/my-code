list_of_jokes = (
    "I attended a court wedding of a goat and Cow",
    "After the flood, Noah was so scared to walk on land"
    "My 85 years grandma won the marathon",
    "Programmers act like they are cool, meanwhile they are only shy",
    "I am a super dancer only in my closet",
    "My boss thinks I want to be an Accountant"
)

counter = 0
counts = 5
while True:
    
    value = input("Choose any number between 1-6 and get a joke ")
    
    if not value.isdigit() :
        print('not an integer please type a number between 1-6 ')
        continue

    value = int(value)

    if value not in range(1, 7) :
        print('number out of range please type a number between 1-6')
        continue
    
    print(list_of_jokes[value - 1])

    counter += 1
    if counter == counts :
        print('End of Jokes')
        break