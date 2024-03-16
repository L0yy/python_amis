from flask import Flask, render_template,send_file

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        "pageTitle":     "首页哈",
		"pageSchemaApi": "GET:/index",
    }
    return render_template('index.tmpl', **data)


@app.route('/index')
def indexhandle():
    return send_file('templates\\index.site')

if __name__ == '__main__':
    app.run()