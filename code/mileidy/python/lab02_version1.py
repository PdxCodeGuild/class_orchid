nums = []

while True:
    choice = input('Enter a number or done to quit: ')

    if choice == 'done':
        print(f"Your number average is: {sum(nums) / len(nums)}")
        break