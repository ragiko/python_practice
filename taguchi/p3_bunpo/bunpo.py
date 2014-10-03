# coding: utf-8
"""
http://diveintopython3-ja.rdy.jp/native-datatypes.htmlのコピペ
文法とか
"""

## リスト
# append(), extend(), insert(), remove(), pop()を持つ
# extend...リストとリストを合体させる
# append...リストとオブジェクト要素を合体させる
a_list = ['a', 'b', 'mpilgrim', 'z', 'example']
print a_list[-1] # example

## スライス
print a_list[3:] # ['z', 'example'] 要は3~5要素
print a_list[:] # ['a', 'b', 'mpilgrim', 'z', 'example']

## リストから要素を取り除く: 
print a_list.pop(3) # z : 3つ目が消えるらしい
print a_list # ['a', 'b', 'mpilgrim', 'example']

## タプル
# タプルはイミュータブルなリストだ。いったん作成されたタプルは、どんな手段によっても変更できない。 
a_tuple = ("a", "b", "mpilgrim", "z", "example") # 宣言
print a_tuple.index("example") # 4
print "z" in a_tuple # True : 要素があるか調べられる

# ある種のタプル（具体的に言えば、文字列とか数字とか他のタプルとかいったようなイミュータブルな値からなるタプル）は辞書のキーとして使える。リストはイミュータブルではないので、辞書のキーとしては決して使うことができない。

if ('a', 'b'):
    print(True) 
else: 
    print(False)
# => true
# 要素を1つでももつタプルは真だ。 
print type((False,))
# 1つの要素からなるタプルを作るには、値の後にカンマを置かなくてはならない。もしこのカンマがないと、Pythonは余分な括弧があるだけだと見なしてしまう。これはエラーにはならないが、タプルは作成されない。

(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7) 
print MONDAY # 0

## 集合
a_set = {1, 2}
a_set.add(1)
print a_set # set([1, 2]) : 集合は一意な値を詰めた袋だ。既にその集合に含まれている値を追加しようとしても、何も起こらない。例外も送出されない。本当に何も起こらないのだ。 

a_set = {2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195}
b_set = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}
print a_set.union(b_set)    
print a_set.intersection(b_set)
# union()メソッドは、どちらかの集合に含まれるすべての要素を含んだ新しい集合を返す。
# intersection()メソッドは、両方の集合に含まれるすべての要素を含んだ新しい集合を返す。
# difference()メソッドは、a_setには含まれるがb_setには含まれていないすべての要素を含んだ新しい集合を返す。
# symmetric_difference()メソッドは、どちらか一方だけの集合に含まれるすべての要素を含んだ新しい集合を返す。 

## NONE
# Noneは唯一のnull値
print None == 0 # FALSE
print None == "" # FALSE

