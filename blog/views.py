# -*-coding:utf8-*-
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

# Create your views here.

# import markdown
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, DetailView
from .models import Post, Category, Tag, Comment, CommentPost
from .forms import CommentForm, CommentPostForm
from django.core.mail import send_mail
from RealBlog.settings import EMAIL_FROM


# def blog(request):
#     post_list = Post.objects.all().order_by('-created_time')
#     return render(request, 'blog.html', context={'post_list': post_list})


class IndexView(ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'post_list'
    paginate_by = 4


def msg_detail(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    return render(request, 'message_detail.html', {'msg_detail': comment})


# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'detail.html'
#     context_object_name = 'post'
#
#     def get(self, request, *args, **kwargs):
#         response = super(PostDetailView, self).get(request, *args, **kwargs)
#         self.object.increase()
#         return response

# 以函数形式来展示文章信息和评论
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 这里的post. 指向建模型时的realated_name,取出可用的文章评论
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        commentpost_form = CommentPostForm(data=request.POST)
        if commentpost_form.is_valid():
            # new_comment = CommentPost()
            # new_comment.name = request.POST.get('name', '')
            # new_comment.email = request.POST.get('email', '')
            # new_comment.body = request.POST.get('body', '')
            # 调用表单save方法创建一个 评论模型,commit还没提交
            new_comment = commentpost_form.save(commit=False)
            # 把评论跟post模型关联
            new_comment.post = post

            new_comment.save()
            return redirect(post)
    else:
        commentpost_form = CommentPostForm()
    return render(request, 'detail.html', {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'commentpost_form': commentpost_form})


# 这里的pk来自url中的正则提取
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list_category = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'category.html', context={'post_list': post_list_category})


def tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    post_list_tag = Post.objects.filter(tag=tag)
    return render(request, 'category.html', context={'post_list': post_list_tag})


# class CategoryView(ListView):
#     model = Post
#     template_name = 'category.html'
#     context_object_name = 'post_list'
#
#     def get_queryset(self):
#         cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
#         return super(CategoryView, self).get_queryset().filter(category=cate)

# get_querset() 方法会默认获取全部数据，我们自己熬加上过滤器


# def show_comment(request):
class ShowComment(ListView):
    model = Comment
    queryset = Comment.objects.order_by('-created_time')
    template_name = 'message.html'
    context_object_name = 'msg_list'
    paginate_by = 3

    @staticmethod
    def post(request):
        message_form = CommentForm(request.POST)
        if message_form.is_valid():
            username = request.POST.get("name", "")
            email = request.POST.get("email", "")
            subject = request.POST.get("subject", "")
            text = request.POST.get("text", "")
            try:
                send_mail(subject, '{}{}'.format(text, email), EMAIL_FROM, ["1066493443@qq.com"])
            except:
                print('不知名邮箱错误')
            comment = Comment()
            comment.name = username
            comment.email = email
            comment.subject = subject
            comment.text = text
            comment.save()
            # msg_list = Comment.objects.all()
            # return render(request, 'message.html', {'msg_list': msg_list})
            return redirect('url')
        else:

            return render(request, '404.html')

