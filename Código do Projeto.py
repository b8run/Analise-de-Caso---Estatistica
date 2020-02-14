import pandas as pd
import matplotlib.pyplot as pyplot
from pylab import *
import numpy as np
def read(arquivo):
    leitura = pd.read_csv(arquivo, encoding='utf-8', sep=';' )
    return leitura

data2014 = read('pessoas2014-2.csv')
data2015 = read('pessoas2015-2.csv')
data2016 = read('pessoas2016-2.csv')

'''' Segue sequencia de variaveis da esquerda para direita que vão ser trabalhadas:
sexo, estado_fisico,tipo_envolvido,uso_solo, condicao_metereologica,fase_dia, causa_acidente, municipio, br, dia_semana '''
#ESCOPO DE VARIAVEIS PARA EVITAR REPETIÇÃO DE TERMO;

MASCULINO = ('sexo == "Masculino"')
FEMININO = ('sexo == "Feminino"')
#gravidade do acidente
MORTO = ('estado_fisico =="Morto"')
ILESO = ('estado_fisico == "Ileso"')
Grave = ('estado_fisico == "Ferido Grave"')
LEVE = ('estado_fisico == "Ferido Leve"')
#tipo envolvido
CONDUTOR = ('tipo_envolvido =="Condutor"')
PASSAGEIRO = ('tipo_envolvido =="Passageiro"')
PEDESTRE = ('tipo_envolvido =="Pedestre"')
CAVALEIRO = ('tipo_envolvido =="Cavaleiro"')
#localidade ou meio
RURAL = ('uso_solo == "Rural"')
URBANO = ('uso_solo == "Urbano"')
#condição metereologica
CLARO = ('condicao_metereologica == "Ceu Claro"')
NUBLADO = ('condicao_metereologica == "Nublado"')
SOL = ('condicao_metereologica == "Sol"')
CHUVA = ('condicao_metereologica == "Chuva"')
NEBLINA = ('condicao_metereologica == "Nevoeiro/neblina"')
VENTO = ('condicao_metereologica == "Vento"')
#Fase do dia
NOITE = ('fase_dia == "Plena noite"')
ANOITECER = ('fase_dia == "Anoitecer"')
DIA = ('fase_dia == "Pleno dia"')
AMANHECER = ('fase_dia == "Amanhecer"')
#causa dos acidentes
OUTRAS = ('causa_acidente == "Outras"')
DORMINDO = ('causa_acidente == "Dormindo"')
dVIA = ('causa_acidente == "Defeito na via"')
ANIMAIS = ('causa_acidente == "Animais na Pista"')
ATENCAO = ('causa_acidente == "Falta de atenção"')
ALCOOL = ('causa_acidente == "Ingestão de álcool"')
MECANICO = ('causa_acidente == "Defeito mecânico em veículo"')
VELOCIDADE = ('causa_acidente == "Velocidade incompatível"')
SINALIZACAO = ('causa_acidente == "Desobediência à sinalização"')
DISTANCIA_SEGURA = ('causa_acidente == "Não guardar distância de segurança"')
ULTRAPASSAGEM = ('causa_acidente == "Ultrapassagem indevida"')
# cidades
CAMPINA_GRANDE = ('municipio == "CAMPINA GRANDE"')
RECIFE= ('municipio == "RECIFE"')
JOAO_PESSOA= ('municipio == "JOAO PESSOA"') #br
#recife e jp

BR101 = ('br == 101')
#recife
BR232 = ('br == 232')
BR408 = ('br == 408')
#campina grande
BR230 = ('br == 230')
BR104 = ('br == 104')

#dia da semana

SEGUNDA = ('dia_semana == "Segunda"')
TERCA = ('dia_semana == "Terça"')
QUARTA = ('dia_semana == "Quarta"')
QUINTA = ('dia_semana == "Quinta"')
SEXTA = ('dia_semana == "Sexta"')
SABADO = ('dia_semana == "Sábado"')
DOMINGO = ('dia_semana == "Domingo"')

# FIM DAS DECLARAÇÕES DE VARIAVEIS

