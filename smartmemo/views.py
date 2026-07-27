from django.shortcuts import render,redirect
from .models import Memo, Category
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm,ProfileEditForm  #ユーザー登録機能
from django.shortcuts import render,redirect

# Create your views here.
@login_required
def index(request):
    memos=Memo.objects.filter(user=request.user)#
    return render(request,"smartmemo/index.html",{
        "memos":memos,
    })

#フォーム作成
@login_required
def create(request):
    if request.method=="POST":
        
        title=request.POST["title"]
        content=request.POST["content"]
        category_id = request.POST.get("category")

        category = None
        if category_id:
            category = Category.objects.get(id=category_id)

        Memo.objects.create(
            user=request.user,
            title=title,
            content=content,
            category=category
        )
        return redirect("index")
    return render(request,
                  "smartmemo/create.html",
                  {
                      "categories":Category.objects.all()
                  }
                  )

#編集機能を作成
@login_required
def edit(request,memo_id):
    memo = Memo.objects.get(id=memo_id, user=request.user,)

    #更新処理を作成
    if request.method=="POST":
        
        memo.title=request.POST["title"]
        memo.content=request.POST["content"]

        memo.save()

        return redirect("index")

    return render(request,"smartmemo/edit.html",{
        "memo":memo,
    })

#削除機能を作成
@login_required
def delete(request,memo_id):
    memo=Memo.objects.get(id=memo_id, user=request.user,)

    memo.delete()
    
    return redirect("index")

#検索機能を作成
@login_required
def search(request):
    keyword = request.GET.get("keyword","")
    
    #ログインユーザーのメモだけ検索する
    memos= Memo.objects.filter(
        user=request.user
        ).filter(
            Q(title__icontains=keyword)|
            Q(content__icontains=keyword)

        )
    

    return render(
        request,
        "smartmemo/index.html",
        {
            "memos":memos,
            "keyword":keyword,
        }
    )

#カテゴリをクリックすると、そのカテゴリのメモだけを表示する
@login_required
def category(request,category_id):
    category = Category.objects.get(id=category_id)
    #ログインユーザーのメモだけ、そのカテゴリを表示する
    memos = Memo.objects.filter(user=request.user,category=category)

    return render(
        request,
        "smartmemo/index.html",
        {
            "memos":memos,
            "selected_category":category,
        }
    )

#ユーザー登録機能
def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        #入力された値が正しいか、文字数と未入力がないか。従っているかを調べる
        if form.is_valid():
            form.save() # 認証が済んだ安全なデータをＤＢに新しく書き込む。

            return redirect("login")
        
    else:
        form = RegisterForm()

    return render(
        request,
        "smartmemo/register.html",
        {
            "form": form,
        }
    )

#プロフィール画面機能
@login_required
def profile(request):
    return render(
        request,
        "smartmemo/profile.html",
        {
            "user":request.user,
        }
    )

#プロフィール編集機能
@login_required
def profile_edit(request):
    if request.method == "POST":
        form = ProfileEditForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileEditForm(instance=request.user)

    return render(request,"smartmemo/profile_edit.html", {"form": form})