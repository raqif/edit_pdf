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
input_file_name = 'file1a.pdf'
input_file = os.path.join(input_folder, input_file_name)

text_file = 'input.txt'
positions = [(225, 130, 500, 600), (225, 167, 500, 600), (225, 149, 500, 600)]
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
output_file_name = '1.KB (A,B,SS) BORANG MAKLUMAT PENGGAJIAN PEKERJA PERKHIDMATAN MEMBEKAL MAKANAN BERMASAK.pdf'
output_file = os.path.join(output_folder, output_file_name)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

add_text_as_image_to_pdf(input_file, output_file, texts, positions, page_number)
