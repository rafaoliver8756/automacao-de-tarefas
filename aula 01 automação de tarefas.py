import pyautogui
import time
import os
import pandas

pyautogui.PAUSE = 0.5

os.system('start chrome --profile-directory="Default"')
time.sleep(3) #tempo para que o navegar abre a tela totalmente
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" #link usado para a aula, pode ser substutuido por qualquer outro link.

pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3) #tempo para que a página carregue e em seguida dar continuidade aos comandos

pyautogui.click(x=905, y=411)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("12345*8978-") #senha qualquer, pois a página é apenas para fins de demostração.
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3) #tempo para que a página carregue e em seguida dar continuidade aos comandos

#uso do pandas e openpyxl para ler os dados de um arquivo excel e usar esses dados para preencher um formulário na página web
#import pandas, openpyxl

#o próximo passo precisamos que o python tenha acesso ao arquivo excel
tabela = pandas.read_csv(r"C:\Users\rafae\OneDrive\projetos\PYTHON\automação de tarefas - curso da hashtag Lira\produtos.csv") #raw string (string “crua”) para evitar problemas com as barras invertidas no caminho do arquivo
print(tabela)

#limpando coluna obs que esta com ;;;
tabela = tabela.replace(";;;", "") # serve para substituir os ";;;" por um espaço vazio
for linha in tabela.index: 
#index: cada linha da tabela existe um número de índice, para o programa entender que é uma linha invés de uma coluna, aplicamos o comando index. linha = index coluna = columns
#No código acima eu quero dizer: Para cada linha da minha tabela eu vou executar esse código todo


        '''
        Cadastrar os produtos na página web | Cada linha abaixo e aplicado a regra de identação que diz que tudo com o espaço 
        será considerado parte do for, ou seja, será aplicado um laço de repetição.
        '''
        
        pyautogui.click(x=789, y=297)
        #código
        codigo = tabela.loc[linha, "codigo"] #aqui diz que na tabela irei localizar a linha (index que é a variável do for) e a coluna "codigo" para pegar o código do produto.
    
        pyautogui.write(codigo)
        pyautogui.press("tab")

        #marca

        marca = tabela.loc[linha, "marca"]

        pyautogui.write(marca)
        pyautogui.press("tab")

        #tipo 

        tipo = tabela.loc[linha,"tipo"]

        pyautogui.write(tipo)
        pyautogui.press("tab")

        #categoria

        categoria = str(tabela.loc[linha, "categoria"])

        pyautogui.write(categoria)
        pyautogui.press("tab")

        #preço

        preco = str(tabela.loc[linha, "preco_unitario"])

        pyautogui.write(preco)
        pyautogui.press("tab")
        
        #custo

        custo = str(tabela.loc[linha, "custo"])
        
        pyautogui.write(custo)
        pyautogui.press("tab") 

        #obs

        obs = str(tabela.loc[linha, "obs"]) #str para converter no valor de texto

        if obs != "nan": #se a observação for diferente de "nam" (espaço vazio) escreva a pbservação, caso contrário pule para o próximo campo
            pyautogui.write(obs)
        pyautogui.press("tab")

        pyautogui.press("enter") #passar para o botão salvar e clicar

#voltar para o ínicio da tela para cadastrar o próximo produto
pyautogui.scroll(5000) #rolar a tela para cima
 
