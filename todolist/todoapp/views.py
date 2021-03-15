from django.shortcuts import render,redirect,reverse
from .forms import ToDoListForm
from .models import ToDoListModel
# Create your views here.

def ToDoListView(request):
    task_list=ToDoListModel.objects.order_by("id")
    form=ToDoListForm()
    if request.method=="POST":
        form=ToDoListForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('index')

    all_data={"form":form,
                "task_lists":task_list,}

    return render(request,'todoapp/index.html',all_data)

def DeleteView(request,id):
    if request.method=="POST":
        item=ToDoListModel.objects.get(id=id)
        item.delete()
        return redirect('index')
