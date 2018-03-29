# -*-coding:utf8-*-
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

# Create your views here.

# import markdown
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, DetailView
from .models import Post, Category, Tag, Comment
from .forms import CommentForm
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


class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super(PostDetailView, self).get(request, *args, **kwargs)
        self.object.increase()
        return response


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
    template_name = 'message.html'
    context_object_name = 'msg_list'
    paginate_by = 3

    # class MessageView(View):
    #     def get(self, request):
    #         msg_list = Comment.objects.all().order_by('-created')
    #
    #         return render(request, 'message.html', {'msg_list': msg_list})
    # {% url 'blog:message_form'%}
    def post(self, request):
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

            msg_list = Comment.objects.all()
            return render(request, 'message.html', {'msg_list': msg_list})
        else:

            return render(request, '404.html')

# def show_comment_form(request):
#     msg_list = Comment.objects.all().order_by('-created')
#
#     if request.method=='POST':
#         message_form = CommentForm(request.POST)
#         if message_form.is_valid():
#             username = request.POST.get("name", "")
#             email = request.POST.get("email", "")
#             subject = request.POST.get("subject", "")
#             text = request.POST.get("text", "")
#
#             comment = Comment()
#             comment.name = username
#             comment.email = email
#             comment.subject = subject
#             comment.text = text
#
#             comment.save()
#
#             # msg_list = Comment.objects.all()
#             return render(request, 'message.html', {'msg_list': msg_list})
#         else:
#
#             return render(request, '404.html')
