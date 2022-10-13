from django.shortcuts import render
import json

# I can use keyword logic to then filter through my api by keyword, data returned will be stored in a variable, that variable is then passed to context to be displayed on html

# create a key for each value i want (muscle), for loop looking for keyword matches and store that in an empty list?

def results(request):
    if request.method == 'POST':
        results = []
        keyword = request.POST['user_exercise_search']
        with open('exercises.json', 'r') as f:
            jsonfile = json.load(f)
        for exercise in jsonfile['exercises']:
            # print(exercise['category'])
            print(keyword)
            if exercise['category'] == int(keyword):
                results.append(exercise)
        print(results)

        
        
        

    
    context = {'results': results}

    return render(request, 'results.html', context)
# Create your views here.
