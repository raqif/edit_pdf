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
        text_instance = page.insert_textbox(text_box, text)
        text_instance.update({'flags': fitz.TEXTBOX_ADD_OVERWRITE})
        
    pdf.save(output_file)
    pdf.close()

# Input file path
input_folder = 'input pdf'
input_file_name = 'file2.pdf'
input_file = os.path.join(input_folder, input_file_name)

text_file = 'input.txt'
positions = [(225, 203, 500, 600), (225, 243, 500, 600), (225, 223, 500, 600)]
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
output_file_name = '2. BORANG SENARAI JENAMA BAHAN-BAHAN MAKANAN YANG DIGUNAKAN.pdf'
output_file = os.path.join(output_folder, output_file_name)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

add_text_to_pdf(input_file, output_file, texts, positions, page_number)
