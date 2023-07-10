import fitz
import os

def add_text_to_pdf(input_file, output_file, texts, positions, page_number):
    pdf = fitz.open(input_file)
    print(pdf)
    page = pdf[page_number - 1]
    print(page)
    page.clean_contents()
    for text, position in zip(texts, positions):
        text_box = fitz.Rect(position[0], position[1], position[2], position[3])
        page.insert_textbox(text_box, text)

    pdf.save(output_file)
    pdf.close()

# Input file path
input_folder = 'input pdf'
input_file_name = 'file1.pdf'
input_file = os.path.join(input_folder, input_file_name)

text_file = 'input.txt'
positions = [(225, 103, 500, 600), (225, 143, 500, 600), (225, 123, 500, 600)]
page_number = 1

with open(text_file, 'r') as file:
    text_input = file.read()

texts = text_input.strip().split('\t')

# Output file path
output_folder = texts[2]
output_file_name = '1.KB (C) BORANG MAKLUMAT PENGGAJIAN PEKERJA PERKHIDMATAN MEMBEKAL MAKANAN BERMASAK.pdf'
output_file = os.path.join(output_folder, output_file_name)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

add_text_to_pdf(input_file, output_file, texts, positions, page_number)
