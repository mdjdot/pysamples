#!/usr/bin/env python3
from PyPDF4 import PdfFileReader
from PyPDF4 import PdfFileWriter

"""
www.360doc.com/content/19/0505/06/39062348_833408454.shtml
"""


def extractPdfInfo():
    with open("./Python 面试题.pdf", "rb") as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        pageNum = pdf.getNumPages()

        result = f"""
        infomatino anout  {"./Python 面试题.pdf"}

        author:     {info.author}
        creator:    {info.creator}
        procucer:   {info.producer}
        subject:    {info.subject}
        title:      {info.title}
        page nums:  {pageNum}
        """

        print(result)


def readWritePdf():
    with open("./Python 面试题.pdf", "rb") as f:
        pdfReader = PdfFileReader(f)
        pdfWriter = PdfFileWriter()
        page = pdfReader.getPage(0)
        pdfWriter.addPage(page)
        with open("./new.pdf", "wb") as f1:
            pdfWriter.write(f1)


if __name__ == "__main__":
    extractPdfInfo()
    readWritePdf()
