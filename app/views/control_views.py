
from flask import Blueprint, request, render_template, flash, url_for, session, g, redirect
from app.models import User
from app import db
import functools
from ..forms import UserLoginForm

test = Blueprint('test', __name__, url_prefix='/')

@test.route('/')
def hello():
    return render_template("index.html")

@test.route('/about')
def about():
    return "about World!"

@test.route('/cart')
def cart():
    return render_template("cart.html")

#데이터를 등록하기 위한 함수를 만들어야 한다.
# @test.route('/login')
# def login():
#     email_address = request.args.get('email_address')
#     passwd = request.args.get('passwd')
#     print(email_address, passwd)

#     # if email_address == 'dave@gmail.com' and passwd == '111':

#     #     return_data = {'auth': 'success'}
#     # else:
#     #     return_data = {'auth': 'failed'}
#     # return jsonify(return_data)
#     return render_template("login_rawtest.html")

@test.route('/login', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
		# 폼 입력으로 받은 username으로 데이터베이스에 해당 사용자가 있는지를 검사한다. 만약 사용자가 없으면 "존재하지 않는 사용자입니다."라는 오류를 발생시키고, 사용자가 있다면 폼 입력으로 받은 password와 check_password_hash 함수를 사용하여 데이터베이스의 비밀번호와 일치하는지를 비교합니다.
        user = User.query.filter_by(user_id=form.user_id.data).first()
        # 로그인 자체가 막혀버림 
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif (user.password != form.password.data):
            error = "비밀번호가 올바르지 않습니다."
            
        # 아무 문제가 없으면 
        if error is None:
            # 사용자도 존재하고 비밀번호도 일치한다면 플라스크 서버의 나를 위한 저장소인 세션(session)에 사용자 정보를 저장합니다.

						# 세션에 user_id라는 객체 생성
            session.clear()
            session['user_id'] = user.user_id
            _next = request.args.get('next', '')
            if _next:
                return redirect(_next)
            else:
                return redirect(url_for('test.hello'))
                
        # 에러메시지를 flash 한테 넘깁니다
        # 문제가 있으면 그 문제를 form_errors.html로 보내버리는 역할 
        print(session['user_id'])
        flash(error)
    return render_template("login_rawtest.html", form=form)


@test.route('/html_test')
def hello_html():
    # html file은 templates 폴더에 위치해야 함
    return render_template('login_rawtest.html')
