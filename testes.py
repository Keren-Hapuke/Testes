from selenium import webdriver

navegador = webdriver.Chrome()

#Abrir a página
navegador.get("http://127.0.0.1:8000/")
#Clicar em "criar conta
navegador.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/a').click()
#Preencher os dados
navegador.find_element_by_name('nome').send_keys("maria")
navegador.find_element_by_name('email').send_keys("maria@gmail.com")
navegador.find_element_by_name('senha1').send_keys("maria123")
navegador.find_element_by_name('senha2').send_keys("maria123")
#Clicar em cadastrar
navegador.find_element_by_id('cadastrar-usuario').click()
#Fazer login
navegador.find_element_by_name('email').send_keys("maria@gmail.com")
navegador.find_element_by_name('senha').send_keys("maria123")
#Clicar em logar
navegador.find_element_by_id('logar').click()
#Fazer logout
navegador.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[3]').click()










