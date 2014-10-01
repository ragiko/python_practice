# coding: UTF-8
"""
nltk の ntlk/classify/scikitlearn.pyからコード規約やクラスの書き方を学ぶ
"""

def t_tamura(massage):
    print "原君ー" + massage

class BaseHara():
    """原さんのベースクラス"""

    def __init__(self, message):
        """
        初期化される部分
        ・関数も引数に入れられるっぽい
        ・インスタンスメソッドは_を付けている
        """
        self._message = message
        self._t_tamura = t_tamura

    def say_message(self):
        """ 
        selfは自己の変数を参照するために用いる
        """
        print self._message 
    
    def say_t_tamura(self):
        self._t_tamura("一緒に大吉行こうよ")

class Hara(BaseHara):
    """
    ()により継承する
    """
    def a():
        print a


if __name__ == "__main__":
    h = Hara("test")
    h.say_message()
    h.say_t_tamura()


