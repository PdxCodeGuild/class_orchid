# Exercise 1

teachers = [
    {
        'name': 'Lisa',
		'city': 'Portland',
		'job': 'programmer',
		'computer': 'windows',
		'cat': 'Heather'
    },
    {
        'name': 'Pete',
        'city': 'Portland',
        'job': 'programmer',
        'computer': 'Mac',
    },
]
keys = ['name', 'city', 'job', 'computer', 'cat', 'mansion']
for teacher in teachers:
    print(teacher)
    for key in keys:
        try:
            print(f'Their {key} is {teacher[key]}')
        except KeyError:
            print(f'They have no {key}')
        

# Exercise 2


def add(x, y):
    return x + y


test_inputs = [
    (2, 2), # 4 
    ('2', '2'), # '22' bug
    (2, '2'), # TypeError 2 + '2'
    ('two', 2), # TypeError 'two' + 2
    # previous line becomes a ValueError after using int
    # ValueError: invalid literal for int() with base 10: 'two'
]

for nums in test_inputs:
    try:
        print(f'values: {nums[0]}, {nums[1]}')
        result = add(int(nums[0]), int(nums[1]))
        print(result)
    except TypeError as e:
        print('TypeError')
        print(e)
    except ValueError as e:
        print('ValueError')
        print(e)

