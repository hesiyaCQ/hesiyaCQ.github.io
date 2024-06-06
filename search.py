from flask import Flask, render_template, request

app = Flask(__name__)


articles = [
    {"title": "大学的真相", "date": "2024-05-01 11:55", "link": "https://www.zhihu.com/question/622975242/answer/3321302845?utm_psn=1781440775583711232"},
    {"title": "比赛推荐", "date": "2024-05-02 10:13", "link": "https://www.zhihu.com/question/653417794/answer/3472144895?utm_psn=1781440920190713857"},
    {"title": "如何参加比赛", "date": "2024-05-03 08:03", "link": "https://www.zhihu.com/question/651135579/answer/3451662787?utm_psn=1781440969344708609"},
    {"title": "全国大学生数学建模大赛", "date": "2024-05-04 11:07", "link": "https://zhuanlan.zhihu.com/p/685234513?utm_psn=1781441078844465152"},
    {"title": "前端开发学习路线", "date": "2024-05-05 10:44", "link": "https://www.zhihu.com/question/30180100/answer/3203323314?utm_psn=1781447912510865408"}
]

@app.route('/')
def index():
    return render_template('index.html', articles=articles)

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    # 根据搜索词过滤出匹配的项目
    matched_articles = [article for article in articles if query in article['title']]
    return render_template('search_results.html', articles=matched_articles)

if __name__ == '__main__':
    app.run(debug=True)
