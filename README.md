# ITRC Web Site — 2026-11-20 XMLからの再生成

`itrcwebsite.WordPress.2026-11-20.xml` の公開記事・固定ページ222件を元にしたJekyllサイトです。カテゴリ・著者別一覧29ページを含み、XML由来の251ページを生成します。元サイトからの復元ページ38件を加え、現在は合計289ページです。

## ローカル確認

Ruby 4.0とBundlerがある環境で、このフォルダから実行します。

```sh
bundle install
bundle exec jekyll serve --host 127.0.0.1 --port 4000
```

`Server running...` の表示後に http://localhost:4000/ を開きます。終了は `Ctrl+C` です。
HTMLだけ生成する場合は `bundle exec jekyll build`。出力先は `_site/` で、`_site/index.html` の直接閲覧にも対応しています。

## 編集と構成

- トップ：`index.md`
- 各ページ：該当フォルダの `index.html`
- 共通HTML：`_layouts/default.html`、`_layouts/page.html`
- 旧テーマのスタイル：`wp-content/themes/simpler/`
- XMLのカスタムCSSと補足スタイル：`assets/migration.css`
- `url` と `baseurl` は空。公開先のドメイン・リポジトリ名に依存しない相対リンクを使用。
- 本文HTMLの `{% raw %}` / `{% endraw %}` はLiquid誤解釈防止用。編集時に残してください。

## 今回の処理

- 11月20日XMLの公開本文を使用。旧版との本文差分比較は実施していません。
- 下書き、管理用投稿、コメントデータ、著者メールアドレスなどの管理メタデータは生成対象外。
- 原本XMLを保持したまま、XMLとして不正な制御文字1文字を読み込み時に除去。
- サイト内リンクを相対化し、外部のプロトコル省略URLはHTTPS化。
- トップに残る旧第60回研究会リンクを、実在する `meet/60-cfp/index.html` に修正。
- WordPress依存のコメント・検索フォーム、API/feed検出タグ、絵文字ローダーを出力しない構成。
- 折りたたみショートコード31件をHTMLの `details` / `summary` に変換。
- 過去のHTML本文は再利用せず、旧版の共通レイアウトとダウンロード済み画像・CSS等だけを再利用。
- XMLの添付ファイル12件はローカルに存在することを確認。
- 上流リポジトリ：`git@github.com:itrcnet/www.itrc.net.git`。公開先設定・DNS変更はこのソース準備には含みません。
- robots.txtは公開方針未指定のため未配置。旧レビューサイトの巡回拒否設定は引き継いでいません。

## 検証と残課題

```sh
bundle exec jekyll build
python3 scripts/check_site.py
```

検証結果は `reports/link-audit.json` に生成します。`reports/` はローカルの監査用で、Git管理・サイト公開の対象外です。取り込み・外部リンク監査の詳細記録も移行作業用フォルダにのみ保持しています。
元サイトから取得できる欠落資料・画像・ページを復元しました。元サイトでも404だった13種類・25箇所の内部リンクは、本文を保持してリンクを解除しました。元URLは `reports/unavailable-urls.txt`、変更箇所は `reports/internal-link-cleanup.json` に記録しています。欠落画像は0件です。
実ブラウザでの表示とコンソールの確認は未実施です。

トップのXML原文にある「2026年5月下旬」「第61回研究会(meet60)」はそのまま保持しています。公開前に日付・研究会番号を確認してください。

XMLからの再生成スクリプトと原本XMLはローカルの移行作業用フォルダに保持し、このリポジトリには含めていません。通常の編集・Jekyllビルドには不要です。

2026-11-21: 元サイトから `contents/organizational_diagram_ITRC3.gif` と `contents/shimojo_ITRC3.jpg` を取得・復元。再生成用にも `migration-20261120/recovered-assets/` に保存しています。

2026-11-21: 元サイト内の欠落参照をクロールし、追加で96ファイル（PDF43、HTML38、JPEG14、テキスト1）を復元。HTMLには移転先へ案内するローカルページも含みます。取得結果は `reports/crawl.json` に記録。旧版との本文差分比較は行っていません。

内部リンク整理：外部リンクは今回の確認・変更の対象外です。再生成時にも `migration-20261120/internal-link-fixes.json` の判断を適用します。

外部リンク整理：監査結果とユーザー判断に基づき未達リンクを解除。`ricc.itrc.net` と `lsnl.jp` 配下は指示により維持、東大キャンパスマップはユーザー確認済みとして維持しています。詳細は `reports/external-link-decisions.json` と `reports/external-links-outside-o.md` を参照してください。

## Git管理対象

ページ本文、レイアウト、CSS・画像・PDF等の公開資産、Jekyll設定、Gemfile / Gemfile.lock、検証スクリプト、README、既存のLICENSEを管理します。生成物 `_site/`、監査結果 `reports/`、キャッシュ、バックアップ、WordPress原本やDBダンプは含めません。
