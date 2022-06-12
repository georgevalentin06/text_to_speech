import PyPDF2
import gtts


file = open('FILEPATH', 'rb')

pdf_file = PyPDF2.PdfFileReader(file)
pages = pdf_file.numPages
pdf_text = []

for page in range(pages):
    current_page = pdf_file.getPage(page)
    pdf_text.append(current_page.extractText())


converted_text = " ".join(pdf_text)

audio = gtts.gTTS(text=converted_text, lang='en')

audio.save("Audio.mp3")