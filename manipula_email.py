import imaplib, email, os


#Pasta onde será salvo o anexo

# loga no e-mail
def loga(usuario,senha,imap_url):
    con = imaplib.IMAP4_SSL(imap_url)
    con.login(usuario,senha)
    return con
# extrai o corpo do e-mail
def corpo_email(msg):
     if msg.is_multipart():
         return corpo_email(msg.get_payload(0))
     else:
         return msg.get_payload(None,True)
# baixa os anexos
def baixa_anexos(caminho_pasta,msg):
    for part in msg.walk():
        if part.get_content_maintype()=='multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        Nome_anexo = part.get_filename()
        if bool(Nome_anexo): #testa se tem anexo
            anexo_caminho = os.path.join(caminho_pasta, Nome_anexo)
            with open(anexo_caminho,'wb') as f:
                f.write(part.get_payload(decode=True))
        return Nome_anexo
# Busca por e-mail de acordo com o critério chave
def busca(chave,valor,con):
    result, data  = con.search(None,chave,'"{}"'.format(valor))
    return data
#converte o formato do e-mail
def get_emails(result_bytes,con):
    msgs = []
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)
        return msgs
