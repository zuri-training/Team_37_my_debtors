from django.shortcuts import render
from django.views import generic
from .models import Debtors
from .form import DebtorForm
from django.urls import reverse_lazy


# Create your views here.
class HomePage(generic.TemplateView):
    template_name = 'index.html'


# search debtors by first or last name
def searchDebtor(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    debtors_list = Debtors.objects.filter(first_name__icontains=q, last_name__icontains=q).order_by('-student_id')
    context = {'debtors_list': debtors_list}
    return render(request, 'home.html', context)


# Update data of added debtors - only by the school admin who initially added it
class UpdateDebtor(generic.UpdateView):
    model = Debtors
    form_class = DebtorForm
    template_name = 'update_post.html'


# Delete debtor after payment is made - only by the school admin who initially added it
class DeleteDebtor(generic.DeleteView):
    model = Debtors
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

