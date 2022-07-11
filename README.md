# SCRIPT DE POSTAGEM AUTOMÁTICA PARA TWITTER QUE GERA RELATÓRIO EM .TXT 
###### [Go to English](https://github.com/RadiHaz/twi-bot/edit/main/README.md#english)
---
## ***Portugês Brasileiro/Brazilian Portuguese***

# Sobre
## Script que utiliza uma conta do Twitter, [específica para desenvolvedores](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api "Documentação para iniciar com a API"), para fazer postagens automatizadas com base em *arrays* com *strings* e temporizador entre postagens que você pode predefinir. Ao executar o script, tendo sucesso na postagem do tweet, ele gera um relatorio que é inserido no arquivo *relatorio.txt*, que contém, respectivamente: 
## 1. ID do tweet (para contabilizar quantos tweets foram feitos desde a execução do script);
## 2. A frase do tweet em sí; 
## 3. Hora da postagem do tweet, HH:MM:SS.

### *Então, inicialmente, seria algo como: `1 Ô meu querido ta bem gelada essa coquinha ai em? 21:50:33`*

---

## *IMPORTANTE: Para iniciar, você **PRECISA** ter suas [chaves de autenticação da API do Twitter](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api "Documentação para iniciar com a API"). O processo é relativamente rápido e geralmente aceitam o cadastro em pouco tempo, no meu caso foi instantâneo. Daqui em diante presumirei que você já tem acesso às suas chaves.*

---

# Começando com o script
## Utiliza tweepy para autenticação das chaves E para fazer as postagens.

## [Documentação do tweepy](https://docs.tweepy.org/en/stable/)

`$ pip install tweepy`

Este é um bot de postagem automatizada com base em um layout de frase para o tweet que você pode predefinir, mas, inicialmente, será o seguinte:

`frase = ["Ô", <String>, <String>]`

*exemplo de output esperado: **"Ô meu guerreiro ta certo esses 20% de gorjeta aqui?"***.

O código funciona nesta **EXATA** ordem quando o arquivo **twitterbot.py** é executado:

1. Autentica suas chaves da API do Twitter.
2. Declara a variável `contador` que serve como uma espécie de ID e é inserida no *relatorio.txt*, ao gerá-lo.


Pode-se notar que não está incluso nenhum executável *.exe* ou *.bat*. Isso é porque considero meu código como um template base para você moldar como desejar a partir daqui.

### ***English***
