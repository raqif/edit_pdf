import fitz
import os

def add_text_as_image_to_pdf(input_file, output_file, texts, positions, page_numbers):
    pdf = fitz.open(input_file)

    for page_number in page_numbers:
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
input_file_name = 'file8.pdf'
input_file = os.path.join(input_folder, input_file_name)

text_file = 'input.txt'
positions = [(200, 116, 500, 600), (200, 153, 500, 600), (200, 134, 500, 600)]
page_numbers = [1,3]

with open(text_file, 'r') as file:
    text_input = file.read()

texts = text_input.strip().split('\t')

# Output file path
output_file = os.path.join(input_folder, 'output.pdf')

add_text_as_image_to_pdf(input_file, output_file, texts, positions, page_numbers)
