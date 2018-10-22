# -*- coding: utf-8 -*-

# シャープ(#)でコメント
# 1行目の「 -*- coding: utf-8 -*-」はこのコードはutf-8で書いてあることの宣言。pythonコードは慣例的に1行目にこれを入れる。

# ここからプログラム本文
# メッセージボックスのために必要なライブラリを連れてくる。
import tkMessageBox
# インポートしたライブラリはjavaのオブジェクト感覚でメソッドを呼び出せる。
tkMessageBox.showinfo('showinfo','Hello python!')