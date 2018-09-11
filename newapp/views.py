from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Person
from .models import Movies
from .forms import PersonForm
from .movieform import MoviesForm



def customerlist(request):
	data=Person.objects.all()
	return render(request,'customerlist.html',{'data':data})
def removeitem(request,num):
	Person.objects.filter(id=int(num)).delete()
	return redirect('/customerlist')	
def availablemovies(request):
	data =Movies.objects.all()
	return render(request,'availablemovies.html',{'data':data})	
def removemoviefromdb(request,num):
	Movies.objects.filter(id=int(num)).delete()
	return redirect('/availablemovies')	
def addcustomer(request):
	if request.method == "POST":
		form = PersonForm(request.POST)
		if form.is_valid():
			Person_item = form.save(commit=False)	
			Person_item.save()
			return redirect('/customerlist')
	else:
		form = PersonForm()
	return render(request,'forms/addform.html',{'form':form})	


def addmovies(request):
	if request.method == 'POST':
		movieform = MoviesForm(request.POST)

		if movieform.is_valid():		
			Movies_item = movieform.save(commit=False)
			Movies_item.save()
			return redirect('/availablemovies')

	else:
		movieform = MoviesForm()
	return render(request,'forms/addmovieform.html',{'movieform':movieform})	

def assignmovies(request):
	data=Person.objects.all()
	moviedata = Movies.objects.all().exclude(isRented=True)
	return render(request,'assignmovie.html',{'data':data,'moviedata':moviedata})

def giveKey(request):
	print(request.POST)
	person = request.POST["person"].split()[0]
	print(person)
	movie = request.POST["movie"]
	foundMovie=Movies.objects.get(name=movie)
	foundPerson=Person.objects.get(first_name=person)
	foundMovie.isRented=True
	foundMovie.save()
	pkMovie= foundMovie.id
	print(foundPerson.movie)
	foundPerson.movie=foundMovie
	foundPerson.save()
	return redirect('/customerlist')

def returnmovie(request):
	data = Person.objects.all().exclude(movie__isnull=True)
	return render(request,'returnmovie.html',{'data':data})


def removemovie(request,number):
	
	obj=Person.objects.get(id=int(number))
	MOobject = Movies.objects.get(name = obj.movie)
	MOobject.isRented = False
	MOobject.save()
	obj.movie = None
	obj.save()
	return redirect('/returnmovie')




