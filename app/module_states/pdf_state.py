import os 
from fpdf import FPDF
from app import app

class PDF_STATE(FPDF):

    title_header = ''
    path_static = app.config['STATIC_FOLDER']
    path_logo = os.path.join( path_static , 'logo.png')

    def header(self):
        # Logo
        self.image(self.path_logo, 10, 10, 10)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Title
        self.cell(0, 10, self.title, 0, 0, 'C')
        # Line break
        self.ln(30)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def print_attribute(self, txt):
        # Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        self.cell(0, 10, txt = txt, border = 0, ln = 1, align = '', fill = False, link = '')        