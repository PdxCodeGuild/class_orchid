from django.shortcuts import render, redirect
from . models import Item
from django.shortcuts import redirect




def index(request):
    if request.method=="POST":
        grocery_item=request.POST.get("grocery_item")

        Item.objects.create(
            grocery_item=grocery_item
        )
        return redirect("/")
    
    completed_list = Item.objects.filter(checked_item=True)
    incompleted_list = Item.objects.filter(checked_item=False)
    context={
        "incompleted_list": incompleted_list,
        "completed_list": completed_list,
    }

    return render(request, 'groceries/index.html', context)
    
def delete(request, id):
    item=Item.objects.get(id=id)
    item.delete()
    return redirect("/")    

def shopped(request, id):
    item=Item.objects.get(id=id)
    item.checked_item=True
    item.save()
    return redirect("/")
  



# Need to add more stuff into context. 
# Figure out the actual list name to manipulate the data






# def remove_item(checked_item, grocery_list):
#     if checked_item:
#         # if the label of the check box matches checked_item:
#             grocery_list.remove(checked_item)
#     return grocery_list