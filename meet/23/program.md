---
layout: page
title: meet23 program
asset_prefix: "../../../"
body_class: page page-template-page-nosidebar
permalink: "/meet/23/program/index.html"
---

ITRC meet23 プログラムの詳細です。

## 1 日目 (2008 年 5 月 15 日 (木))

### 10:30 〜 10:45 ベンチャービジネスラボラトリー 3F ベンチャーホール

#### オープニング

### 10:45 〜 12:15 ベンチャービジネスラボラトリー3F ベンチャーホール

#### NGN 分科会セッション 担当: NGN 分科会

NGN 分科会 チェア: 笹部 昌弘

<div markdown="0">
<ol>
  <li>
    <div class="title">ローカルリルート方式による AS 間経路制御安定性向上について</div>
    <div class="authors">鈴木孝明、鈴木一哉、柳生智彦、地引昌弘 (NEC)</div>
    <div class="abstract">インターネットバックボーンにおける AS 間経路制御プロトコルとして、BGP-4 が用いられている。現在、AS 間ネットワークでは、1 日に 50 万件以上もの BGP メッセージが流れている。経路制御メッセージの増加により、ルータ負荷の増加、さらに、パス情報の頻繁な更新によるネットワークの不安定化が問題となっている。経路制御メッセージの増加原因の一つに、ネットワーク障害によるパス情報更新のための経路制御メッセージ送信が考えられる。本発表では、ネットワーク障害によって経路制御メッセージ数が増大する問題を緩和するため、障害が発生したローカルなエリアでパス情報の更新を行う LR-BGP (Local RerouteBGP) を提案する。LR-BGP は各宛先に対してローカルに代替パスを選出し、代替パス沿いのみに経路制御メッセージを送信することでメッセージ数を削減する。シミュレーション評価の結果、ネットワーク全体として、経路制御メッセージ数が平均で 50% 以上、最大で約 80% 削減できることを検証した。また、ネットワークトポロジーが効果に与える影響についても検証を行った。</div>
  </li>
  <li>
    <div class="title">センサネットワークのための進行波型通信機構</div>
    <div class="authors">谷口義明、若宮直紀、村田正幸 (大阪大学)</div>
    <div class="abstract">我々の研究グループでは、ノード間、ネットワーク間、さらにレイヤ間の相互作用を通じて自己組織的にネットワークシステム全体が制御される、拡張性、柔軟性、頑健性を有する自己組織型新世代ネットワークアーキテクチャを提案している。本報告では、基本となる非線形制御の一つであるパルス結合振動子モデルを応用した、自己組織型センサ情報収集機構を提案している。提案機構は、複数のセンシング機能を有するセンサノードからなるセンサネットワークを対象に、センシング対象やセンシング状況に応じた柔軟な情報収集を実現する。シミュレーションにより提案機構の有効性を示す。</div>
  </li>
  <li>
    <div class="title">iSCSI 複数コネクション多重度制御機構の設計と実装</div>
    <div class="authors">井上史斗、大崎博之、野本義弘、今瀬真(大阪大学)</div>
    <div class="abstract">本報告では、広域・広帯域ネットワークにおいて、iSCSI のスループットを最大化する複数コネクションの多重度制御機構 iSCSI-APT (iSCSI with  Automatic Parallelism Tuning) を提案するとともに、その有効性を実験によって示す。近年、SAN (Storage Area Network) を構築するためのプロトコルとして、コストの低さ・既存のインフラ流用の容易さなどから iSCSI が注目されている。しかし、広域・広帯域ネットワークにおいて iSCSI のスループットが低下するという問題が指摘されている。iSCSI は、一つの iSCSI セッション内に複数のコネクションを確立しデータ転送を行なう複数コネクション機能をサポートする。しかし、これが有効に機能するためには、複数コネクションの多重度をネットワーク環境に応じて適切に設定しなければならない。そこで本稿では、ネットワーク環境に応じて複数コネクションの多重度を自動的に調整する機構 iSCSI-APT を提案する。さらに、実装した iSCSI-APT を用いた実験により、iSCSI-APT は iSCSI スループットを最大化できることを示す。</div>
  </li>
</ol>
</div>

### 10:45 〜 12:15 ベンチャービジネスラボラトリー3F ミーティングルーム

#### 研究発表セッション 担当: PC

研究発表 チェア: 曽根 秀昭

<div markdown="0">
<ol>
  <li>
    <div class="title">仮想計算機の複製に基づく規模適応性に優れたサーバ構築システムの設計と実装</div>
    <div class="authors">神屋郁子、下川俊彦 (九州産業大学)</div>
  </li>
  <li>
    <div class="title">大規模キャンパス無線 LAN の構成と機器の要件</div>
    <div class="authors">大和純一 (東北大)、若山永哉 (東北大)、渡邊義和 (NEC)、後藤英昭 (東北大)、山野悟 (NEC)、曽根秀昭 (東北大)</div>
  </li>
  <li>
    <div class="title">テストベッドネットワーク再構成における経路制御方法の検討</div>
    <div class="authors">中村一彦 (NICT)、山本成一 (東京大学)、小林和真 (倉敷芸術科学大学)、下條真司 (NICT)、曽根秀昭 (東北大学)</div>
  </li>
  <li>
    <div class="title">信頼性 99.9999% に向けて、ネットワーク機器における機能と実装</div>
    <div class="authors">森 工 (ジュニパーネットワークス)</div>
  </li>
