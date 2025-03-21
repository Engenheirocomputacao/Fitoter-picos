from django.urls import reverse_lazy
from fitoterapico.models import Fitoterapico
from fitoterapico.forms import FitoterapicoModelForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

    
class FitoterapicoListView(ListView):
    model = Fitoterapico
    template_name = 'fitoterapico.html'
    context_object_name = 'fitoterapico'

    def get_queryset(self):
        fitoterapico = super().get_queryset().order_by('nome')
        search = self.request.GET.get('search')

        if search:
            fitoterapico = fitoterapico.filter(nome__icontains=search)

        return fitoterapico




@method_decorator(login_required(login_url='login'), name='dispatch')
class NovoFitoterapicoCreateView(CreateView):
    model = Fitoterapico
    form_class = FitoterapicoModelForm
    template_name = 'novo_fitoterapico.html'
    success_url = '/fitoterapico/'



class FitoterapicoDetailView(DetailView):
    model = Fitoterapico
    template_name = 'fitoterapico_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class FitoterapicoUpdateView(UpdateView):
    model = Fitoterapico
    form_class = FitoterapicoModelForm
    template_name = 'fitoterapico_update.html'
    
    def get_success_url(self):
        return reverse_lazy('fitoterapico_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='login'), name='dispatch')
class FitoterapicoDeleteView(DeleteView):
    model = Fitoterapico
    template_name = 'fitoterapico_delete.html'
    success_url = '/fitoterapico/'