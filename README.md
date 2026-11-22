# ITRC Web Site

ITRC WebサイトのJekyllソースです。更新はこのリポジトリで行います。

## 主な編集箇所

```text
index.md                         # トップページ
meet/                            # 研究会用ページ
└── <開催回>/
    ├── cfp.md                   # 開催案内
    ├── cfp-demo.md              # デモ募集
    └── program.md               # プログラム
activities.md                    # 活動一覧
o/                               # 旧サイトのページ（about・itrc3〜5等）
meet/sample/                   # 編集用サンプル（HTML生成・公開対象外）
```

ページ本文はMarkdownで管理します。[編集用サンプル](meet/sample/README.md)を参照してください。`meet/sample/` はHTML生成・公開の対象外です。見出し・リンク・表・取り消し線の書き方を確認できます。

## 通常の更新フロー

1. **ITRC研究会を開催するとき**
   - `meet/sample/` を参考に、`meet/` に研究会用ページを作成します。コピーした場合は開催回・`permalink`・日時・連絡先・申込先を必ず更新します。
   - トップページ（`index.md`）と活動一覧（`activities.md`）を更新し、研究会用ページへのリンクを追加します。
   - 研究会終了後はトップページを更新し、開催予定の案内を開催済みの情報に変更します。
2. **分科会などを開催するとき**
   - トップページ（`index.md`）と活動一覧（`activities.md`）を更新します。
   - 開催案内が別のサイトにある場合は、そのページへリンクします。

トップページと活動一覧は自動更新されないため、開催情報とリンクをそれぞれ編集してください。

## ディレクトリ構成の詳細

| パス | 内容・用途 |
|---|---|
| `index.md` | トップページ。Markdownで編集 |
| `meet/<開催回>/<種別>.md` | 研究会の開催案内・プログラム・報告など |
| `activities.md` | 過去の活動一覧 |
| `n/` | 現組織の趣意書・定款・役員・入会案内 |
| `o/`、`o/about/`、`o/itrc3/`、`o/itrc4/`、`o/itrc5/`、`o/join/`、`o/rules/`、`o/symposium/` | 旧組織・各期の活動情報 |
| `project/`、`wg/`、`others/` | 各テーマのページ |
| `category/`、`author/` | 移行時に生成したカテゴリ別・著者別一覧 |
| `_layouts/default.html` | 共通のhead・ヘッダー・フッター、CSS等の読み込み |
| `_layouts/page.html` | ページの見出し・本文。`default`を継承 |
| `assets/migration.css` | 引き継いだカスタムCSSと補足スタイル |
| `contents/` | 復元した画像・PDF・資料 |
| `wp-content/`、`wp-includes/` | 旧サイトから引き継いだ画像・CSS・JS・フォント等 |
| `_config.yml` | サイト名、ビルド設定、除外対象など |
| `scripts/check_site.py` | 生成したHTMLとローカル参照先のチェック |
| `_site/` | ビルド結果。直接編集・コミットしない |
| `reports/` | ローカルのチェック結果。コミット・公開しない |

`wp-content/` や `wp-includes/` は公開資産の保存先で、WordPressを実行するための構成ではありません。既存ページから参照されるため、確認せず削除・改名しないでください。

`_posts/` は使わず、通常のページとして管理しています。

## ディレクトリの入口と自動一覧

`meet/index.md` や `meet/60/index.md` は `layout: directory` を使い、直下のページをLiquidで一覧表示します。リンク一覧はビルド時に更新されるので、手作業で追加する必要はありません。共通処理は `_includes/directory-list.html` にあります。`o/index.md` は既存の本文の末尾に一覧を追加しています。

新しい開催回には `meet/61/index.md` も作成してください。Jekyllがこのファイル自体を自動作成するわけではありません。

```yaml
---
layout: directory
title: 第61回研究会
listing_order: 61
asset_prefix: "../../"
body_class: page page-template-page-nosidebar
permalink: /meet/61/index.html
---
```

研究会一覧は `listing_order` の降順です。各回の一覧はページタイトル順です。`meet/final/index.md` は第50回と第51回の間に表示します。

## ページの書式

単独ページは `cfp.md` のようなファイルで管理し、子ページがあるディレクトリの入口は `index.md` を使います。見出し・段落・リンク・リストなどはMarkdownで記述しています。複雑な表、折りたたみ、書式やアンカーを維持する必要がある部分はHTMLを併用しています。

`<div markdown="0">` で囲んだ範囲はHTMLとして扱います。その中を編集するときはHTMLの構造を保ってください。単純な内容に整理できる場合は、囲みごと通常のMarkdownへ置き換えられます。

旧 `meet/60-cfp/` は `meet/60/cfp/`、旧 `meet/60-cf-demo/` は `meet/60/cfp-demo/` です。`meet50-*` や `meet/report/*` も同じ回数・種別の構造に整理し、重複した移転案内を統合しています。

`o/about/` や `o/join/` などの移転案内もMarkdownです。Front Matterの `redirect_to` に移転先への相対パスを指定すると、共通レイアウトが移転案内を出力します。

