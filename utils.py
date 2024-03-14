import configurations as config
from jinja2 import Environment, FileSystemLoader
from fpdf import FPDF


def get_system_prompt(novel_details):
    system_prompt = {}
    file_loader = FileSystemLoader(config.TEMPLATES_FOLDER)
    env = Environment(loader=file_loader)
    template = env.get_template(config.SYSTEM_PROMPT_TEMPLATE_FILE)
    system_prompt = template.render(novel_details)
    return system_prompt


def text_to_pdf(content, filepath):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', size=13)
    encoder = 'latin-1'
    content = content.encode('latin-1', errors='ignore')
    content = content.decode()
    pdf.multi_cell(0, 10, content)
    pdf.output(filepath)
