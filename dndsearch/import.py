
import pyPdf
import sys
import sql
from sql import Page

def getPageContents(page, pdf):
    return pdf.getPage(page).extractText()
    
if __name__ == '__main__':
    pdf = pyPdf.PdfFileReader(file(sys.argv[2], 'rb'))
    page_count = pdf.getNumPages()

    # Sql stuff
    session = sql.Session()

    for i in range(0, page_count):
      p = Page(sys.argv[1], i, getPageContents(i, pdf))
      Page.add(p, session=session)