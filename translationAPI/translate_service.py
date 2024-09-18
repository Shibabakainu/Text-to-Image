# coding: utf-8
"""

Abstract::
    -
History::
    - Ver.      Date            Author        History
    -
"""
# 標準ライブラリ


# 関連外部ライブラリ
from googletrans import Translator

# 内部ライブラリ


class TranslateService:
    """
    boto3のAWS Cognitoをラップしたクラス
    """

    def __init__(self):
        """
        クラスのコンストラクタ
        """
        self.__translator = Translator()
        self.__src = 'ja'
        self.__dest = 'en'

    def translate(self, text):
        """Translate text
        """
        try:
            translated_text = self.__translator.translate(text, src=self.__src, dest=self.__dest).text
            return {"result": translated_text}
        except Exception as e:
            raise e
