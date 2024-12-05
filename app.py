from flask import Flask,render_template


flask_app=Flask(__name__)



@flask_app.route('/')
def home():
    return render_template('home.html')



@flask_app.route('/advice')
def advice():
    return render_template('advice.html')

@flask_app.route('/support')
def support():
    return render_template('/support.html')

@flask_app.route('/signup')
def signup():
    return render_template('/signup.html')


@flask_app.route('/login')
def login():
    return render_template('/login.html')


if __name__ =='__main__':
    flask_app.run(
        host='127.0.0.1',
        port=8005,
        debug=True
    )


