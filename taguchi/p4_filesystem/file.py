# coding: utf-8
import os, glob

print(os.path.join('/Users/pilgrim/diveintopython3/examples', 'humansize.py')) 
# os.path.join()がファイル名の前にスラッシュを追加してくれる

pathname = '/Users/pilgrim/diveintopython3/examples/humansize.py'
(dirname, filename) = os.path.split(pathname)
print(dirname) # /Users/pilgrim/diveintopython3/examples
print(filename) # humansize.py 

# -----------------------
# リスト内包表記
# -----------------------

# フィルター
# [f for f in glob.glob('*.py') if os.stat(f).st_size > 6000]

# -----------------------
# 辞書内包表記
# -----------------------

metadata_dict = {f:os.stat(f) for f in glob.glob('data/*test*.py')}
print list(metadata_dict.keys()) # ['data/test3.py', 'data/test1.py', 'data/test2.py']    
print  metadata_dict['data/test1.py'].st_size

# 途中で改行入れる時は\を追加
# humansize_dict = {os.path.splitext(f)[0]:humansize.approximate_size(meta.st_size) \     
# for f, meta in metadata_dict.items() if meta.st_size > 6000}1

# 辞書のkeyとvalueを入れ替える
a_dict = {'a': 1, 'b': 2, 'c': 3}
print {value:key for key, value in a_dict.items()} # {1: 'a', 2: 'b', 3: 'c'}


