from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404
from user.models import user
from .models import Board
from .forms import BoardForm
def board_detail(requset, pk):
    try:
        board=Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다.')

    return render(requset, 'board_detail.html',{'board':board})
def board_write(requset):
    if not requset.session.get('user'):
        return redirect('/user/login/')
    if requset.method=='POST':
        form=BoardForm(requset.POST)
        if form.is_valid():
            user_id=requset.session.get('user')
            User=user.objects.get(pk=user_id)

            board=Board()
            board.title=form.cleaned_data['title']
            board.contents=form.cleaned_data['contents']
            board.writer=User
            board.save()

            return redirect('/board/list/')
    else:
        form = BoardForm()
    return render(requset, 'board_write.html',{'form':form})

def board_list(requset):
    all_boards=Board.objects.all().order_by('-id')
    page=int(requset.GET.get('p',1))
    paginator=Paginator(all_boards,2)
    boards=paginator.get_page(page)
    return render(requset,'board_list.html',{'boards':boards})