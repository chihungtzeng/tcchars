# -*- coding: utf-8 -*-
"""
Convert *.xls from 重編國語辭典修訂本 and store char attributes in json.
"""
import os
import io
# import pprint
import logging
import json
import pandas
__EXCLUDE_FIELDS = u"字詞屬性 字詞號 相似詞 相似詞1 相似詞2 相似詞3 相似詞4 相反詞 釋義 編按 多音參見訊息 異體字".split()


def __read_xls(excel_file_name):
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    excel_path = os.path.join(cur_dir, excel_file_name)
    contents = pandas.read_excel(excel_path)
    _dicts = contents.to_dict("records")
    ret = [_ for _ in _dicts if _["字詞屬性"] == 1 and len(_["字詞名"]) == 1]
    logging.info(u"%s: Total records: %d, char records: %d",
                 excel_file_name, len(_dicts), len(ret))
    return ret


def __read_all_xls():
    filenames = ["dict_revised_2015_20180409_1.xls",
                 "dict_revised_2015_20180409_2.xls",
                 "dict_revised_2015_20180409_3.xls"]
    char_dicts = []
    for fname in filenames:
        char_dicts += __read_xls(fname)

    # remove unneeded fields:
    for _dict in char_dicts:
        for key in __EXCLUDE_FIELDS:
            _dict.pop(key, None)
    # remove \n
    for _dict in char_dicts:
        for key in _dict:
            if isinstance(_dict[key], str):
                _dict[key] = _dict[key].strip()
    return char_dicts


def main():
    """Prog entry"""
    char_dicts = __read_all_xls()
    output_file = "char_dicts.json"
    logging.warning("Write %d records to %s", len(char_dicts), output_file)
    with io.open(output_file, "w", encoding="utf-8") as _fp:
        jdata = json.dumps(char_dicts, sort_keys=True, ensure_ascii=False)
        _fp.write(jdata)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
