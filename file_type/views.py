from .models import ContentAddressable
from django.views.generic.edit import CreateView, FormView, DeleteView, UpdateView


class ContentAddressableCreate(CreateView):
    model = ContentAddressable
    fields = ['file_name', 'file_url', 'file_digest']


class ContentAddressableUpdate(UpdateView):
    model = ContentAddressable
    fields = ['file_name', 'file_url', 'file_digest']


class ContentAddressableForm(FormView):
    model = ContentAddressable
    fields = ['file_name', 'file_url', 'file_digest']


class ContentAddresableUpdate(UpdateView):
    model = ContentAddressable
    fields = ['file_name', 'file_url', 'file_digest']


class ContentAddresableDelete(DeleteView):
    model = ContentAddressable
    fields = ['file_name', 'file_url', 'file_digest']
