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
input_file_name = 'file8.pdf'
input_file = os.path.join(input_folder, input_file_name)

text_file = 'input.txt'
positions = [(200, 116, 500, 600), (200, 153, 500, 600), (200, 134, 500, 600)]
page_number = 1

with open(text_file, 'r') as file:
    text_input = file.read()

texts = text_input.strip().split('\t')
del texts[0]
print(texts)
texts = texts[:3]
print(texts)

# Output folder path
output_folder = texts[2]
print(output_folder)
output_file_name = '8. BORANG SIJIL KURSUS PENGENDALI MAKANAN.pdf'
output_file = os.path.join(output_folder, output_file_name)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

add_text_as_image_to_pdf(input_file, output_file, texts, positions, page_number)
