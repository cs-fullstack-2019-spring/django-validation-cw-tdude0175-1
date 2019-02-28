from django.shortcuts import render
from django.http import HttpResponse
from .forms import NewCarForm , NewCarModel  #you can import both from forms since it exists in both
# Create your views here.


def index(request):
    carForm = NewCarForm()    # asigns each model and form to a variable
    carModel = NewCarModel.objects.all()

    if request.method == "POST":
        carForm = NewCarForm(request.POST)  #adds form information and if it is wrong it will keep the information for fixing
        if (carForm.is_valid()):
            NewCarModel.objects.create(make= request.POST['make'],model=request.POST['model'],
                                       year=request.POST['year'],mpg=request.POST['mpg'])
                                        #this adds the car and makes it an actual model
            return render(request,'carApp/congratulations.html',)
            #this renders the congratulations page
        else:
            context= \
                {
                    "form":carForm,
                    'model':carModel,  #this adds errors for rendering the page
                    'errors':carForm.errors
                }
            return render(request,'carApp/index.html',context)
    context = \
        {
            "form":carForm,
            'model':carModel    #this is for a new page and will always render both the form for a new car and all existing cars
        }
    return render(request,'carApp/index.html',context)

# only used to define access to the congratulations.html
def congrat(request):
    return render(request,'carApp/congratulations.html',)