from flask import Flask
from flask import render_template
from flask import request
from flask import session

app = Flask(__name__)
app.secret_key = '123'

# creating users' dictionary
users = {'user1': {'name': 'Or', 'email': 'or@gmail.com'},
         'user2': {'name': 'Hila', 'email': 'hila@gmail.com'},
         'user3': {'name': 'Daniel', 'email': 'daniel@gmail.com'},
         'user4': {'name': 'Ofir', 'email': 'ofir@gmail.com'},
         'user5': {'name': 'Gil', 'email': 'gil@gmail.com'},
         'user6': {'name': 'Anat', 'email': 'anat@gmail.com'}
         }


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment_9():
    if 'mail' in request.args:
        email = request.args['mail']
        if email == '':
            return render_template('assignment9.html', users_list=users)
        else:
            for key, value in users.items():
                if value.get('email') == email:
                    return render_template('assignment9.html', p_name=value.get('name'), p_mail=value.get('email'))
        return render_template('assignment9.html', users_list=users)
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        session['username'] = username
        return render_template('assignment9.html', p_username=username, p_password=password)
    return render_template('assignment9.html')


@app.route("/logout", methods=['GET', 'POST'])
def logout_func():
    session['username'] = ''
    return render_template('assignment9.html')


@app.route('/home')
@app.route('/')
def home_func():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)

