def gerar_relatorio(contador, tweet, hora) : 
    relatorio = open("relatorio.txt", "a")
    conteudo_relatorio = [str(contador), tweet, hora]
    for lines in conteudo_relatorio:
        relatorio.write(lines + ' ')
    relatorio.writelines('\n')
    relatorio.close()
    contador += 1
    print(f'Sleep ativado. {conteudo_relatorio}')