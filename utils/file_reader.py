from pypdf import PdfReader
from docx import Document


def read_pdf(file):

    text = ""

    reader = PdfReader(file)

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:

            text += page_text

    return text


def read_docx(file):

    doc = Document(file)

    text = ""

    for para in doc.paragraphs:

        text += para.text + "\n"

    return text


def read_txt(file):

    return file.read().decode("utf-8")
