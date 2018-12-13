from flask import Flask, request, render_template
from flask_mail import Mail, Message
import read
app = Flask(__name__)

app.config.update(DEBUG=True,
                  MAIL_SERVER='smtp.gmail.com',
                  MAIL_PORT=465,
                  MAIL_USE_SSL=True,
                  MAIL_USERNAME = 'XXXXXX@gmail.com',
                  MAIL_PASSWORD = 'XXXXXX')

recepient_gather= read.receipient_updater()
@app.route('/send-mail', methods=['GET', 'POST'])
def send_mail():
	if request.method == 'POST':
		mail = Mail(app)
		message = "Success"
		subject = "Test Mail"
		msg = Message(subject,
		sender="<"+"picamerax"+">",
		recipients=recepient_gather)
		msg.body = message
		mail.send(msg)
	return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8123)
