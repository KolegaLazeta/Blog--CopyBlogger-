from email import message
from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Creating Post
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False) #dobijamo objekat modela
        instance.save()
        #message
        messages.success(request, 'Successfully Created')
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, 'Not Successfully Created')
    return render(request, 'post_form.html', {'form': form})

# Post(id) 
def post_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    return render(request, 'post_detail.html', {'instance': instance})

# list of all posts
def post_list(request):
    queryset = Post.objects.all()
    return render(request, 'post_list.html', {'object_list': queryset})

# updating post
def post_update(request, id):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Saved')

        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, 'Not Successfully Saved')

    return render(request, 'post_form.html', {'instance': instance, 'form': form})

# deleting post
def post_delete(request, id):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, 'Successfully Saved')
    return redirect('list')

