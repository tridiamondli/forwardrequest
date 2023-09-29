# -*- coding: UTF-8 -*-

from flask import Flask, request
import cloudscraper

app = Flask(__name__)

# 默认路由/，支持GET方法
@app.route('/', methods=['GET'])
def index():
    return 'Hello World!'

@app.route('/proxy', methods=['GET'])
def proxy():

    url = request.args.get('url')
    UserAgent_str = request.args.get('User-Agent')
    Referer_str = request.args.get('Referer')
    Cookie_str = request.args.get('Cookie')

    scraper = cloudscraper.create_scraper()

    if UserAgent_str is not None:
        scraper.headers.update({'User-Agent': UserAgent_str})
    if Referer_str is not None:
        scraper.headers.update({'Referer': Referer_str})
    if Cookie_str is not None:
        scraper.cookies.update({'Cookie': Cookie_str})

    try:
        response = scraper.get(url)
        return response.text
    except :
        return "error"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)