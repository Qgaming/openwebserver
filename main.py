from flask import Flask, render_template

app = Flask(__name__, template_folder='www')

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except:
        return render_template('404.html')
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)