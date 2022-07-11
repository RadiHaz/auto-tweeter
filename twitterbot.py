import tweepy
from gerarFrase import gerar_frase
from gerarRelatorio import gerar_relatorio
from time import sleep
from datetime import datetime
import creds

# Authenticate to Twitter
AUTH = tweepy.OAuthHandler(creds.API_KEY, creds.API_SECRET)
AUTH.set_access_token(creds.ACCESS_KEY,
                      creds.ACCESS_SECRET)
API = tweepy.API(AUTH, wait_on_rate_limit=True)
contador = 1
while True:
    tweet = gerar_frase() # frase com as 3 partes completas
    hora = datetime.now().strftime("%H:%M:%S") # hora minuto e segundo da execução do codigo/postagem do tweet
    API.update_status(tweet)
    gerar_relatorio(contador, tweet, hora)
    sleep(3600) # 1 hora entre postagens

# optional error catch block // bloco opcional para tratar erros
# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication")
