from django.shortcuts import render, redirect

from .forms import ServicingForm
from .models import Guitar, Accessory
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

# Define the home view
def home(request):
    return render(request, 'home.html')

def guitars_index(request):
    guitars = Guitar.objects.all()
    return render(request, 'guitars/index.html', { 'guitars': guitars })

def about(request):
    return render(request, 'about.html')

def guitars_detail(request, guitar_id):
  
  guitar = Guitar.objects.get(id=guitar_id)
  id_list = guitar.accessories.all().values_list('id')
  accessories_guitar_doesnt_have = Accessory.objects.exclude(id__in=id_list)
  servicing_form = ServicingForm()
  print(guitar.servicing_set.all())
  return render(
    request,
    'guitars/detail.html',
    {
      'guitar': guitar,
      'servicing_form': servicing_form,
      'accessories': accessories_guitar_doesnt_have,
    }
  )

class GuitarCreate(CreateView):
  model = Guitar
  fields = ['make', 'model', 'year', 'cost']
  # success_url = '/guitars/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    # Let the CreateView superclass do its usual job
    return super().form_valid(form)

class GuitarUpdate(UpdateView):
  model = Guitar
  # Let's disallow the renaming of a guitar by
  # excluding the name field
  fields = ['make', 'model', 'year', 'cost']

def add_servicing(request, guitar_id):
  
  # create a FeedingForm instance using
  # the data that was submitted via the form
  form = ServicingForm(request.POST)
  # validate the form
  if form.is_valid():
    
    # can't save the form/object to the db
    # until we've assigned a cat_id
    new_servicing = form.save(commit=False)
    new_servicing.guitar_id = guitar_id
    new_servicing.save()
  return redirect('detail', guitar_id=guitar_id)
class GuitarDelete(DeleteView):
  model = Guitar
  success_url = '/guitars/'

class AccessoryList(ListView):
  model = Accessory

class AccessoryDetail(DetailView):
  model = Accessory

class AccessoryCreate(CreateView):
  model = Accessory
  fields = '__all__'

class AccessoryUpdate(UpdateView):
  model = Accessory
  fields = ['name', 'cost']

class AccessoryDelete(DeleteView):
  model = Accessory
  success_url = '/accessories/'

def assoc_accessory(request, guitar_id, accessory_id):
  Guitar.objects.get(id=guitar_id).accessories.add(accessory_id)
  return redirect('detail', guitar_id=guitar_id)