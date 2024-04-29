# about pokanpo

pokanpoはガントチャート形式でポイ活情報を確認するツールです。

生成したガントチャートをgithub pagesで公開しています

[https://usop4.github.io/pokanpo/](https://usop4.github.io/pokanpo/)

# 技術的なこと

markdown形式で書いたキャンペーン情報がgithubにpushされたことをトリガーに、github actionsでガントチャートを生成し、github pagesにデプロイします。

ガントチャート作成にはeleganttというライブラリを使っています。

![ganttchart](https://usop4.github.io/pokanpo/ganttchart.png)