#iniciando funções
#funções para determina o indice de ferimentos dos acidentados na qual mais ocorre a nivel Brasil
def dia_semana_maioracidentes(arquivo):
    segunda = len(arquivo.query(CAMPINA_GRANDE).query(SEGUNDA))
    terca = len(arquivo.query(CAMPINA_GRANDE).query(TERCA))
    quarta = len(arquivo.query(CAMPINA_GRANDE).query(QUARTA))
    quinta = len(arquivo.query(CAMPINA_GRANDE).query(QUINTA))
    sexta = len(arquivo.query(CAMPINA_GRANDE).query(SEXTA))
    sabado = len(arquivo.query(CAMPINA_GRANDE).query(SABADO))
    domingo = len(arquivo.query(CAMPINA_GRANDE).query(DOMINGO))
    semana = [segunda, terca, quarta, quinta, sexta, sabado, domingo]
    return semana

def mortos_fasediaUrb (arquivo):
    #frequencia absoluta nivel brasil
    amanhacer = len(arquivo.query(MORTO).query(URBANO).query(AMANHECER))
    dia = len(arquivo.query(MORTO).query(URBANO).query(DIA))
    anoitecer = len(arquivo.query(MORTO).query(URBANO).query(ANOITECER))
    noite = len(arquivo.query(MORTO).query(URBANO).query(NOITE))
    total = noite + anoitecer + dia + amanhacer
    mortos_urbano = [amanhacer, dia, anoitecer, noite, total]
    return mortos_urbano

def mortos_fasediaRur (arquivo):
    #frequencia absoluta nivel brasil
    amanhacer = len(arquivo.query(MORTO).query(RURAL).query(AMANHECER))
    dia = len(arquivo.query(MORTO).query(RURAL).query(DIA))
    anoitecer = len(arquivo.query(MORTO).query(RURAL).query(ANOITECER))
    noite = len(arquivo.query(MORTO).query(RURAL).query(NOITE))
    total = noite+ anoitecer + dia + amanhacer
    mortos_rural = [ amanhacer, dia, anoitecer, noite, total ]
    return mortos_rural

def GravementeferidosUrbano (arquivo):
    #frequencia absoluta nivel brasil
    amanhacer = len(arquivo.query(Grave).query(URBANO).query(AMANHECER))
    dia = len(arquivo.query(Grave).query(URBANO).query(DIA))
    anoitecer = len(arquivo.query(Grave).query(URBANO).query(ANOITECER))
    noite = len(arquivo.query(Grave).query(URBANO).query(NOITE))
    total = noite + anoitecer + dia + amanhacer
    feridos_graveUrbano = [amanhacer, dia, anoitecer, noite, total]
    return feridos_graveUrbano

def GravementeferidosRural (arquivo):
    #frequencia absoluta nivel brasil
    amanhacer = len(arquivo.query(Grave).query(RURAL).query(AMANHECER))
    dia = len(arquivo.query(Grave).query(RURAL).query(DIA))
    anoitecer = len(arquivo.query(Grave).query(RURAL).query(ANOITECER))
    noite = len(arquivo.query(Grave).query(RURAL).query(NOITE))
    total = noite+ anoitecer + dia + amanhacer
    feridos_graveRural = [ amanhacer, dia, anoitecer, noite, total ]

    return feridos_graveRural

def feridosleveUrbano (arquivo):
    #frequencia absoluta nivel brasil
    amanhacer = len(arquivo.query(LEVE).query(URBANO).query(AMANHECER))
    dia = len(arquivo.query(LEVE).query(URBANO).query(DIA))
    anoitecer = len(arquivo.query(LEVE).query(URBANO).query(ANOITECER))
    noite = len(arquivo.query(LEVE).query(URBANO).query(NOITE))
    total = noite+ anoitecer + dia + amanhacer
    leveURBANO= [ amanhacer, dia, anoitecer, noite, total ]
    return leveURBANO

def feridosleverural (arquivo):
    #frequencia absoluta nivel brasil
    amanhacer = len(arquivo.query(LEVE).query(RURAL).query(AMANHECER))
    dia = len(arquivo.query(LEVE).query(RURAL).query(DIA))
    anoitecer = len(arquivo.query(LEVE).query(RURAL).query(ANOITECER))
    noite = len(arquivo.query(LEVE).query(RURAL).query(NOITE))
    total = noite+ anoitecer + dia + amanhacer
    leveRURAL= [ amanhacer, dia, anoitecer, noite, total ]
    return leveRURAL

