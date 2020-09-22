import manipula_email
import agregaRPA
import email

usuario = input("digite o endereço do e-mail: ")
senha = input("digite a senha:")
pasta = input("digite o endereço da pasta de destino dos anexos:") # as barras devem ser duplas por exemplo C:\\Users\\Avell\\Desktop\\rpa

imap_url = 'imap.gmail.com'

con = manipula_email.loga(usuario,senha,imap_url) # loga no e-mail com as credenciais fornecidas
con.select('INBOX')

data = manipula_email.busca('SUBJECT','Planilha Fornecimento',con) # busca o identificador de todos os e-mails com assunto Planilha Fornecimento
num = data[0].split()
for i in range(0,len(num)): # para cada e-mail com assunto Planilha Fornecimento é repetido o processo de download dos anexos e agregação com a planilha unificada
    result, data = con.fetch(num[i],'(RFC822)')
    raw = email.message_from_bytes(data[0][1])
    fornecedor = manipula_email.baixa_anexos(pasta,raw) # baixa o anexo do e-mail atual e retorna o nome do fornecido ( que deve ser igual ao nome da planilha)
    agregaRPA.agrega(pasta,fornecedor) # chama o método que agrega o a planilha do fornecedor atual com a planilha unificada
print("Processo finalizado")

