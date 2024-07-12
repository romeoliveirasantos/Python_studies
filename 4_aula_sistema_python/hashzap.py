#<-passo a passo->
#titulo
#botão iniciar chat
    #popUp/modal/alerta
    #titulo: bem vindo ao chat
    #Campo de texto: escreva seu nome no chat
    #botão: entrar no chat
        #sumir com o titulo e botão inicial
        #fechar o popup
        #criar chat(com a mensagem de nome do usuário e a frase entrou no chat)
        #em baixo do chat:
            #campo de texto: digite sua mensagem
            #botão enviar
                #vai aparecer a mensagem no chat com o nome do usuário
#criar um socket para diferentes usuários se comunicar -> tunnel de comunicação
#lib utilizada flet -> aplicativo/site/programa de computador
#outras libs para site -> flask e django -> só criam sites
##########################################################################################################################################################
##########################################################################################################################################################
#3 passos para criar sistemas utilizando flet
#1 - importar o flet
import flet as ft

#2 - criar a função principal do sistema
#def -> definir
#obrigatóriamente você precisa passar uma pagina inicial como parâmetro dessa função
def main(pagina):
    #criar  o titulo
    titulo = ft.Text('ChatZap')

    #função que cria o tunnel de comunicação
    def enviar_mensagem_tunel(mensagem):
        print(mensagem)
        chat.controls.append(ft.Text(mensagem))
        pagina.update()
        
    #pubsub -> tunel de comunicação -> subscribe -> enviar para todo mundo
    pagina.pubsub.subscribe(enviar_mensagem_tunel) 

    titulo_janela = ft.Text('Bem vindo(a) ao ChatZap')
    campo_nome_usuario = ft.TextField(label='Escreva seu nome no chat')

    def enviar_mensagem(evento):
        #enviar mensagem
            #usuario: mensagem
        texto = f'{campo_nome_usuario.value}: {texto_mensagem.value}'
        
        
        #enviar mensagem no tunnel para todos
        pagina.pubsub.send_all(texto)

        #limpar o campo da mensagem
        texto_mensagem.value = ''
        pagina.update()


    texto_mensagem = ft.TextField(label='Digite sua mensagem', on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)
    chat = ft.Column()
    #organizando elementos na tela utilizando coluna e linhas
    linha_mensagem = ft.Row([texto_mensagem, botao_enviar])

    def entrar_chat(evento):
        #tirar titulo da página
        pagina.remove(titulo)
        #tirar botão iniciar chat
        pagina.remove(botao_iniciar)
        #fechar o popup
        janela.open = False
        #criar o campo de texto de enviar mensagem
        pagina.add(chat)
        #criar botão enviar mensagem #criar o chat  
        pagina.add(linha_mensagem)
        #escrever a mensagem usuário entrou no chat
        texto_entrou_chat = f'{campo_nome_usuario.value} entrou no chat'  
        pagina.pubsub.send_all(texto_entrou_chat)      
        

        pagina.update()


    botao_entrar_chat = ft.ElevatedButton('Entrar no chat', on_click=entrar_chat)
    janela = ft.AlertDialog(
        title=titulo_janela,
        content= campo_nome_usuario,
        #é permitido colocar mais de um botão -> em lista []
        actions= [botao_entrar_chat]
    )


#toda função usada dentro de um botão precisa receber um evento como parâmetro
#toda vez que alguma ação do código editar a pagina, ela precisa ser atualizada via código
    def abrir_popup(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update() #-> atualiza a pagina após qualquer ação de edição
        
        
    botao_iniciar = ft.ElevatedButton('Iniciar Chat', on_click=abrir_popup)
    #colocar coisas na pagina
    #adicionar elementos na pagina
    pagina.add(titulo)
    pagina.add(botao_iniciar)
    

#3 - executar o sistema
#você precisa passar uma função para que seu sistema seja inicializado
#o parâmetro view seta o modo de visualização, se é app ou site
ft.app(main, view=ft.WEB_BROWSER)