def ilesosrural (arquivo):
    #frequencia absoluta nivel brasil
    amanhacer = len(arquivo.query(ILESO).query(RURAL).query(AMANHECER))
    dia = len(arquivo.query(ILESO).query(RURAL).query(DIA))
    anoitecer = len(arquivo.query(ILESO).query(RURAL).query(ANOITECER))
    noite = len(arquivo.query(ILESO).query(RURAL).query(NOITE))
    total = noite+ anoitecer + dia + amanhacer
    ilesosRURAL = [ amanhacer, dia, anoitecer, noite, total ]
    return ilesosRURAL

def ilesosurbano (arquivo):
    #frequencia absoluta nivel brasil
    amanhacer = len(arquivo.query(ILESO).query(URBANO).query(AMANHECER))
    dia = len(arquivo.query(ILESO).query(URBANO).query(DIA))
    anoitecer = len(arquivo.query(ILESO).query(URBANO).query(ANOITECER))
    noite = len(arquivo.query(ILESO).query(URBANO).query(NOITE))
    total = noite+ anoitecer + dia + amanhacer
    ilesosURBANO = [ amanhacer, dia, anoitecer, noite, total ]
    return ilesosURBANO

def valoresparabr230_104CG(arquivo):
    mortes230 = len(arquivo.query(MORTO).query(BR230).query(CAMPINA_GRANDE))
    ilesos230 = len(arquivo.query(ILESO).query(BR230).query(CAMPINA_GRANDE))
    feridoLeve230 = len(arquivo.query(LEVE).query(BR230).query(CAMPINA_GRANDE))
    feridoGrave230 = len(arquivo.query(Grave).query(BR230).query(CAMPINA_GRANDE))
    #BR 104
    mortes104 = len(arquivo.query(MORTO).query(BR104).query(CAMPINA_GRANDE))
    ilesos104 = len(arquivo.query(ILESO).query(BR104).query(CAMPINA_GRANDE))
    feridoLeve104 = len(arquivo.query(LEVE).query(BR104).query(CAMPINA_GRANDE))
    feridoGrave104 = len(arquivo.query(Grave).query(BR104).query(CAMPINA_GRANDE))
    total_mortes = mortes104 + mortes230
    total_ilesos = ilesos104 + ilesos230
    total_leve = feridoLeve104 + feridoLeve230
    total_grave = feridoGrave104 + feridoGrave230
    valores = [[mortes230, ilesos230, feridoLeve230, feridoGrave230],
               [mortes104, ilesos104,feridoLeve104, feridoGrave104],
               [total_mortes, total_ilesos, total_leve, total_grave]]
    return valores

