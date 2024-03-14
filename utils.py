import configurations as config
from jinja2 import Environment, FileSystemLoader
from reportlab.pdfgen import canvas


def get_system_prompt(novel_details):
    system_prompt = {}
    file_loader = FileSystemLoader(config.TEMPLATES_FOLDER)
    env = Environment(loader=file_loader)
    template = env.get_template(config.SYSTEM_PROMPT_TEMPLATE_FILE)
    system_prompt = template.render(novel_details)
    return system_prompt


def text_to_pdf(content, filepath):
    pdf_canvas = canvas.Canvas(filepath)
    pdf_canvas.drawString(100, 750, content)
    pdf_canvas.save()
