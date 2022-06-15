from PyPDF2 import PdfFileMerger

# junta os pdfs passados na variável arquivos_PDF em ordem

merger = PdfFileMerger()

# Cria uma lista com nomes de arquivos
arquivos_PDF = [r'..\junta_PDF\texto_1.pdf',
             r'..\junta_PDF\texto_2.pdf', r'..\junta_PDF\texto_3.pdf']

# Iterar sobre a lista de nomes de arquivos
for arquivo_PDF in arquivos_PDF:
    # Append PDF files
    merger.append(arquivo_PDF)
    
# Escreve o PDF juntado
merger.write("paginas_combinadas.pdf")
merger.close()
