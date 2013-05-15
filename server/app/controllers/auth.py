# -*- coding: utf-8 -*-
from controllers import base_handler
from utils import util
from utils.logger import logger
from utils import database
from models.user import User
from sqlalchemy import and_
import time

class LoginHandler(base_handler.BaseHandler):

    LOGINCHECKERROR = '5001'

    def get(self):

        self.render('login.html')

    def post(self):

        inputParams = {
            'username': self.get_argument('username'),
            'password': self.get_argument('password')
        }

        self._checkLogin(inputParams)

    def _checkLogin(self, inputParams):
        db_session = database.getSession()
        user_query = db_session.query(User)

        r = user_query.filter(and_(User.username == inputParams.get('username'),
                                   User.password == inputParams.get('password'))).first()

        if r is None:
            self._sendError(self.LOGINCHECKERROR, '用户名或密码错误')
        else:
            self._loginUser(r)

    def _loginUser(self, user):
        sid = self.session.sessionid
        self.set_secure_cookie('sid', sid)

        self.session['username'] = user.username

        self.redirect('/', permanent=False)

    def _sendError(self, errorCode, errorMsg):
        loginUrl = '/login?ecode=' + errorCode + '&emsg=' + errorMsg

        self.redirect(loginUrl, permanent=False)


class RegHandler(base_handler.BaseHandler):

    USERNAME_ERRORCODE = '5001'
    PASSWORD_ERRORCODE = '5002'

    def get(self):

        self.render('reg.html')

    def post(self):
        inputParams = {
            'username': self.get_argument('username'),
            'password': self.get_argument('password')
        }

        if self._validateInput(inputParams):
            self._addUser(inputParams)

    def _addUser(self, userData):
        userData['email'] = userData.get('username')
        userData['role'] = 3
        userData['activated'] = 0
        userData['create_time'] = round(time.time())

        u = User(**userData)
        u.saveNew()


    def _validateInput(self, inputParams):

        if not util.isEmail(inputParams.get('username')):
            logger.debug('Invalid email address:' + inputParams.get('username'))
            self._sendError(self.USERNAME_ERRORCODE, 'Invalid email address')
            return False

        if not util.isPassword(inputParams.get('password')):
            logger.debug('Invalid password:' + inputParams.get('password'))
            self._sendError(self.PASSWORD_ERRORCODE, 'Invalid password')
            return False

        return True

    def _sendError(self, errorCode, errorMsg):
        regUrl = '/reg?ecode=' + errorCode + '&emsg=' + errorMsg

        self.redirect(regUrl, permanent=False)



