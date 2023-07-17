import fitz
import os

def add_text_as_image_to_pdf(input_file, output_file, texts, positions, page_number):
    pdf = fitz.open(input_file)
    page = pdf[page_number - 1]
    # more_rot = 90  # extra rotation desired
    # current_rot = page.rotation
    # page.set_rotation(current_rot + more_rot)

    for text, position in zip(texts, positions):


        text_box = fitz.Rect(position[0], position[1], position[2], position[3])

        # Add text as a free text annotation to the page
        annot = page.add_freetext_annot(text_box, text, rotate=90)
        annot.update()

        # # Rotate the annotation by 90 degrees
        # annot.rotate = -90

        # page.set_rotation(current_rot)

    pdf.save(output_file)
    pdf.close()

# Input file path
input_folder = 'input pdf'
input_file_name = 'file6.pdf'
input_file = os.path.join(input_folder, input_file_name)

text_file = 'input.txt'
positions = [(80, 1, 500, 600), (118, 1, 500, 600), (98, 1, 500, 600)]
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
output_file_name = '6. BORANG MAKLUMAT SUMBER KEWANGAN.pdf'
output_file = os.path.join(output_folder, output_file_name)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

add_text_as_image_to_pdf(input_file, output_file, texts, positions, page_number)
