from django.shortcuts import render, get_object_or_404, redirect
from .models import Expenditure
from .forms import ExpenseForm


# Create your views here.
def list_expense(request):
    expenses = Expenditure.objects.all()
    return render(request, 'expense/expense_list.html',{"expenses": expenses})

# now i will try to convert this into class based generic views and then after RESTaPI



def create_expense(request):
        if request.method == "POST":
            form = ExpenseForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect("expense_list")
        else:
            form = ExpenseForm()
         
        return render(request, 'expense/expense_form.html', {"form": form})

def update_expense(request, pk):
    expenses = get_object_or_404(Expenditure, pk=pk)

    if request.method =="POST":
        form = ExpenseForm(request.POST, request.Files, instance=expenses)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
        
    else:
         form = ExpenseForm(instance = expenses)
         
    return render(request, 'expense/expense_form.html', {"form": form})

def delete_expense(request, pk):
     expenses =get_object_or_404(Expenditure, pk =pk)

     if request.method =="POST":
          expenses.delete()
          return redirect('expense_list')
     return render(request, 'expense/confirm_expense_delete.html', {"expenses": expenses })