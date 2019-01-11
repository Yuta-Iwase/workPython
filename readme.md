# 使用法紹介
## <a href="https://raw.githubusercontent.com/Yuta-Iwase/workPython/master/hist/HistgramPlot.py">HeatMap.py</a>
↑の「リンクを名前をつけて保存」

|変数名|解説|
|:-|:-|
|inputPath|読み込むファイル名(csvである必要がある)|
|outputName|出力する際のファイル名|
|plotRangeX|横軸はいくつからいくつのデータなのか与える。(空白で0,1,2,...となる)|
|plotRangeY|縦軸はいくつからいくつのデータなのか与える。(空白で0,1,2,...となる)|
|cmap|matplotlibライブラリで予め準備されているカラーマップ名([ここ](https://matplotlib.org/examples/color/colormaps_reference.html)を参照)を指定。<br>(空白でカラーマップ:hotとなる)|
- 読み込むファイルはカンマ区切りにする必要がある(タブ区切りではダメ)
- `inputPath` は末尾に必ず `.csv` まで書く必要がある。
- `outputName` は空白にして省略可能。その場合、 `inputPath` と同名になる。
- `plotRangeX` , `plotRangeY` は2から5を指定したいなら `plotRangeX = [2,5]`などと書く。
- `plotRangeX` , `plotRangeY` は `plotRangeX = []` などと省略することができ、その場合は値は0,1,2,...となる。
