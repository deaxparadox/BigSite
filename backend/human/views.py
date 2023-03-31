from django.shortcuts import render

from .models import Human

def human_list(request):
    return render(
        request, "human/list.html", {
            "humans": Human.objects.all()
        }
    )

def human_detail(request, username):
    return render(request, 'human/detail.html', {
        "human": Human.objects.get(username=username)
    })