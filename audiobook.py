import PyPDF3
import pyttsx3

pdfread = PyPDF3.PdfFileReader(open(file name))
speaker = pyttsx3.init()

for i in range(pdfread.numPages):
    text = pdfread.getPage(i).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()

speaker.save_to_file(text,"audio.mp3")
speaker.runAndWait()