from django.shortcuts import render, get_object_or_404
from .models import Poll

# 심리테스트 설문지
def home(request):
    return render(request, 'aliceapp/home.html')

def q1(request):
    return render(request, 'aliceapp/q1.html')

def q1(request):
    return render(request, 'aliceapp/q2.html')
    
def q1(request):
    return render(request, 'aliceapp/q3.html')

def q1(request):
    return render(request, 'aliceapp/q4.html')

def q1(request):
    return render(request, 'aliceapp/q5.html')

def q1(request):
    return render(request, 'aliceapp/q6.html')

def q1(request):
    return render(request, 'aliceapp/q7.html')

def q1(request):
    return render(request, 'aliceapp/q8.html')

def q1(request):
    return render(request, 'aliceapp/q9.html')
    


def reviewhome(request):
    blogs = Blog.objects
    return render(request, 'aliceapp/reviewhome.html', {'blogs' : blogs})

def reviewdetail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'aliceapp/reviewdetail.html', {'blog' : blog_detail})

def reviewnew(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post.save()
            return redirect('reviewhome')
    else:
        form = PostForm()
        return render(request, 'aliceapp/reviewnew.html', {'form' : form})

def postcreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('reviewhome')
    else:
        form = PostForm()
        return render(request, 'aliceapp/reviewnew.html', {'form' : form})


def reviewedit(request):
    return render(request, 'aliceapp/reviewedit.html')

def postupdate(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=blog)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('reviewdetail', blog_id=blog.pk)
    else:
        form = PostForm(instance=blog)
        return render(request, 'aliceapp/reviewedit.html', {'form' : form})

def postdelete(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.delete()
    return redirect('reviewhome')

# 심리테스트 결과
def alice(request):
    return render(request, 'aliceapp/result_alice.html')

def rabbit(request):
    return render(request, 'aliceapp/result_rabbit.html')

def hat(request):
    return render(request, 'aliceapp/result_hat.html')

def humdum(request):
    return render(request, 'aliceapp/result_humdum.html')

def queen(request):
    return render(request, 'aliceapp/result_queen.html')

def cat(request):
    return render(request, 'aliceapp/result_cat.html')

def caterpillar(request):
    return render(request, 'aliceapp/result_caterpillar.html')

def duchess(request):
    return render(request, 'aliceapp/result_duchess.html')

def poll(request, poll_id):
    if poll_id == 9:
        return render(request, 'aliceapp/final.html')
    else:
        polls = get_object_or_404(Poll, pk=poll_id+1)
        return render(request, 'aliceapp/poll.html', {'polls' : polls})

def start(request):
    return render(request, 'aliceapp/start.html')

def final(request):
    return render(request, 'aliceapp/final.html')