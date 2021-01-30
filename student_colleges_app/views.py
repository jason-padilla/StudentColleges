from django.shortcuts import render, redirect	# notice the import!
from .models import College, Student
def index(request):
    context = {
        "colleges": College.objects.all().order_by('name')
    }
    return render(request, "index.html", context)
# show all of the data from a table
def add_student(request):
    chosen_college = College.objects.get(name = request.POST['college'])
    Student.objects.create(first_name = request.POST['first-name'],last_name = request.POST['last-name'], college = chosen_college)
    return redirect("/")

def add_college(request):
    College.objects.create(name = request.POST['college-name'],mascot = request.POST['mascot'], rank = request.POST['rank'])
    return redirect("/")