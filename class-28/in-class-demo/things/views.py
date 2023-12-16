from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Thing
from django.urls import reverse_lazy


class ThingListView(ListView):
    template_name = 'thing_list.html'
    model = Thing
    context_object_name = 'things'


class ThingDetailView(DetailView):
    template_name = 'thing_detail.html'
    model = Thing


class ThingCreateView(CreateView):
    template_name = 'thing_create.html'
    model = Thing

    # NEW! a list of strings that represents the fields in the model
    fields = ["name", "rating", "reviewer"]


class ThingDeleteView(DeleteView):
    template_name = 'thing_delete.html'
    model = Thing
    # Why is this reverse_lazy()? https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#reverse-lazy
    success_url = reverse_lazy('thing_list')


class ThingUpdateView(UpdateView):
    template_name = 'thing_update.html'
    model = Thing
    fields = "__all__"  # this would also work in ThingCreateView
