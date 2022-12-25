from fpdf import FPDF,HTMLMixin
import datetime
import re


class CreatePDFHtml(FPDF, HTMLMixin):
    pass


def create_pdf_at_html(html_code,user_name='unregfile'):
    pdf = CreatePDFHtml()
    pdf.add_page()
    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu', '', 14)
    pdf.write_html(html_code,ul_bullet_char='-')
    file_name = str(user_name)+(re.sub(r"\D", "-", str(datetime.datetime.now())))
    name = f'media/pdf/{datetime.datetime.now().year}/{datetime.datetime.now().month}/{datetime.datetime.now().day}/{file_name}.pdf'
    try:
        pdf.output(name)
    except:
        print('не сохранилась')
    return name