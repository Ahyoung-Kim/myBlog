from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Comment
from .forms import PostForm, CommentForm


def base(request):
    return render(request, 'base.html')


def home(request):
    # 작성한 글들을 index.html에 띄우기
    # Post 객체를 DB에서 모조리 가져오기, 'date' 내림차순으로
    posts = Post.objects.filter().order_by('-date')
    return render(request, 'index.html', {'posts': posts})


def diary(request):
    # 작성한 글들을 index.html에 띄우기
    # Post 객체를 DB에서 모조리 가져오기, 'date' 내림차순으로
    posts = Post.objects.filter().order_by('-date')
    return render(request, 'diary.html', {'posts': posts})

# 새 글 작성 폼


def post_form(request):
    # POST 요청이라면 -> 작성한 폼을 가져와서 DB에 저장하고 'home' 페이지로 이동
    if request.method == 'POST' or request.method == 'FILES':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():  # 유효성 검사
            form.save()  # DB에 저장
            return redirect('home')

    # GET 요청이라면 -> 폼을 보여줘야 함
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})


def detail(request, post_id):
    # 이때 request는 GET 요청!

    # get_object_or_404 메소드를 통해 DB에서 Post 객체 중,
    # 기본키 pk가 post_id 인 객체를 찾고 찾지 못하면 404를 반환
    post_detail = get_object_or_404(Post, pk=post_id)

    # 각 게시글의 댓글 폼 보여주어야 함
    comment_form = CommentForm()

    return render(request, 'detail.html',
                  {'post_detail': post_detail, 'comment_form': comment_form})


def comment(request, post_id):
    # CommentForm 객체 가져오기
    form = CommentForm(request.POST)

    if form.is_valid():
        # 일단은 DB에 저장하지 않고 대기하기
        finished_form = form.save(commit=False)
        # post_id에 상응하는 Post 객체를 찾고 Comment 객체의 post에 저장해야함
        # post는 Comment 객체의 외래키!
        finished_form.post = get_object_or_404(Post, pk=post_id)
        # DB에 반영
        finished_form.save()

    return redirect('detail', post_id)
