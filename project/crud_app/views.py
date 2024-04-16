from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Bill


class Bill_Create(CreateView):
    model = Bill
    fields = "__all__"
    success_url = reverse_lazy("list_url")


class Bill_List(ListView):
    model = Bill


class Bill_Detail(DetailView):
    model = Bill


class Bill_Update(UpdateView):
    model = Bill
    fields = "__all__"
    success_url = reverse_lazy("list_url")



class Bill_Delete(DeleteView):
    model = Bill
    success_url = reverse_lazy("list_url")

