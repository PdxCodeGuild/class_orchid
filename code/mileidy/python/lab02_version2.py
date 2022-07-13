# i created a blank numbers list that would be filled by user input
nums = []

while True:
    choice = input('Enter a number or done to quit: ')
#my first attempt of placement before i changed my location due to terminal errors i recieved
    #choice = int(choice)
    #nums.append(choice)
#i created an if statement for when the user would be finished their input i could give them their result and break the loop
    if choice == 'done':
        print(f"Your number average is: {sum(nums) / len(nums)}")
        break
# i type casted the string i recieved from the user into an integer in order to preceed with the mathematical portion
    choice = int(choice)
#here i appended the users input inside the empty list
    nums.append(choice)
