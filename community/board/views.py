from django.shortcuts import render, redirect
from user.models import user
from .models import Board
from .forms import BoardForm
def board_detail(requset, pk):
    board=Board.objects.get(pk=pk)
    return render(requset, 'board_detail.html',{'board':board})
def board_write(requset):
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
    boards=Board.objects.all().order_by('-id')

    return render(requset,'board_list.html',{'boards':boards})