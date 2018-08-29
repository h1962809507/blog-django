from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post

from .models import Comment
from .forms import CommentForm

# Create your views here.


def post_comment(request, post_pk):

    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            # 数据如果合法储存到数据库
            comment = form.save(commit=False)  # 只创建模型，不保存
            comment.post = post
            comment.save()  # 保存
            return redirect(post)

        else:
            # 数据如果不合法，重新渲染详情页，并渲染表单的错误
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
            }
            return render(request, 'blog/detail.html', context=context)
    # 不是post请求，说明没有提交数据，重新定向到文章详情页
    return redirect(post)
