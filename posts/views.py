from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,CreateView,DeleteView,
                                    DetailView,ListView,DeleteView)

from posts.models import POST,UPDATE
from posts.forms import NewPostForm,UpdateModelForm



"""

OPTION

"""

class Options(TemplateView):
    template_name='posts/post_option.html'


"""
post THE IMAGES

"""

class NewPost(CreateView):
    model = POST
    fields = ('new_image','Name')
    def new_post(request):

        registered = False

        if user.is_superuser():

            if request.method == 'POST':

                New_post = NewPostForm(data=request.POST)

                if New_post.is_valid():

                    post = New_post.save(commit=False)

                    if 'new_image' in request.FILES:
                        print('Found it')
                        post.New_post = request.FILES['new_image']
                    New_post.save()

                    registered=True

                else:
                    print(NewPostForm.errors)
            else:
                New_post = NewPostForm
            return render(request,'posts/new_post.html',{'New_post':NewPostForm})
        else:
            Print("You must be Superuser to access this Page")


"""

DISPLAYING THE IMAGE IN THE PAGE

"""


class DisplayImages(ListView):
    context_object_name = 'images'
    model = POST
    template_name = 'posts/display.html'

    def display_images(request):

        if request.method == 'GET':

            Images = POST.objects.all()
            return render(request,'posts/display.html',{'images':Images})

"""

#VIEW THE DETAIL OF THE IMAGES

"""

class Detail_post(DetailView):
    context_object_name = 'image_detail'
    model = POST
    template_name = 'posts/post_detail.html'


"""

DELETE THE IMAGE

"""

class Delete_image(DeleteView):
    model = POST
    success_url = reverse_lazy('posts:gallery')




"""

UPDATES

"""


class updates_create(LoginRequiredMixin,CreateView):

    form_class = UpdateModelForm
    Model = UPDATE
    template_name = 'posts/post_form.html'

class Updates_list(ListView):
    model = UPDATE

    def get_queryset(self):
        return UPDATE.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class Updates_detail(DetailView):

    model = UPDATE
    template_name = 'posts/updates_detail.html'


class Updates_delete(LoginRequiredMixin,DeleteView):
    model = UPDATE
    success_url = reverse_lazy('posts/updates_list.html')
