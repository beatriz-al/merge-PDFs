from glob import glob
from PyPDF2 import PdfFileMerger

# Script que junta todos os arquivos com a extensao .pdf de dentro do diretório atual

def pdf_merge():
    merger = PdfFileMerger()
    allpdfs = [a for a in glob("*.pdf")]

    [merger.append(pdf) for pdf in allpdfs]

    with open("Merged_pdfs.pdf", "wb") as new_file:
        merger.write(new_file)


if __name__ == "__main__":
    pdf_merge()


