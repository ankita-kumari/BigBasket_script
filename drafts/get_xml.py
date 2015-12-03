import urlparse
import urllib2

def get_xml(uri,login):
    netlock = urlparse.urlparse(uri)
    pswdMngr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    pswdMngr.add_password(None,netlock[1],login.get("username"),login.get("password"))
    auth = urllib2.HTTPBasicAuthHandler(pswdMngr)
    req = urllib2.Request(uri)
    opener = urllib2.build_opener(auth)
    f = opener.open(req)
    print f
    xml = f.read()
    f.close()
    return xml

if __name__ == '__main__':
    print get_xml('https://bigbasket.com/auth/login/', {"username" : "kumariankita002@gmail.com", "password" : "ankita002"})