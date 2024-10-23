import PyPDF2

# Caminho para o arquivo PDF
caminho_pdf = 'arquivo.pdf'

# Abrindo o arquivo PDF
with open(caminho_pdf, 'rb') as pdf_file:
    # Criando um objeto de leitura do PDF
    leitor_pdf = PyPDF2.PdfReader(pdf_file)
    
    # Inicializando uma variável para armazenar o texto
    texto_completo = ""

    # Iterando sobre todas as páginas e extraindo o texto
    for pagina in range(len(leitor_pdf.pages)):
        texto_pagina = leitor_pdf.pages[pagina].extract_text()
        texto_completo += texto_pagina

# Exibindo o texto extraído
texto_completo = texto_completo.split()

# cont = 0
# while(cont<len(texto_completo)):
#     print('Position = ',cont,'   ',texto_completo[cont])
#     cont = cont + 1

print('===========================================')
print('===========================================')
print('===========================================')
print('===========================================')

positionWbc = texto_completo.index('WBC')
positionRbc = texto_completo.index('RBC')
positionHgb = texto_completo.index('HGB')
positionHct = texto_completo.index('HCT')
positionPlt = texto_completo.index('PLT')
positionNeu = texto_completo.index('NEU')
positionLym = texto_completo.index('LYM')
positionMon = texto_completo.index('MON')
positionEos = texto_completo.index('EOS')
positionBaso = texto_completo.index('BASO')

print('PROTOCOLO = ',texto_completo[4])



RBC = texto_completo[positionRbc+1]
print('RBC = ',RBC)

HCT = texto_completo[positionHct+1]
print('HCT = ',HCT)

HGB = texto_completo[positionHgb+1]
print('HGB = ',HGB)

WBC = texto_completo[positionWbc+1]
print('Leucócitos WBC = ',WBC)

PLT = texto_completo[positionPlt+1]
print('PLT = ',PLT)




NEU = texto_completo[positionNeu+1]
print('NEU = ',NEU)

EOS = texto_completo[positionEos+1]
print('EOS = ',EOS)

BASO = texto_completo[positionBaso+1]
print('BASO = ',BASO)

LYM = texto_completo[positionLym+1]
print('LYM = ',LYM)

MON = texto_completo[positionMon+1]
print('MON = ',MON)









