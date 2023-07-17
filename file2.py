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

    page = pdf[1]
    position = positions [3]
    text = texts[0]
    text_box = fitz.Rect(position[0], position[1], position[2], position[3])

    # Add text as a free text annotation to the page
    annot = page.add_freetext_annot(text_box, text)
    annot.update()

    page = pdf[2]
    position = positions [4]
    text = texts[0]
    text_box = fitz.Rect(position[0], position[1], position[2], position[3])

    # Add text as a free text annotation to the page
    annot = page.add_freetext_annot(text_box, text)
    annot.update()

    page = pdf[3]
    position = positions [5]
    text = texts[0]
    text_box = fitz.Rect(position[0], position[1], position[2], position[3])

    # Add text as a free text annotation to the page
    annot = page.add_freetext_annot(text_box, text)
    annot.update()

    page = pdf[4]
    position = positions [6]
    text = texts[0]
    text_box = fitz.Rect(position[0], position[1], position[2], position[3])

    # Add text as a free text annotation to the page
    annot = page.add_freetext_annot(text_box, text)
    annot.update()

    page = pdf[5]
    position = positions [7]
    text = texts[0]
    text_box = fitz.Rect(position[0], position[1], position[2], position[3])

    # Add text as a free text annotation to the page
    annot = page.add_freetext_annot(text_box, text)
    annot.update()

    page = pdf[6]
    position = positions [8]
    text = texts[0]
    text_box = fitz.Rect(position[0], position[1], position[2], position[3])

    # Add text as a free text annotation to the page
    annot = page.add_freetext_annot(text_box, text)
    annot.update()

    pdf.save(output_file)
    pdf.close()

# Input file path
input_folder = 'input pdf'
input_file_name = 'file2.pdf'
input_file = os.path.join(input_folder, input_file_name)

text_file = 'input.txt'
positions = [(230, 185, 500, 600), (230, 225, 500, 600), (230, 205, 500, 600), (130, 100, 500, 600), (130, 86, 500, 600), (130, 91, 500, 600), (130, 88, 500, 600), (130, 86, 500, 600), (130, 101, 500, 600)]
page_numbers = [1,3]

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
output_file_name = '2. BORANG SENARAI JENAMA BAHAN-BAHAN MAKANAN YANG DIGUNAKAN.pdf'
output_file = os.path.join(output_folder, output_file_name)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

add_text_as_image_to_pdf(input_file, output_file, texts, positions, page_numbers)
