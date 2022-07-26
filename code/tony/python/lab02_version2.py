nums = list()

while True:
    user_input = input('Enter a number, or type "done": ')
    if user_input == 'done': break
    else:
        try:
            user_input = int(user_input)
        except ValueError:
            continue
        nums.append(user_input)

if len(nums):
    avg = sum(nums) / len(nums)
    print(avg)