</ol>
</div>

### 12:15 〜 13:15 ベンチャービジネスラボラトリー 3F ミーティングルーム

#### 昼食/運営委員会 (ITRC 運営委員のみ)

### 13:15 〜 14:45 情報連携基盤センター (ITC) 4F 演習室

#### UAI 分科会セッション 担当: UAI 分科会

UAI 分科会「UAI セミナー」

<div markdown="0">
<ol>
  <li>
    <div class="title">Web アクセシビリティ概論</div>
    <div class="authors">渡辺隆行 (東京女子大学)</div>
  </li>

  <li>
    <div class="title">アクセシブルなコンテンツ、ナビゲーション、フォーム</div>
    <div class="authors">山口俊光</div>
  </li>

  <li>
    <div class="title">WCAG 2.0 最新情報</div>
    <div class="authors">梅垣正宏</div>
  </li>
  <li>
    <div class="title">JIS X 8341-3 改正の方針</div>
    <div class="authors">渡辺隆行 (東京女子大学)</div>
  </li>
</ol>
</div>

詳細は UAI セミナーのページを御覧ください。14:45 以降は引き続き UAI セミナーを併催いたします。

### 14:45 〜 15:30 ベンチャービジネスラボラトリー 3F ベンチャーホール (展示内容紹介)、ベンチャービジネスラボラトリー 3F ベンチャーホールラウンジスペース (デモ展示)

#### デモ展示紹介 担当: PC/LA

デモ展示団体一覧

- 有限会社シー・オー・コンヴ
- 日本電気株式会社
- SAMTK マルチプラットフォーム対応多地点間通信基盤ソフトウェア 名古屋大学大学院工学研究科電子情報システム専攻
- サン・マイクロシステムズ株式会社

### 15:30 〜 17:30

#### [招待講演セッション] 担当: PC/LA

※このセッションは情報処理学会 CMS 研究グループとの共催です。

オープン時代における大規模組織のアイデンティティ管理

<div markdown="0">
<ol>
  <li>
    <div class="title">趣旨・講演者紹介</div>
    <div class="authors">梶田将司 (名古屋大学)</div>
  </li>
  <li>
    <div class="title">IC カードを核とした名古屋工業大学におけるアイデンティティ管理 〜1 年間の運用から〜</div>
    <div class="authors">齊藤彰一 (名古屋工業大学情報基盤センター 准教授)</div>
    <div class="abstract">
      <ul>
        <li>ID として IC Card 導入</li>
        <li>文部科学省特別研究経費の支援により実施</li>
        <li>製品ベース (Sun Java IdM) のアイデンティティ管理</li>
        <li>講演者の齊藤氏は、名古屋工業大学の ID 管理システムにおいて、プロビジョニングを含むすべての事項を一手に担当されている専門家である</li>
        <li>参考 URL</li>
        <ul>
          <li>http://www.ssn.nitech.ac.jp/~shoichi/</li>
          <li>http://www2.itc.nagoya-u.ac.jp/pub/pdf/pdf/vol06_04/317_319salon.pdf</li>
        </ul>
      </ul>
    </div>
  </li>
  <li>
    <div class="title">名古屋大学におけるアイデンティティ管理 -生涯 ID としての名古屋大学 ID-</div>
    <div class="authors">内藤久資 (名古屋大学多元数理科学研究科・情報連携統括本部)</div>
    <div class="abstract">
      <ul>
        <li>講演者の内藤氏は、学内統一認証基盤の構築を黎明期から取り組み、CAS^2 (Central Authentication and Authorization Service) の研究開発等、実践的な研究開発を実施</li>
        <li>生涯 ID として名古屋大学 ID の導入</li>
        <li>オープンソースベース・独自対応ベースのアイデンティティ管理</li>
        <li>参考 URL</li>
        <ul>
          <li>http://ci.nii.ac.jp/naid/110004734709/</li>
          <li>http://www.internetconference.org/ic2007/PDF/regular-paper/naito-hisashi.pdf</li>
        </ul>
      </ul>
    </div>
  </li>
  <li>
    <div class="title">戸籍の電子化にあたっての名前表記問題</div>
    <div class="authors">竹中稔 (富士ゼロックスシステムサービス株式会社公共システム事業部)</div>
    <div class="abstract">
      <ul>
        <li>戸籍における名前表記の問題の現状と課題を整理</li>
        <li>講演者の竹中氏は、公共システムの現場において直面している問題に詳しい</li>
      </ul>
    </div>
  </li>
  <li>
    <div class="title">討論</div>
    <div class="authors">チェア: 梶田将司</div>
  </li>
</ol>
</div>

### 18:00 〜 20:00 グリーンサロン東山 レストラン花の木

#### レセプション

