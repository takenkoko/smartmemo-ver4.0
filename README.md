# SmartMemo Ver4.0

### Where Notes Meet Code.

開発期間：2026年6月中旬～継続開発中

> 単なるメモアプリではなく、「メモWrite・コードCode・実行Run」を一つの場所で管理できる
> ハイブリッドメモ帳を目指して開発しています。

##　開発の歩み
※後ほど作成する予定

【アプリのスクリーンショット】

- ログイン画面
![SmartMemo](screenshots/login_v4.0.png)

- メイン画面
![SmartMemo](screenshots/main_v4.0.png)

- ログイン失敗時のアラート画面
![SmartMemo](screenshots/Error(1)_v4.0.png)

- ユーザー登録画面
![Register](screenshots/register_v4.0.png)

- ユーザー登録パスワードが一致しないときアラート画面
![password Error](screenshots/password_error_v4.0.png) 

- プロフィール画面
![Profile](screenshots/profile_v4.0.png)

- パスワード変更画面
![PasswordChange](screenshots/password_change_v4.0.png)

- アカウント削除画面
![AccountDelete](screenshots/delete_v4.0.png)

Django・Bootstrap・CSSで構築したシンプルなメモ管理Webアプリです。

## Ver4.0 更新内容
-  ユーザー登録（Sign Up）機能を追加
- UserCreationForm をカスタマイズ
-  RegisterForm を作成
- ユーザー登録画面を作成
- Bootstrap対応登録フォーム
- ログイン画面・登録画面のUIを統一
- ラベル・help_text を日本語化
- ログイン画面に「新規登録はこちら」を追加
- `{{ form.as_p }}` を卒業し、フォームを手動で作成
- 新たにナビゲーションバーの色を変更
- プロフィール画面（表示・編集）を追加
- ユーザー登録時にメールアドレス入力欄を追加
- パスワード変更機能を追加（PasswordChangeView + カスタムフォームで日本語化）
- アカウント削除機能を追加（パスワード確認・確認ダイアログ付き）



## Features(主な機能)
- Create memo
- Edit memo
- Delete memo
- Search memo
- Category support
- Category badges
- User registration (Sign Up)
- User authentication (Login / Logout)
- User-specific memo management
- Profile view / edit
- Password change
- Account deletion
- Bootstrap UI

## Tech Stack
- Python
- Django
- Bootstrap 5
- CSS
- SQLite 
- Git
- GitHub

## Future Plans
- PostgreSQL migration
- Responsive UI improvements
- Markdown support
- Code syntax highlighting
- Dark mode


## 開発メモ
SmartMemoは、Djangoの学習とWebアプリケーション開発の理解を目的として開発しています。

現在も継続的に機能追加・改善を行い、バージョンアップを続けています。

将来的には、通常のメモだけでなく、コードも保存・管理できるメモアプリへ発展させる予定です。

  
