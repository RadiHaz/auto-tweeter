import tweepy
from gerarFrase import gerar_frase
from gerarRelatorio import gerar_relatorio
from time import sleep
from datetime import datetime
import creds

# Authenticate to Twitter
auth = tweepy.OAuthHandler(creds.API_KEY, creds.API_SECRET)
auth.set_access_token(creds.ACCESS_KEY,
                      creds.ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)
contador = 1
while True:
    tweet = gerar_frase() # frase com as 3 partes completas
    hora = datetime.now().strftime("%H:%M:%S") # hora minuto e segundo da execução do codigo/postagem do tweet
    api.update_status(tweet)
    gerar_relatorio(contador, tweet, hora)
    sleep(3600) # 1 hora entre postagens

# optional error catch block // bloco opcional para tratar erros
# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication")
