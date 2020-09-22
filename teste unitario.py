import pandas as pd
import agregaRPA 

# Caso 1: planilha de fornecedor sem existir planilha unificada
# Cria entrada da função para o caso 1 de teste
colunas = ['Produto','Quantidade','Valor']
dados_fornecedor1 = pd.DataFrame(columns = colunas)
dados_fornecedor1.loc[0] = ["arroz",10,20]
dados_fornecedor1.to_csv('fornecedor1.csv', index = False)
#chama a função

agregaRPA.agrega('fornecedor1.csv','fornecedor1')

#verifica a saída para o caso 1
dados_planilha_unificada =  pd.read_csv('Planilha Unificada.csv')
colunas = dados_planilha_unificada.columns.tolist()
resposta = pd.DataFrame(columns = colunas)
resposta.loc[0] = ['fornecedor1',"arrroz",10,20]
print(resposta)

print(dados_planilha_unificada)
if all(dados_planilha_unificada.loc[dados_planilha_unificada.Fornecedor == 'fornecedor1'].eq(dados_fornecedor1)):
    print("Caso 1 testado com sucesso")
else:
    print("Caso 1 falhou")
    
#______________________________________________________________________________________________________________    
# Caso 2: planilha de fornecedor com fornecedor e produtos novos
colunas = ['Produto','Quantidade','Valor']
dados_fornecedor2 = pd.DataFrame(columns = colunas)
dados_fornecedor2.loc[0] = ["feijao",30,15]
dados_fornecedor2.to_csv('fornecedor2.csv', index = False)
#chama a função

agregaRPA.agrega('fornecedor2.csv','fornecedor2')

#verifica a saída para o caso 2
dados_fornecedor1['Fornecedor']='fornecedor1'
dados_fornecedor2['Fornecedor']='fornecedor2'
dados_planilha_unificada =  pd.read_csv('Planilha Unificada.csv')
if all(dados_planilha_unificada.loc[dados_planilha_unificada.Fornecedor == 'fornecedor1'].eq(dados_fornecedor1)):
    if  all(dados_planilha_unificada.loc[dados_planilha_unificada.Fornecedor == 'fornecedor2'].eq(dados_fornecedor2)):

        print("Caso 2 testado com sucesso")
else:
    print("Caso 2 falhou")
    
#______________________________________________________________________________________________________________    
# Caso 3 :planilha de fornecedor já cadastrado com produtos novos
colunas = ['Produto','Quantidade','Valor']
dados_fornecedor1 = pd.DataFrame(columns = colunas)
dados_fornecedor1.loc[0] = ["arroz",10,20]
dados_fornecedor1.loc[1] = ["batata",30,10]

dados_fornecedor1.to_csv('fornecedor1.csv', index = False)
#chama a função

agregaRPA.agrega('fornecedor1.csv','fornecedor1')

#verifica a saída para o caso 3
dados_planilha_unificada =  pd.read_csv('Planilha Unificada.csv')
dados_fornecedor1['Fornecedor']='fornecedor1'
dados_fornecedor2['Fornecedor']='fornecedor2'
if all(dados_planilha_unificada.loc[dados_planilha_unificada.Fornecedor == 'fornecedor1'].eq(dados_fornecedor1)) :
    if all(dados_planilha_unificada.loc[dados_planilha_unificada.Fornecedor == 'fornecedor2'].eq(dados_fornecedor2)):
        print("Caso 3 testado com sucesso")
else:
    print("Caso 3 falhou")
#______________________________________________________________________________________________________________
# Caso 4: planilha de fornecedor já cadsatrado com quantidades e valores novos de produtos existentes

colunas = ['Produto','Quantidade','Valor']
dados_fornecedor1 = pd.DataFrame(columns = colunas)
dados_fornecedor1.loc[0] = ["arroz",30,15]
dados_fornecedor1.loc[1] = ["batata",50,5]

dados_fornecedor1.to_csv('fornecedor1.csv', index = False)
#chama a função

agregaRPA.agrega('fornecedor1.csv','fornecedor1')

#verifica a saída para o caso 4
dados_planilha_unificada =  pd.read_csv('Planilha Unificada.csv')
dados_fornecedor1['Fornecedor']='fornecedor1'
dados_fornecedor2['Fornecedor']='fornecedor2'
if all(dados_planilha_unificada.loc[dados_planilha_unificada.Fornecedor == 'fornecedor1'].eq(dados_fornecedor1)) :
    if all(dados_planilha_unificada.loc[dados_planilha_unificada.Fornecedor == 'fornecedor2'].eq(dados_fornecedor2)):
        print("Caso 4 testado com sucesso")
else:
    print("Caso 4 falhou")
    
    
    
