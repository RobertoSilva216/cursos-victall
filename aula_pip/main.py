import requests
requisicao = requests.get('https://jsonplaceholder.typicode.com/posts/1')
resposta = requisicao.json()

print(resposta)  # Exibe o conteúdo da resposta em formato JSON
print(f"Campo title: {resposta['title']}") #Exibe o campo title retornado no json
