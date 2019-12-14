from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from webapp.forms import ImageForm
from webapp.models import Image


class IndexView(ListView):
    model = Image
    template_name = 'index.html'
    context_object_name = 'photo_list'
    ordering = '-created_at'


class PhotoView(DetailView):
    model = Image
    template_name = 'photo/view.html'
    context_object_name = 'photo'


class PhotoCreateView(LoginRequiredMixin,CreateView):
    model = Image
    template_name = 'photo/create.html'
    form_class = ImageForm

    def get_success_url(self):
        return reverse('webapp:photo_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        self.object = Image.objects.create(author=self.request.user, photo=form.cleaned_data['photo'],
                                           sign=form.cleaned_data['sign'])

        return HttpResponseRedirect(self.get_success_url())


class PhotoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Image
    template_name = 'photo/update.html'
    form_class = ImageForm
#    fields = ('name', 'category', 'photo', 'description')
    context_object_name = 'photo'
    permission_denied_message = 'Access Denied!'
    permission_required = 'webapp.change_image'

    def has_permission(self):
        image = Image.objects.get(pk=self.kwargs['pk'])
        if image.author == self.request.user or super().has_permission():
            return True

    def get_success_url(self):
        return reverse('webapp:photo_detail', kwargs={'pk': self.object.pk})


class PhotoDeleteView(PermissionRequiredMixin, DeleteView):
    model = Image
    template_name = 'photo/delete.html'
    success_url = reverse_lazy('webapp:index')
    context_object_name = 'photo'
    permission_denied_message = 'Access Denied!'
    permission_required = 'webapp.delete_image'

    def has_permission(self):
        image = Image.objects.get(pk=self.kwargs['pk'])
        if image.author == self.request.user or super().has_permission():
            return True



