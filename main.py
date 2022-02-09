from flask import Flask, render_template, Response

app = Flask(__name__, template_folder="html", static_folder="css-js")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('/error-handler.html'), 404


@app.route('/e')
@app.route('/err')
@app.route('/error')
@app.route('/error404')
def error():
    return render_template('/error-handler.html')


@app.route('/e2')
@app.route('/err2')
@app.route('/error2')
@app.route('/error403')
def error2():
    return render_template('/error-handler2.html')


# render_template
@app.route('/')
@app.route('/home')
def index():
    return render_template('/main-html/index.html')


@app.route('/yt')
@app.route('/youtube')
def youtube():
    response = Response()
    response.headers['Refresh'] = '0; url=/error403'
    return response


# others
@app.route('/discord')
def dc_rules():
    return render_template('dsc.gg/ziek-page')


# Response

@app.route('/rblxgroup')
def rblxgroup():
    response = Response()
    response.headers[
        'Refresh'] = '0; url=https://www.roblox.com/groups/4447582/The-Oberon-Dynasty'
    return response


# templates
@app.route('/footer')
def footer():
    return render_template('/templates/footer.html')


@app.route('/header')
def header():
    return render_template('/templates/header.html')


@app.route('/sidenav')
def sidenav():
    return render_template('/templates/sidenav.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)  # debug=True/False
