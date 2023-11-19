import os

import pyttsx3
from PyPDF2 import PdfReader

files = []
try:
    with open("filenamesList.txt", "r") as f:
        try:
            files = f.readlines()
            textToSpeech = pyttsx3.init()
            textToSpeech.setProperty('rate', 150)
            textToSpeech.setProperty('volume', 5.0)
            for f in files:
                try:
                    with open(f, "rb") as pdfFileObj:
                        try:
                            print('[OPEN "' + f + '" SUCCESS ]')
                            reader = PdfReader(pdfFileObj)
                            text = ""
                            for page in reader.pages:
                                text += page.extract_text().strip().replace("\n", " ")
                                textToSpeech.save_to_file(
                                    text, os.path.splitext(f)[0] + ".mp3"
                                )
                            try:
                                textToSpeech.runAndWait()
                                textToSpeech.stop()
                            except RuntimeError:
                                print("Error Converting Text to Speech")
                        except:
                            print("Failed While Converting PDF file to Text ")
                except (IOError, PermissionError, FileNotFoundError):
                    print("Error opening the file " + f)
        except (IOError, OSError):
            print("Error Reading from file")
except (FileNotFoundError, PermissionError, OSError):
    print("Error opening the file")
