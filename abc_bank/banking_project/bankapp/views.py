from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ApplicationForm
from .models import District, Branch, Application


# Create your views here.


def index(request):
    districts = District.objects.all()
    return render(request, "index.html", {'district': districts})


def home(request):
    districts = District.objects.all()
    try:
        if request.method == "POST":
            email_address = request.POST['email_address']
            application2 = get_object_or_404(Application, email_address=email_address)
            if application2:
                return render(request, "application_detail.html", {'district': districts, 'application2': application2})
            else:
                messages.info(request, "Application not found.")
                return redirect("bankapp:home")
        else:
            return render(request, "home.html", {'district': districts})
    except:
        messages.info(request, "Application not found.")
        return redirect("bankapp:home")


def application(request):
    districts = District.objects.all()
    form = ApplicationForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        messages.info(request, "Application Submitted Successfully")
        return redirect('bankapp:application')
    return render(request, "application.html", {'form': form, 'district': districts})


def getBranch(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id)
    branch_option = [{'id': branch.id, 'branch': branch.branch} for branch in branches]
    return JsonResponse(branch_option, safe=False)