from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


#==========================
#ユーザー登録フォームを作成
#==========================
class RegisterForm(UserCreationForm):#新しくユーザーを作るためのフォーム

    #メールアドレス入力対応
    email = forms.EmailField(
        label="メールアドレス",
        required=True,
    )

    error_messages = {
        "password_mismatch":"入力したパスワードが一致しません。",

    }
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields["username"].label = "ユーザー名"
        self.fields["password1"].label = "パスワード"
        self.fields["password2"].label = "パスワード再確認"

        #Bootstrap対応
        self.fields["username"].widget.attrs.update({
            "class":"form-control",
            "placeholder":"ユーザ―名",
        })

        self.fields["email"].widget.attrs.update({
            "class":"form-control",
            "placeholder":"メールアドレス",
        })

        self.fields["password1"].widget.attrs.update({
            "class":"form-control",
            "placeholder":"パスワード",
        })

        self.fields["password2"].widget.attrs.update({
            "class":"form-control",
            "placeholder":"パスワード再確認",
        })

        #フォームのラベル・説明文を日本語化
        self.fields["username"].help_text = "150文字以内。英文字と@ / . / + / - / _ が使用できます。"

        self.fields["password1"].help_text = "パスワードは、8文字以上で、他の個人情報と異なるパスワードを設定してください。"

        self.fields["password2"].help_text = "確認のため、もう一度同じパスワードを入力してください。"
        
       

    class Meta:
        model = User
        fields=(
            "username",
            "email",
            "password1",
            "password2",
        )
#=========================================
#ログインフォームのデザインをBootstrapを対応
#=========================================
class LoginForm(AuthenticationForm):
    
    def __init__ (self, *args, **kwargs):

         #親クラスAuthenticationFormを初期化
        super().__init__(*args,**kwargs)

        #Usernameを日本語化
        self.fields["username"].label= "ユーザ―名"
        self.fields["password"].label="パスワード"

        #ユーザー名入力欄のデザインを設定
        self.fields["username"].widget.attrs.update({
            "class":"form-control",
            "placeholder":"ユーザー名",
        })

        #パスワード入力欄のデザインを設定
        self.fields["password"].widget.attrs.update({
            "class":"form-control",
            "placeholder":"パスワード",
        })

#===========================
#プロフィール編集フォーム
#===========================
class ProfileEditForm(UserChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].label = "ユーザー名"
        self.fields["email"].label = "メールアドレス"

        self.fields["username"].widget.attrs.update({
            "class":"form-control",
            "placeholder":"ユーザー名",
        })

        self.fields["email"].widget.attrs.update({
            "class":"form-control",
            "placeholder":"メールアドレス",
        })

    class Meta:
        model = User
        fields = (
            "username",
            "email",
        )