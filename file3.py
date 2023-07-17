import fitz
import os

def add_text_as_image_to_pdf(input_file, output_file, texts, positions, page_numbers):
    pdf = fitz.open(input_file)

    page = pdf[0]
    for text, position in zip(texts, positions):
        text_box = fitz.Rect(position[0], position[1], position[2], position[3])

        # Add text as a free text annotation to the page
        annot = page.add_freetext_annot(text_box, text)
        annot.update()

    page = pdf[2]
    position = positions [2]
    text = texts[0]
    text_box = fitz.Rect(position[0], position[1], position[2], position[3])

    # Add text as a free text annotation to the page
    annot = page.add_freetext_annot(text_box, text)
    annot.update()

    pdf.save(output_file)
    pdf.close()

# Input file path
input_folder = 'input pdf'
input_file_name = 'file3.pdf'
input_file = os.path.join(input_folder, input_file_name)

text_file = 'input.txt'
positions = [(180, 194, 500, 600), (180, 175, 500, 600), (90, 293, 500, 600)]
page_numbers = [1,3]

with open(text_file, 'r') as file:
    text_input = file.read()

texts = text_input.strip().split('\t')
del texts[0]
del texts[1]
print(texts)
texts = texts[:2]
print(texts)

# Output folder path
output_folder = texts[1]
print(output_folder)
output_file_name = '3. SURAT AKUAN PEMBIDA.pdf'
output_file = os.path.join(output_folder, output_file_name)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

add_text_as_image_to_pdf(input_file, output_file, texts, positions, page_numbers)
