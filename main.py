from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    try:
        with open("test.txt","w") as fo:
             fo.write(text)
    except:
          return ('There is no such file found', 400)
    return ('', 204)		
if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)