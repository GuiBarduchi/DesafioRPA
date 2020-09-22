import pandas as pd

# caminho para os arquivos
def agrega(caminho_anexo,nome_fornecedor):
    planilha_unificada = "Planilha Unificada.csv"     
    dados_nova_planilha = pd.read_csv(caminho_anexo + '\\' + nome_fornecedor)

    try: 
        with open(planilha_unificada,'r') as f: # caso ja exista o arquivo da planilha unificada
            dados_planilha_unificada = pd.read_csv(planilha_unificada)
        
    except IOError as e: # caso não exista o arquivo da planilha unificada
        colunas = ['Fornecedor','Produto','Quantidade','Valor']
        dados_planilha_unificada = pd.DataFrame(columns = colunas)
 

    dados_sem_fornecedor_atual = dados_planilha_unificada.loc[dados_planilha_unificada.Fornecedor != nome_fornecedor[:-4]] # # carrega todos os dados da planilha unificada com exceção dos dados do fornecedor que será atualizado pelo novo arquivo do fornecedor
    dados_nova_planilha['Fornecedor'] = nome_fornecedor[:-4]      
    dados_planilha_unificada = dados_sem_fornecedor_atual.append(dados_nova_planilha) # acrescenta à planilha unificada os novos valores do novo arquivo do fonecedor

    dados_planilha_unificada.to_csv('Planilha Unificada.csv', index = False)        # salva a nova planilha unificada
        