def causa_acidentes(arquivo):
    #br 230
    acidentes_velocidade230 = len(arquivo.query(VELOCIDADE).query(BR230).query(CAMPINA_GRANDE))
    acidentes_animais230 = len(arquivo.query(ANIMAIS).query(BR230).query(CAMPINA_GRANDE))
    acidentes_ultrapassagem230 = len(arquivo.query(ULTRAPASSAGEM).query(BR230).query(CAMPINA_GRANDE))
    acidentes_alcool230 = len(arquivo.query(ALCOOL).query(BR230).query(CAMPINA_GRANDE))
    #br 104
    acidentes_velocidade104 = len(arquivo.query(VELOCIDADE).query(BR104).query(CAMPINA_GRANDE))
    acidentes_animais104 = len(arquivo.query(ANIMAIS).query(BR104).query(CAMPINA_GRANDE))
    acidentes_ultrapassagem104 = len(arquivo.query(ULTRAPASSAGEM).query(BR104).query(CAMPINA_GRANDE))
    acidentes_alcool104 = len(arquivo.query(ALCOOL).query(BR104).query(CAMPINA_GRANDE))
    #soma brs
    velocidade =  len(arquivo.query(CAMPINA_GRANDE).query(VELOCIDADE))
    animais = len(arquivo.query(CAMPINA_GRANDE).query(ANIMAIS))
    ultrapass = len(arquivo.query(CAMPINA_GRANDE).query(ULTRAPASSAGEM))
    alco = len(arquivo.query(CAMPINA_GRANDE).query(ALCOOL))
    outrastotal = len(arquivo.query(CAMPINA_GRANDE).query(OUTRAS))
    dormindototal = len(arquivo.query(CAMPINA_GRANDE).query(DORMINDO))
    defeitototal = len(arquivo.query(CAMPINA_GRANDE).query(MECANICO))
    defeviatotal = len(arquivo.query(CAMPINA_GRANDE).query(dVIA))
    atencaototal = len(arquivo.query(CAMPINA_GRANDE).query(ATENCAO))
    sinaliztotal = len(arquivo.query(CAMPINA_GRANDE).query(SINALIZACAO))
    distancetotal = len(arquivo.query(CAMPINA_GRANDE).query(DISTANCIA_SEGURA))
    #indice de mortalidade
    velocidade_morto = len(arquivo.query(CAMPINA_GRANDE).query(VELOCIDADE).query(MORTO))
    animais_morto = len(arquivo.query(CAMPINA_GRANDE).query(ANIMAIS).query(MORTO))
    ultrapass_morto = len(arquivo.query(CAMPINA_GRANDE).query(ULTRAPASSAGEM).query(MORTO))
    alcool_morto = len(arquivo.query(CAMPINA_GRANDE).query(ALCOOL).query(MORTO))
    outrastotal_morto = len(arquivo.query(CAMPINA_GRANDE).query(OUTRAS).query(MORTO))
    dormindototal_morto = len(arquivo.query(CAMPINA_GRANDE).query(DORMINDO).query(MORTO))
    defeitototal_morto = len(arquivo.query(CAMPINA_GRANDE).query(MECANICO).query(MORTO))
    defeviatotal_morto = len(arquivo.query(CAMPINA_GRANDE).query(dVIA).query(MORTO))
    atencaototal_morto = len(arquivo.query(CAMPINA_GRANDE).query(ATENCAO).query(MORTO))
    sinaliztotal_morto = len(arquivo.query(CAMPINA_GRANDE).query(SINALIZACAO).query(MORTO))
    distancetotal_morto = len(arquivo.query(CAMPINA_GRANDE).query(DISTANCIA_SEGURA).query(MORTO))

    # Indice geral
    acidentes_velocidadeGERAL = len(arquivo.query(VELOCIDADE))
    acidentes_animaisGERAL = len(arquivo.query(ANIMAIS))
    acidentes_ultrapassagemGERAL = len(arquivo.query(ULTRAPASSAGEM))
    acidentes_alcoolGERAL = len(arquivo.query(ALCOOL))

    valores_causa = [
        [acidentes_velocidade230,acidentes_animais230,acidentes_ultrapassagem230,acidentes_alcool230],
        [acidentes_velocidade104,acidentes_animais104,acidentes_ultrapassagem104,acidentes_alcool104],
        [velocidade,animais,ultrapass,alco, outrastotal, dormindototal, defeitototal, defeviatotal, atencaototal, sinaliztotal, distancetotal],
        [acidentes_velocidadeGERAL,acidentes_animaisGERAL,acidentes_ultrapassagemGERAL,acidentes_alcoolGERAL],
    [velocidade_morto, animais_morto, ultrapass_morto, alcool_morto, outrastotal_morto, dormindototal_morto, defeitototal_morto, defeviatotal_morto, atencaototal_morto, sinaliztotal_morto, distancetotal_morto]]
    return valores_causa

def graficoacidentes(arquivo,nome):
    x_list = [causa_acidentes(arquivo)[2][0],causa_acidentes(arquivo)[2][1], causa_acidentes(arquivo)[2][2], causa_acidentes(arquivo)[2][3],causa_acidentes(arquivo)[2][4],causa_acidentes(arquivo)[2][5],causa_acidentes(arquivo)[2][6],causa_acidentes(arquivo)[2][7],causa_acidentes(arquivo)[2][8],causa_acidentes(arquivo)[2][9],causa_acidentes(arquivo)[2][10]]
    labels_list = ['Velocidade', 'Animais', 'Ultrapassagem', 'Álcool', 'Outros', 'Dormindo', 'Defeito Mecânico','Defeito via', 'Falta de atenção','Desobediência de sinalização','Não manteve distância segura']
    pyplot.axis('equal')
    pyplot.pie(x_list, labels=labels_list,autopct='%1.1f%%',)
    pyplot.title('Causa dos acidentes em '+ nome)
    pyplot.show()