Jekyllでは先頭の `---` で囲むYAMLを **Front Matter** と呼びます。[公式の書式説明](https://jekyllrb.com/docs/front-matter/)

このサイトで使う主な設定は以下です。

| 項目 | 用途 |
|---|---|
| `layout: page` | 通常のページ用レイアウト |
| `title` | ページタイトルと本文見出し。本文で同じH1を重ねる必要はない |
| `asset_prefix` | **このサイト独自の設定**。出力先からサイトルートまでの相対パス |
| `body_class` | テーマの表示用クラス。新規ページは下記の例に合わせる |
| `permalink` | 出力先のパス。既存URLを維持したい場合などに指定 |

本文にLiquidを書く場合は [Liquidの説明](https://jekyllrb.com/docs/liquid/) を参照してください。

共通レイアウトでは `{{ content }}` に本文が入り、`{{ page.title }}` などでFront Matterを参照します。構造や共通リンクの変更はレイアウト、色・余白などの変更はCSSで行います。[レイアウトの説明](https://jekyllrb.com/docs/layouts/)

## 新しいページを追加する例

たとえば `meet/61/cfp.md` を作成します。日付や開催情報は実際の内容に置き換えてください。

```markdown
---
layout: page
title: "研究会の開催案内"
asset_prefix: "../../../"
body_class: page page-template-page-nosidebar
permalink: /meet/61/cfp/index.html
---

## 開催概要

ここに本文を書きます。

[トップへ](../../../index.html)
```

`_site/meet/61/cfp/index.html` に出力されます。`permalink` でソースの配置と公開URLを分けています。`cfp.md` と `cfp/index.md` など、同じ出力先を持つページを重複して置かないでください。[出力パス（Permalinks）の説明](https://jekyllrb.com/docs/permalinks/)

ページを追加しただけではトップや活動一覧にリンクは増えません。必要な掲載先を併せて編集してください。`category/`・`author/` の一覧も移行時点の内容であり、現在のJekyllビルドでは自動更新されません。

## リンク・画像・資料の扱い

サイト内は**生成後のHTMLを基準にした相対パス**を使います。たとえばソースが `meet/60/cfp.md` でも出力先は `meet/60/cfp/index.html` なので、`asset_prefix` は `../../../` のままです。公開ドメインやGitHubのリポジトリ名を本文に埋め込む必要はありません。

| 出力元 | サイトルートへの `asset_prefix` | トップへのリンク |
|---|---|---|
| `/index.html` | `""` | `index.html` |
| `/activities/index.html` | `"../"` | `../index.html` |
| `/meet/61/cfp/index.html` | `"../../../"` | `../../../index.html` |

- ページへのリンクはソースの `.md` ではなく、生成後の `index.html` を指定します。直接ファイルを開く場合にも辿れます。
- 先頭が `/` のルート相対パスは避けてください。`file://` での閲覧やサブディレクトリへの配置で参照先が変わります。
- `permalink` で出力階層を変えた場合、`asset_prefix` と本文の相対リンクもその階層に合わせます。
- 画像・PDFは `contents/` などに保存し、リンク元からの相対パスで参照します。例：研究会ページから `[資料](../../../contents/example.pdf)`。
- 外部URLは `https://` などのスキームを明示し、`//example.com/...` という書き方は避けます。
- 既存ページのファイル名や出力パスを変更すると、過去のリンクも変わるため、通常の本文更新では維持してください。

`url` と `baseurl` は現在空です。公開先依存の設定を追加する場合は、ローカル閲覧と公開後のリンクの両方を確認してください。

## Git管理と公開

### 更新・レビュー・公開のポリシー

- `main` は公開用の確定版とし、公開専用の `web` ブランチは設けません。
- 更新は作業ブランチで行い、PRでレビューしてから `main` にマージします。原則として `main` への直接pushは行いません。
- GitHubのWeb画面からの編集も可能です。その場合も作業ブランチとPRを使います。
- 本文・リンクの確認を行い、ページ追加や画像・レイアウトの変更はJekyllで生成したサイトでも確認します。
- `main` に反映した内容を、GitHub Pagesの標準ビルドで公開します。

### Git管理と公開する成果物

ページ本文、レイアウト、公開資産、設定、`Gemfile` / `Gemfile.lock`、検証スクリプト、README、既存のLICENSEをGit管理します。生成物・監査結果・キャッシュ・バックアップ・秘密情報等は `.gitignore` で除外しています。

公開する成果物は `bundle exec jekyll build` が生成する **`_site/` の中身**です。READMEや監査レポートなどは `_config.yml` の `exclude` で公開物から除いています。`.gitignore` はGit管理用であり、Jekyllの公開除外設定とは別です。

## Appendix：ローカル確認

Ruby 4.0とBundlerを用意し、cloneしたフォルダから実行してください。自動チェックにはPython 3も使用します。

```sh
bundle install
bundle exec jekyll serve --host 127.0.0.1 --port 4000
```

`Server running...` の表示後に http://localhost:4000/ を開きます。確認中はターミナルを開いたままにし、終了は `Ctrl+C` です。接続拒否になる場合は、サーバーが起動しているか、起動時にエラーが出ていないかを確認してください。

通常の本文編集は自動で再生成されます。`_config.yml` を変更した場合はサーバーを再起動してください。依存ライブラリを変更した場合は `bundle install` を実行し、`Gemfile.lock` もコミットします。

### ビルドとチェック

```sh
bundle exec jekyll build
python3 scripts/check_site.py
```

チェック結果は `reports/link-audit.json` に出力します。ページ数、HTMLへの未処理テンプレート混入、フォーム、ルート相対・旧ドメイン参照を検査し、内部の参照先ファイル欠落を集計します。`missing_links` と `missing_assets` が0であることも確認してください。

このチェックだけでは、外部サイトの接続状況、見た目やJavaScriptの実行結果までは確認できません。ブラウザでも変更ページとそこへ辿るリンクを開き、画像・資料・表示・コンソールを確認してください。
