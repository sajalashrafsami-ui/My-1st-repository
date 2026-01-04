from PyPDF2 import PdfMerger
all= [r"C:\Users\HP\Downloads\Presentation sociology.pdf.pdf",r"C:\Users\HP\Downloads\Theoretical_QA_Special_Relativity.pdf.pdf",r"C:\Users\HP\Downloads\Theoretical_QA_Photoelectric_Compton.pdf.pdf"]
m= PdfMerger()
for i in all:
    m.append(i)
m.write("three.pdf")
m.close()