def graficoferidos(arquivo, nome):
    #Grafico que mostra o tipo de ferimento para cada BR
    height = [valoresparabr230_104CG(arquivo)[0][0], valoresparabr230_104CG(arquivo)[1][0],
              valoresparabr230_104CG(arquivo)[0][1], valoresparabr230_104CG(arquivo)[1][1],
              valoresparabr230_104CG(arquivo)[0][2], valoresparabr230_104CG(arquivo)[1][2],
              valoresparabr230_104CG(arquivo)[0][3], valoresparabr230_104CG(arquivo)[1][3]]
    bars = ('Mortes BR230', 'Mortes BR104', 'Ilesos BR230', 'Ilesos BR104', 'Ferido Leve BR230', 'Ferido Leve BR104',
            'Ferido Grave BR230', 'Ferido Grave BR104')
    y_pos = np.arange(len(bars))
    plt.barh(y_pos, height, color =['#000080','#696969','#FF0000','#90EE90','#008000','#808000','#546945','#056564'] )
    plt.yticks(y_pos, bars)
    xlabel(nome)
    plt.show()


def totalacidentes(arquivo):
    total230 = len(arquivo.query(BR230).query(CAMPINA_GRANDE))
    total104 = len(arquivo.query(BR104).query(CAMPINA_GRANDE))
    totalMascu = len(arquivo.query(CAMPINA_GRANDE).query(MASCULINO))
    totalFemin = len(arquivo.query(CAMPINA_GRANDE).query(FEMININO))
    acidentes_total = len(arquivo.query(CAMPINA_GRANDE))
    total = [total230, total104, acidentes_total, totalMascu, totalFemin]
    return total

def graficototal(arquivo, arquivo2, arquivo3):
    height = [totalacidentes(arquivo)[2],totalacidentes(arquivo2)[2], totalacidentes(arquivo3)[2]]
    bars = (2014, 2015, 2016)
    y_pos = np.arange(len(bars))

    plt.bar(y_pos, height, color =['#000080','#696969','#FF0000'])
    plt.xticks(y_pos, bars)
    plt.title('Acidentes totais em relação aos anos e as duas BRs')
    plt.ylabel('Acidentes')
    plt.xlabel('Anos')
    plt.show()

def graficobrseparado(arquivo, arquivo2, arquivo3):
    barWidth = 0.25
    bars1 = [totalacidentes(arquivo)[1], totalacidentes(arquivo2)[1], totalacidentes(arquivo3)[1]]
    bars2 = [totalacidentes(arquivo)[0], totalacidentes(arquivo2)[0], totalacidentes(arquivo3)[0]]
    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    plt.bar(r1, bars1, color='#7f6d5f', width=barWidth, edgecolor='white', label='104')
    plt.bar(r2, bars2, color='#557f2d', width=barWidth, edgecolor='white', label='230')
    plt.ylabel('Acidentes', fontweight='bold')
    plt.xlabel('Anos', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(bars1))], ['2014', '2015', '2016'])
    plt.title('Acidentes nas Rodovias de Campina Grande\n(BR 104) e (BR 230)')
    plt.legend()
    plt.show()

def graficoporsexo(arquivo, arquivo2, arquivo3):
    barWidth = 0.25
    bars1 = [totalacidentes(arquivo)[3], totalacidentes(arquivo2)[3], totalacidentes(arquivo3)[3]]
    bars2 = [totalacidentes(arquivo)[4], totalacidentes(arquivo2)[4], totalacidentes(arquivo3)[4]]
    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    plt.bar(r1, bars1, color='#1E90FF', width=barWidth, edgecolor='white', label='Masculino')
    plt.bar(r2, bars2, color='#FF0000', width=barWidth, edgecolor='white', label='Femino')
    plt.ylabel('Acidentes', fontweight='bold')
    plt.xlabel('Anos', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(bars1))], ['2014', '2015', '2016'])
    plt.title('Acidentes totais em relação a sexo')
    plt.legend()
    plt.show()

