from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .forms import PostForm


def post_create(request):
    #if not request.user.is_staff or not request.user.is_superuser:
     #   raise Http404

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # message success
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)


def post_list(request):
    posts = Post.objects.all()

    query = request.GET.get("q")

    if query:
        posts = posts.filter(category__title__icontains=query)

    paginator = Paginator(posts, 12)  # Show 25 contacts per page
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, slug):
    instance = get_object_or_404(Post, slug=slug)

    if request.GET.get('choices'):
        # prevent query on field ''
        newdata = Post.objects.filter(**{request.GET.get('choices'): \
                                                        request.GET.get('textField')})

        # this is the equivalent of running
        #     EmployeeDetails.objects.filter(keyword=request.GET['textField'])

    context = {
        "instance": instance,
    }
    return render(request, "post_detail.html", context)


def post_update(request, slug):
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "post_form.html", context)


def post_delete(request, slug):
    instance = get_object_or_404(Post, slug=slug)
    messages.success(request, "Successfully deleted!")
    instance.delete()
    return redirect("posts:list")


def book_list(request):
    posts = Post.objects.filter(category__title__icontains="Aktualności")

    query = request.GET.get("q")

    if query:
        posts = posts.filter(category__title__icontains=query)

    paginator = Paginator(posts, 12)  # Show 25 contacts per page
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'books.html', {'posts': posts})