import fitz
import os

def add_text_as_image_to_pdf(input_file, output_file, texts, positions, page_number):
    pdf = fitz.open(input_file)
    page = pdf[page_number - 1]

    for text, position in zip(texts, positions):
        text_box = fitz.Rect(position[0], position[1], position[2], position[3])

        # Add text as a free text annotation to the page
        annot = page.add_freetext_annot(text_box, text)
        annot.update()

    pdf.save(output_file)
    pdf.close()

# Input file path
input_folder = 'input pdf'
input_file_name = 'file4.pdf'
input_file = os.path.join(input_folder, input_file_name)

text_file = 'input.txt'
positions = [(230, 130, 500, 600), (230, 165, 500, 600), (230, 148, 500, 600)]
page_number = 1

with open(text_file, 'r') as file:
    text_input = file.read()

texts = text_input.strip().split('\t')

# Output file path
output_file = os.path.join(input_folder, 'output.pdf')

add_text_as_image_to_pdf(input_file, output_file, texts, positions, page_number)
