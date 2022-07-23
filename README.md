# SCRIPT DE POSTAGEM AUTOMÁTICA PARA TWITTER QUE GERA RELATÓRIO EM .TXT
[~~Go to English~~](https://github.com/RadiHaz/twi-bot)

## ***Portugês Brasileiro/Brazilian Portuguese***

## TL;DR/Início rápido:
1. Tenha suas chaves da [API do Twitter](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api "Documentação para iniciar com a API");
2. Tendo as chaves, renomeie o arquivo `creds.example.py` para `creds.py` e insira elas de acordo com os nomes das CONSTANTES;
3. No terminal, no diretório do script, execute: 
   ```terminal 
   $ pip install
   ```
4. Execute o script. Você deverá ver o seguinte output:

   ```console 
   Sleep ativado. ['1', 'Ô meu principe tem desconto se toma mais de 5?', '16:46:55']
   ```

# Sobre
Script que utiliza uma conta do Twitter, [específica para desenvolvedores](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api "Documentação para iniciar com a API"), para fazer postagens automatizadas com base em *arrays* com *strings* e temporizador entre postagens que você pode predefinir. Ao executar o script, tendo sucesso na postagem do tweet, ele gera um relatorio que é inserido no arquivo *relatorio.txt*, que contém, respectivamente: 
1. ID do tweet (para contabilizar quantos tweets foram feitos desde a execução do script);
2. A frase do tweet em sí; 
3. Hora da postagem do tweet, no formato HH:MM:SS.

*Então, inicialmente, seria algo como: `1 Ô meu querido ta bem gelada essa coquinha aí em? 21:50:33`*

## **IMPORTANTE**
Para iniciar, você **PRECISA** ter suas [chaves de autenticação da API do Twitter](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api "Documentação para iniciar com a API"). O processo é relativamente rápido e geralmente aceitam o cadastro em pouco tempo, no meu caso foi instantâneo.

Tendo suas chaves, insira-as no arquivo *`creds.py`* (renomeie *`creds.example.py` para `creds.py`*). 

Daqui em diante presumirei que você já tem acesso às suas chaves e as importou corretamente.

Esse script utiliza [tweepy](https://docs.tweepy.org/en/stable/ "Documentação da biblioteca") para autenticação das chaves *E* para fazer as postagens.

No diretório do script, execute no terminal:

```terminal 
   $ pip install
   ```

# Começando com o script

Este é um bot de postagem automatizada com base em um layout de frase para o tweet que você pode predefinir, mas, inicialmente, será o seguinte:

```python 
frase = ["Ô", <String>, <String>]
```

Fosse: 
```python
frase = ["Ô", "meu guerreiro", "ta certo esses 20% de gorjeta aqui?"]
```

O output esperado seria: **"Ô meu guerreiro ta certo esses 20% de gorjeta aqui?"**.

O código funciona nesta **EXATA** ordem quando o script **twitterbot.py** é executado:

1. Autentica suas chaves da API do Twitter:
```python
   AUTH = tweepy.OAuthHandler(creds.API_KEY, creds.API_SECRET)
   AUTH.set_access_token(creds.ACCESS_KEY,
                      creds.ACCESS_SECRET)
```
2. Declara a CONSTANTE `API`, que é utilizada dentro do loop para fazer as postagens;
```python
   API = tweepy.API(AUTH, wait_on_rate_limit=True)
```
3. Declara a variável `contador` que serve como uma espécie de ID e é inserida no *relatorio.txt*, ao gerá-lo:
```python
   contador = 1
```
4. Entra no `while` loop e:

   1. Gera a frase aleatória para o tweet com a função `gerar_frase`e atribui ela à variável `tweet`:
   ```python
      tweet = gerar_frase() # frase com as 3 partes completas
   ```
   2. Identifica a hora atual e atribui ela à variável `hora`:
   ```python
      hora = datetime.now().strftime("%H:%M:%S") # hora minuto e segundo da execução do codigo/postagem do tweet
   ```
   3. Através da CONSTANTE `API`, com o método `update_status`, faz a postagem da frase contida em `tweet`;
   ```python
      API.update_status(tweet)
   ```
   4. Gera o relatório através da função `gerar_relatorio`, que tem como parâmetros `contador, tweet, hora`, que são autoexplicativos:
   ```python
      gerar_relatorio(contador, tweet, hora)
   ```
   5. Define o intervalo entre as postagens com o método `sleep`, em *segundos*:
   ```python
      sleep(3600)
   ```
   ---
   Então temos:
   
   ```python
      while True:
          tweet = gerar_frase() # frase com as 3 partes completas
          hora = datetime.now().strftime("%H:%M:%S") # hora minuto e segundo da execução do codigo/postagem do tweet
          API.update_status(tweet)
          gerar_relatorio(contador, tweet, hora)
          sleep(3600) # 1 hora entre postagens
      ```

### ***English***
