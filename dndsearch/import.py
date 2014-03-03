
import pyPdf
import sys
import sql
from sql import Page
import Queue
import threading

page_queue = Queue.Queue()

def getPageContents(page, pdf):
    return pdf.getPage(page).extractText()


def queue_worker():
    while True:
        page = page_queue.get(True)
        Page.add(page)


for i in range(4):
    t = threading.Thread(target=queue_worker)
    t.daemon = True
    t.start()

    
if __name__ == '__main__':
    pdf = pyPdf.PdfFileReader(file(sys.argv[2], 'rb'))
    page_count = pdf.getNumPages()

    # Sql stuff
    session = sql.Session()

    for i in range(0, page_count):
        p = Page(sys.argv[1], i, getPageContents(i, pdf))
        page_queue.put_nowait(p)

