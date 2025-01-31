from random import randint

chosen_num = randint(1,100)
counter = 0
guesses = []
while True:
    input_given = int(input('Enter a num:'))
    guesses.append(input_given)
    counter = counter + 1
    
    if chosen_num == input_given:
        print(f'Correct Guess and it took {counter} try')
        break
    elif input_given > 100 or input_given < 1:
        print('You are Out of Bounds')
        continue
    elif counter == 1 and abs(chosen_num-input_given) <= 10:
        print('Warmerrr!!')
        continue
    elif counter == 1 and abs(chosen_num-input_given) > 10:
        print('Colderr!!')
        continue
    else:
        if counter >= 1 and abs(chosen_num-guesses[-1]) < abs(chosen_num-guesses[-2]):
            print('Getting Warmer!!!')
        else:
            print('Getting Colder!!!')
        continue