## 2 日目 (2008 年 5 月 16 日 (金))

### 9:00 〜 10:30 ベンチャービジネスラボラトリー3F ベンチャーホール

#### RIBB 分科会 ミーティング 担当: RIBB 分科会

一般の方の参加はできません。

### 9:00 〜 10:30 文系総合館 7F オープンホール

#### CIS/INI 分科会合同セッション 担当: CIS/INI 分科会

※このセッションは情報処理学会 CMS 研究グループとの共催です。

<div markdown="0">
<ol>
  <li>
    <div class="title">キャンパス情報システムの属性連携フレームワークの検討状況</div>
    <div class="authors">秋山豊和、岡村真吾、寺西裕一</div>
  </li>
  <li>
    <div class="title">大学間無線 LAN ローミングのためのリソースアクセス制御手法</div>
    <div class="authors">後藤英昭、渡邊義和、曽根秀昭</div>
  </li>
  <li>
    <div class="title">IC カード職員証および学生証の発行と氏名表記問題について</div>
    <div class="authors">久保仁、内藤久資</div>
  </li>
  <li>
    <div class="title">シングルサインオンに対応した遠隔地からの電子ジャーナル利用事例</div>
    <div class="authors">山本哲也</div>
  </li>
  <li>
    <div class="title">不正抑止を考慮した出席確認システムに関する基礎的検討</div>
    <div class="authors">河田貴司、湯瀬裕昭、吉田雄紀</div>
  </li>
</ol>
</div>

午後は引き続き CMS 研究会を併催いたします。プログラムの詳細は CMS 研究会へお問い合わせください。

### 10:45 〜 12:15 ベンチャービジネスラボラトリー 3F ベンチャーホール

#### RIBB 分科会セッション 担当: RIBB 分科会

RIBB 分科会 チェア: 中川郁夫

<div markdown="0">
<ol>
  <li>
    <div class="title">オーバレイによる地域 IX の効果の一例</div>
    <div class="authors">大石憲且 (NPO 法人 北海道地域ネットワーク協議会)</div>
  </li>
  <li>
    <div class="title">複数のアプリケーションを導入することによるブロードバンド整備</div>
  </li>
  <li>
    <div class="title">ラスト 1 マイル問題への挑戦</div>
    <div class="authors">菊池豊 (高知工科大学)</div>
  </li>
  <li>
    <div class="title">山梨県情報ハイウェイの民間運用</div>
    <div class="authors">羽田友和 (株式会社デジタルアライアンス)</div>
  </li>
</ol>
</div>

### 12:15 〜 13:15

#### 昼食

### 13:15 〜 14:45 ベンチャービジネスラボラトリー 3F ベンチャーホール

#### [特別セッション] 担当: NICT

新世代ネットワーク + JGN2plus (Overlay の概要) 中尾彰宏 (NICT/東京大学)

<div markdown="0">
<ol>
  <li>
    <div class="title">JGN2plus の現状</div>
    <div class="authors">下條真司 (NICT/大阪大学)</div>
  </li>
  <li>
    <div class="title">PlanetLab Research Activities</div>
    <div class="authors">中尾彰宏 (NICT/東京大学)</div>
  </li>
  <li>
    <div class="title">PlanetLab Applications and Federation</div>
    <div class="authors">中内清秀 (NICT)</div>
  </li>
</ol>
</div>

### 15:00 〜 16:30 ベンチャービジネスラボラトリー 3F ベンチャーホール

#### [特別セッション] 担当: NICT

新世代ネットワーク + JGN2plus (Overlay の概要) 中尾彰宏 (NICT/東京大学)

<div markdown="0">
<ol>
  <li>
    <div class="title">Overlay Weaver とその PlanetLab 上での運用</div>
    <div class="authors">首藤一幸 (ウタゴエ/NICT)</div>
  </li>
  <li>
    <div class="title">オーバーレイネットワークを用いたトラヒック制御と分散測定</div>
    <div class="authors">亀井聡、川原亮一 (NTT)</div>
  </li>
  <li>
    <div class="title">PlanetLab の計測結果を用いたオーバーレイルーティングの性能評価</div>
    <div class="authors">長谷川剛 (大阪大学)</div>
  </li>
  <li>
    <div class="title">P2P エージェントプラットフォーム PIAX とその応用</div>
    <div class="authors">寺西裕一 (大阪大学)</div>
    <div class="abstract">P2P オーバーレイ技術とエージェント技術を融合し、様々な情報を自律分散的に処理することで、さまざまなユビキタスコンピューティング応用を可能とするプラットフォーム PIAX について紹介する。</div>
  </li>
  <li>全体質疑</li>
</ol>
</div>

### 16:30 〜 16:45 ベンチャービジネスラボラトリー 3F ベンチャーホール

#### クロージング

<div markdown="0">
<h2 id="pcla" class="pcla">問い合せ先</h2>
</div>

### PC

- 大崎博之 (大阪大学)

### LA

- 秋山豊和 (京都産業大学)
- 梶田将司 (名古屋大学)

その他、本研究会に関しての問い合せは、[質問フォーム](#pcla)で受け付けています。
