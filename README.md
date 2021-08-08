# FlattenNintendoPictures

## 目的

`Nintendo Switch` でSDカードにコピーした画像が `"Nintendo / Album / #{year} / #{month} / #{date}"` というディレクトリ構造になっているのだが
全部一覧で並んだ状態で見たい気持ちになったため作成した

## やること

ディレクトリ構造をすべて消し去り画像がすべて同じ階層にならぶ

## 準備

`Python 3` なら動くはず。

カレントディレクトリに `Output` というフォルダを作成しておく。コピー後はOutput配下に日付のフォルダができて、その配下に画像がコピーされる

コピーしたい `Nintendo` フォルダをカレントディレクトリにコピーしておく

（`"カレントディレクトリ / Nintendo / Album / #{year} / #{month} / #{date}"` という構造にする。もしかするとSDカードからそのままコピーすると `"カレントディレクトリ / Nintendo / Nintendo / Album / #{year} / #{month} / #{date}"` となるかもしれないのでコピーのフォルダを変えてください）