import twill, string, os
from twill.commands import *

b=twill.commands.get_browser()
b.set_agent_string("Mozilla/5.0 (Windows; U; Windows NT 5.1;en-GB;rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14")
b.clear_cookies()
b.go("https://bigbasket.com/auth/login/")
b.showforms()
f=b.get_form("6")
fv("6", "username", "kumariankita002@gmail.com")
fv("6", "password", "ankita002")
formaction('6', 'https://bigbasket.com/auth/login/')
submit()
f_main = b.get_form('5')
formaction('5', 'http://bigbasket.com/ps/')


