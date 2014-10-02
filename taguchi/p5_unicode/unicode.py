# coding: utf-8

import sys

# -------------------
# UNICODE
# -------------------

# UNICODEは32bit(4byte)を全ての文字に対して負荷するため助長
# 
# UTF-8は、Unicodeのための可変長のエンコード体系
# UTF-8の8は8bit
# UTF-8は文字列をバイト列としてエンコードする方法の1つ
#
# 欠点: それぞれの文字が異なるバイト数を使うので、N番目の文字見つけ出す処理はO(N)の演算になる。
# 利点: 一般のASCII文字を扱う場合には非常に効率的な文字コードだ。


# import humansize
# import sys
# '1MB = 1000{0.modules[humansize].SUFFIXES[1000][0]}'.format(sys)
# '1MB = 1000KB'
# 
# {0.modules[humansize].SUFFIXES[1000][0]}'.format(sys)
# sys.modulesでimportしてきたhumansize.SUFFIXES[1000][0]を参照
# 文字列内のhumansizeはクォーテーションを含まない
#
# '{0:.1f} {1}'.format(698.24, 'GB')
# :.1fはフォーマットの形式, 小数点以下

# -------------------
# 一般的な文字列メソッド
# -------------------

s = '''Finished files are the re-  ①
sult of years of scientif-
ic study combined with the
experience of years.'''
print s.count('f') # 5


# key1=value1&key2=value2をdictに変換
query = 'user=pilgrim&database=master&password=PapayaWhip'
a_list = query.split('&')
a_list_of_lists = [v.split('=', 1) for v in a_list if '=' in v]
# v.split('=', 1)の1は１回だけsplit。2こ以上'='が入っている可能性もあるため
a_dict = dict(a_list_of_lists)
print a_dict

# byte(UTF-8) と 文字列(UNICODE)
# 参考: http://lab.hde.co.jp/2008/08/pythonunicodeencodeerror.html
s = u"我が輩は猫である"
# print s
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-7: ordinal not in range(128)
# defaultのdecodeはasciiのため,print s => print s.encode('ascii')でエラーする
#
print s.encode("utf-8") # 我が輩は猫である
print sys.getdefaultencoding() # ascii

reload(sys) # しないと行けないらしい, 参考: http://blog.livedoor.jp/kaz0215/archives/51124286.html
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding() # utf-8
print s # NOT ERROR


