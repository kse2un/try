from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from aliceapp.models import Blog

# Create your views here.
def commentcreate(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect('reviewdetail', blog_id=blog.pk)
        else:
            redirect('list')
    else:
        form = CommentForm()
        return render(request, 'reviewdetail.html', {'form':form, 'blog':blog})
