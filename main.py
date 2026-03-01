import pypdf  
import pyttsx3
from tkinter import Tk
from tkinter.filedialog import askopenfilename


Tk().withdraw()


book = askopenfilename()

if book:
    reader = pypdf.PdfReader(book)
    pages = len(reader.pages)
    
    player = pyttsx3.init()
    
    for num in range(0, pages):
        page = reader.pages[num]
        text = page.extract_text()  
        
        if text:
            player.say(text)
            player.runAndWait()  
