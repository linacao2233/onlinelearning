from django.shortcuts import render
from .models import Subjects, Videos

# Create your views here.

def index(request):
	template = 'main/index.html'

	subjects = Subjects.objects.all()


	context = {
	'subjects': subjects,
	}

	return render(request, template, context)


def VideoPerSubject(request,slug):
	template = 'main/videolist.html'

	subject = Subjects.objects.get(slug=slug)

	videolist = Videos.objects.filter(subject=subject)

	context = {
	'subject': subject,
	'videos': videolist,
	}

	return render(request, template, context)


