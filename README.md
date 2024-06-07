# about pokanpo

pokanpoはガントチャート形式でポイ活情報を確認するツールです。

生成したガントチャートをgithub pagesで公開しています

[https://usop4.github.io/pokanpo/](https://usop4.github.io/pokanpo/)

![ganttchart](https://usop4.github.io/pokanpo/ganttchart.png)

# 技術的なこと

markdown形式で書いたキャンペーン情報がgithubにpushされたことをトリガーに、github actionsでガントチャートを生成し、github pagesにデプロイしています。

ガントチャート作成には[elegantt](https://github.com/usop4/elegantt)を使っています。
