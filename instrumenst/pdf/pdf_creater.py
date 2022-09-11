from fpdf import FPDF,HTMLMixin
import datetime
import re


class CreatePDFHtml(FPDF, HTMLMixin):
    pass


def create_pdf_at_html(html_code,user_name='unregfile'):
    pdf = CreatePDFHtml()
    pdf.add_page()
    pdf.write_html(html_code)
    file_name = str(user_name)+(re.sub(r"\D", "-", str(datetime.datetime.now())))
    name = f'media/pdf/{datetime.datetime.now().year}/{datetime.datetime.now().month}/{datetime.datetime.now().day}/{file_name}.pdf'
    pdf.output(name)
    return name