from PyPDF2 import PdfFileMerger

# junta os pdfs passados na variável arquivos_PDF em ordem
merger = PdfFileMerger()

# Cria uma lista com nomes de arquivos
arquivos_PDF = [r'..\junta_PDF\exercicios-python-secao16_4e.pdf', r'..\junta_PDF\AE_REST_API_Guide_5.6.0.pdf',
                r'..\junta_PDF\exercicios-python-secao07_p2_25e.pdf']

def junta_pdfs(arquivos_PDF):
    # Iterar sobre a lista de nomes de arquivos
    for arquivo_PDF in arquivos_PDF:
        # Append PDF files
        merger.append(arquivo_PDF)

    # Escreve o PDF juntado
    merger.write("paginas_combinadas.pdf")
    merger.close()

junta_pdfs(arquivos_PDF)