def mortos_por_horario(arquivo, nome):
    height = [mortos_fasediaUrb(arquivo)[0],mortos_fasediaUrb(arquivo)[1],mortos_fasediaUrb(arquivo)[2],mortos_fasediaUrb(arquivo)[3]]
    bars = ('Amanhecer', 'Pleno dia', 'Anoitecer', 'Plena noite')
    y_pos = np.arange(len(bars))

    plt.bar(y_pos, height, color=['#000080', '#696969', '#FF0000','#FF1233'])
    plt.xticks(y_pos, bars)
    plt.title('Acidentes totais em relação ao meio Urbano e Rural')
    plt.ylabel('Acidentes')
    plt.xlabel('Anos')
    plt.show()

def diasemana(arquivo, ano):
#demonstra a quantidade de acidentes em relação a dia da semana
    height = [dia_semana_maioracidentes(arquivo)[0],dia_semana_maioracidentes(arquivo)[1],dia_semana_maioracidentes(arquivo)[2],dia_semana_maioracidentes(arquivo)[3],dia_semana_maioracidentes(arquivo)[4],dia_semana_maioracidentes(arquivo)[5],dia_semana_maioracidentes(arquivo)[6]]
    bars = ('Segunda', 'Terça','Quarta', 'Quinta','Sexta', 'Sábado','Domingo')
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, height, color = ['#000080','#DC143C','#FF0000','#90EE90','#008000','#808000','#D2691E'])
    plt.xticks(y_pos, bars)
    plt.title('Acidentes relacionados a dia da semana')
    plt.ylabel('Acidentes')
    plt.xlabel('Dia que mais ocorreu acidente no ano de: ' + ano)
    plt.show()

def acidentes_mortalidade(arquivo,ano):#nome do csv e string da data
    height = [causa_acidentes(arquivo)[4][0], causa_acidentes(arquivo)[4][1], causa_acidentes(arquivo)[4][2],
     causa_acidentes(arquivo)[4][3], causa_acidentes(arquivo)[4][4], causa_acidentes(arquivo)[4][5],
     causa_acidentes(arquivo)[4][6], causa_acidentes(arquivo)[4][7], causa_acidentes(arquivo)[4][8],
     causa_acidentes(arquivo)[4][9], causa_acidentes(arquivo)[4][10]]
    bars = ('Velocidade', 'Animais', 'Ultrapassagem', 'Álcool', 'Outros', 'Dormindo', 'Defeito Mecânico','Defeito via', 'Falta de atenção','Desobediência de sinalização','Não manteve distância segura')
    y_pos = np.arange(len(bars))
    plt.barh(y_pos, height,
             color=['#000080', '#696969', '#FF0000', '#90EE90', '#008000', '#808000', '#546945', '#056564'])
    plt.yticks(y_pos, bars)
    title('Causa dos acidentes que levaram\na morte em '+ano)
    ylabel('Causas dos acidentes que levaram a morte')
    xlabel('Numero de mortes nas Brs 104 e 230')
    plt.show()

#realizando chamadas de variaveis definidas por função

feridos14 = graficoferidos(data2014, 'Valores para ano 2014')
feridos15 = graficoferidos(data2015,'Valores para ano 2015')
feridos16 = graficoferidos(data2016,'Valores para ano 2016')
""""
pizza1 = graficoacidentes(data2014, '2014')
pizza2 = graficoacidentes(data2015, '2015')
pizza3 = graficoacidentes(data2016, '2016')
"""
valor = graficototal(data2014, data2015, data2016)
valor2 = graficobrseparado(data2014, data2015, data2016)
valor3 = graficoporsexo(data2014, data2015, data2016)

morto = mortos_por_horario(data2014, 'Valores para horário do dia 2014')
morto2 = mortos_por_horario(data2015, 'Valores para horário do dia 2015')
morto3 = mortos_por_horario(data2016, 'Valores para horário do dia 2016')

# Grafico relacionado a numero de acidentes que ocorrem durante os dias da semana
dia = diasemana(data2014,'2014')
dia2 = diasemana(data2015,'2015')
dia3 = diasemana(data2016, '2016')

#Grafico que relaciona a quantidade de acidentes com a causa do acidente
morte = acidentes_mortalidade(data2014, '2014')
morte2 = acidentes_mortalidade(data2015,'2015')
morte3 = acidentes_mortalidade(data2016,'2016')