import mechanize
import cookielib
import BeautifulSoup
import logging
# Browser
br = mechanize.Browser()

logging.getLogger('mechanize').setLevel(logging.DEBUG)
# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'
accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
accept_encoding = 'gzip, deflate'
accept_language = 'en-US,en;q=0.8,ru;q=0.6,hi;q=0.4'
cache_control = 'max-age=0'
connection = 'keep-alive'
content_type = 'application/x-www-form-urlencoded'
host = 'bigbasket.com'
origin = 'https://bigbasket.com'
referer = 'https://bigbasket.com/auth/login/'

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Want debugging messages?
br.set_debug_http(True)
br.set_debug_redirects(True)
br.set_debug_responses(True)

# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent', ua), ('Accept', accept), ('Accept-Encoding', accept_encoding), ('Accept-Language', accept_language), ('Cache-Control', cache_control), ('Connection', connection), ('Content-Type', content_type), ('Host', host), ('Origin', origin), ('Referer', referer)]

br.open('http://bigbasket.com/auth/login')
br.select_form(nr=4)
br.form['username'] = 'kumariankita002@gmail.com'
br.form['password'] = 'ankita002'
br.submit()

#br.add_password('https://bigbasket.com/auth/login/', 'kumariankita002@gmail.com', 'ankita002')
#br.open('https://bigbasket.com/auth/login')

#br.select_form(nr=1)
#br.form['q'] = 'apples'
#br.submit()

page = br.response().read()
ref_page = BeautifulSoup.RobustHTMLParser(page)
print ref_page.prettify()


