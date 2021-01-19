from reportlab.lib.colors import HexColor
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.lib.pagesizes import A4


def create_name_tag(name, position):
    canv = Canvas('text-on-image.pdf', pagesize=A4)
    img = ImageReader('static/name.jpg')
    registerFont(TTFont('optima', 'static/OPTIMA.TTF'))
    registerFont(TTFont('optima-bold', 'static/OPTIMA-BOLD.TTF'))

    # now begin the work
    x = 100
    y = 100
    w = 75 * mm
    h = 25 * mm
    canv.drawImage(img, x, y, w, h, anchor='sw', anchorAtXY=True, showBoundary=False)
    canv.setFont('optima-bold', 18)
    canv.setFillColor(HexColor('#742013'))  # change the text color
    canv.drawCentredString(x + w * 0.5, y + h * 0.5, name)
    canv.drawCentredString(x + w * 0.5, y + h * 0.3, position)
    canv.save()
