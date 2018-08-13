from flask import Flask, redirect, url_for, request,render_template
from search import SearchEngine
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        itemName = request.form['nm']
        se = SearchEngine()
        bigw = se.searchBigW(itemName)
        dj=se.searchDavidJones(itemName)
        return render_template('search.html',bigwItems = bigw,djItems=dj)
    else:
        return render_template('search.html',bigwItems = [], djItems = [])

@app.route('/search',methods = ['POST', 'GET'])
def search():
   if request.method == 'POST':
      itemName = request.form['search']
      return itemName




if __name__ == '__main__':
    app.run()



