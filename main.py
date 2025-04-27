from interface_chat import InterfaceChat
from assistente_commit import AssistenteCommit
from assistente_documentacao import AssistenteDocumentacao
from assistente_revisao import AssistenteRevisao
from assistente_teste_unitario import AssistenteTesteUnitario

def main():
    print("iniciando...")
    caminho_arquivo = "Projeto_Dados/twitch_analytics/data_analytics.py"
    print("processando AssistenteCommit...")
    assistente_commit = AssistenteCommit(caminho_arquivo=caminho_arquivo)
    assistente_chat = InterfaceChat(assistente_commit)
    lista_mensagens = assistente_chat.conversar("Você pode gerar uma sugestão de commit para o script data_analytics que estou enviando para você?")
    assistente_chat.apagar_assistente_completamente()

    #for msg in lista_mensagens:
    #    print(f"\nAssistenteCommit: {msg.text.value}")

    print("processando AssistenteDocumentacao...")
    assistente_documentacao = AssistenteDocumentacao(caminho_arquivo=caminho_arquivo)
    assistente_chat = InterfaceChat(assistente_documentacao)
    lista_mensagens = assistente_chat.conversar("Você pode gerar a documentação para o script data_analytics que estou enviando para você?")
    assistente_chat.apagar_assistente_completamente()

    #for msg in lista_mensagens:
    #    print(f"\nAssistenteDocumentacao: {msg.text.value}")

    print("processando AssistenteRevisao...")
    assistente_revisao = AssistenteRevisao(caminho_arquivo=caminho_arquivo)
    assistente_chat = InterfaceChat(assistente_revisao)
    lista_mensagens = assistente_chat.conversar("Você pode gerar uma revisão para o script data_analytics, evitando a criação de variáveis desnecessárias, Estou enviando o script para você")
    assistente_chat.apagar_assistente_completamente()

    #for msg in lista_mensagens:
    #    print(f"\nAssistenteRevisao: {msg.text.value}")

    print("processando AssistenteTesteUnitario...")
    assistente_teste_unitario = AssistenteTesteUnitario(caminho_arquivo=caminho_arquivo)
    assistente_chat = InterfaceChat(assistente_teste_unitario)
    lista_mensagens = assistente_chat.conversar("Elabore um teste unitário para data_analytics.py e para o método getStreamerStats(). Estou enviando para você o arquivo.")
    assistente_chat.apagar_assistente_completamente()

    #for msg in lista_mensagens:
    #    print(f"\nAssistenteTesteUnitario: {msg.text.value}")
    
    print("Fim do processamento  ...")

if __name__ == "__main__":
    main()