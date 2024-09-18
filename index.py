# coding: utf-8
"""

Abstract::
    -
History::
    - Ver.      Date            Author        History
    -
"""
# 標準ライブラリ
import base64
import os
import time
# 関連外部ライブラリ
from flask import jsonify, request, send_file
from http import HTTPStatus

# 内部ライブラリ
from app.app import create_app
from translationAPI.translate_service import TranslateService
from StableDiffusion.sd_service import SDService
translate_service = TranslateService()
sd_service = SDService()

app = create_app("", "", "", "", "")

@app.route('/generate', methods=['GET','OPTIONS'])
def generate():
    """
    """
    if request.method == 'OPTIONS':
        return jsonify({"result": ""}), HTTPStatus.OK
    text = request.args.get('text')
    status = HTTPStatus.OK
    translated_text = translate_service.translate(text)['result']

    print("---------------")
    print("prompt:" + translated_text)
    print("--------------------")

    img = sd_service.create_img(translated_text)
    img.save(f"img.png")
    
    img_path = os.path.abspath("img.png")

    return send_file(img_path, mimetype='image/png'), status


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
