# 正體中文字之部首、筆劃、注音

從「重編國語辭典修訂本」中取出各個中文字的部首、筆劃、注音等特徵，以供對自然語言處理。

原始資料來源：[辭典公眾授權網](https://resources.publicense.moe.edu.tw/index.html)，版權屬原作者。

## 建出字元資訊

請自行從
[辭典公眾授權網](https://resources.publicense.moe.edu.tw/index.html)下載資料，並將解開之excel檔放在repository中（即xls_to_json.py所在目錄）。然後執行以下指令：

```sh
python xls_to_json.py
```

即可生成char_dicts.json (註：excel的預設檔名為dict_revised_2015_20180409_1.xls等，若您下載之檔名不是這樣，您需要修改xmls_to_json.py）

char_dicts.json 的內容如下：
```json
[
...
  {
    "字詞名": "爸",
    "注音一式": "ㄅㄚˋ",
    "漢語拼音": "bà",
    "總筆劃數": 8,
    "部首外筆劃數": 4,
    "部首字": "父"
  },
...
]
```

目前repository裡提供的char_dicts.json內含12521個字元，部分字元的注音欄位會含有注音以外的資訊，如「(一)ㄅㄚ」，「(二)（又音）ㄅㄚˋ」等等，若只想要注音資料的話須另外處理。
