from django.shortcuts import render
from django.http.response import HttpResponse
from .models import FeedbackData
from .forms import FeedbackForm
import datetime as at
date1=at.datetime.now()

def Feedback_view(request):
    if request.method=="POST":
        ffrom=FeedbackForm(request.POST)
        if ffrom.is_valid():
            name=request.POST.get('name','')
            rating=request.POST.get('rating','')
            location=request.POST.get('location','')
            feedback=request.POST.get('feedback','')
            data=FeedbackData(
                name=name.capitalize(),
                rating=rating,
                date=date1,
                location=location,
                feedback=feedback
            )
            data.save()
            ffrom=FeedbackForm()
            feedbacks=FeedbackData.objects.all()
            return render(request,"feedback.html",{'fform':ffrom,'feedbacks':feedbacks})
        else:
            return HttpResponse("Invalid User Data")
    else:
        feedbacks=FeedbackData.objects.all()
        fform=FeedbackForm()
        return render(request,"feedback.html",{'fform':fform,'feedbacks':feedbacks})
