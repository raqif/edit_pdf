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

    # Add text as a free text annotation to the page
    annot = page.add_freetext_annot(text_box, text)
    annot.update()

    pdf.save(output_file)
    pdf.close()

# Input file path
input_folder = 'input pdf'
input_file_name = 'file7.pdf'
input_file = os.path.join(input_folder, input_file_name)

text_file = 'input.txt'
positions = [(235, 110, 500, 600), (235, 129, 500, 600), (235, 147, 500, 600), (235, 165, 500, 600), (400, 460, 500, 600), (400, 365, 500, 600), (400, 384, 500, 600), (400, 403, 500, 600), (400, 421, 500, 600), (400, 439, 500, 600)]
page_numbers = [1,3]

with open(text_file, 'r') as file:
    text_input = file.read()

texts = text_input.strip().split('\t')
# texts = texts[:3]
del texts[0], texts[4], texts[4]
print(texts)

# Output folder path
output_folder = texts[2]
print(output_folder)
output_file_name = '7. BORANG HARGA TAWARAN MENGIKUT SAJIAN.pdf'
output_file = os.path.join(output_folder, output_file_name)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

add_text_as_image_to_pdf(input_file, output_file, texts, positions, page_numbers)
