# SmartMemo Ver5.0

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

- プロフィール画面にアイコン追加
![ProfileIcon](screenshots/profile_icon_v5.0.png)

- プロフィール編集にアイコン変更機能を追加
![Edit](screenshots/edit_v5.0.png)


## Ver5.0 更新内容
- プロフィール画像アップロード機能を追加

# バックエンド
- Profileモデルを新規作成
UserとOneToOneFieldで関連付け
ImageFieldでプロフィール画面を保存
マイグレーションを実行

- settings.pyへメディアファイル設定を追加
MEDIA_URL
MEDIA_ROOT
urls.pyにstatic()を追加し、アップロード画像を配信
signals.pyを作成
- 新規ユーザー登録時にProfileを自動生成
apps.pyのready()でシグナルを読み込み
views.pyにProfileImageFormを作成
profile_edit ビューを修正
Profile.objects.get_or_create()を使用し、即存ユーザーにも対応

## フロントエンド
- profile_edit.html
画像アップロード欄を追加
- profile.html
プロフィール画面を丸型で表示

## デバッグしたこと
- makemigrationsの「No changes detected」（保存忘れ）
- apps.pyのready()インデントミス
- ImportError（forms.py未保存）
- RelatedObjectDoesNotExist（既存ユーザーにProfileがない）→ get_or_createで解決
- profile_edit関数が誤って2つ定義されていた → 統合
- enctype="multipart/form-data"の付け忘れ
- card-bodyのdiv閉じタグ位置ミス
- **MEDIA_ROOT**未設定時に画像がプロジェクトルート直下に保存されていた問題 → mediaフォルダを作成し、profile_iconsを正しい場所へ移動して解決

## 改善したこと
- UUID対策：日本語ファイル名によるトラブルを防ぐため、アップロード時にランダムな英数字名へ自動変換する処理を追加
- UIの整理：Djangoのデフォルト表示（"Currently", "Clear", "Change"の英語表記）をやめ、画像プレビュー＋シンプルなファイル選択欄に作り替え
- CSS整理：インラインstyleだった画像の枠線・サイズ指定を、style.cssの.profile-icon / .profile-icon-largeクラスにまとめて管理しやすくしました。


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

  
