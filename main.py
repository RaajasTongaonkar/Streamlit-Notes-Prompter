"""
Streamlit version of the Notes Prompter.
Just a trial at making a simple teleprompter for guitar notes
The idea is, given a collection of notes, these will be shown on the screen one-by-one
Strumming pattern -> D-D-D-DU-UD-DUDU
16 strokes in ~3.6s for this song => ~0.225 for each stroke(?)
Guitar tutorial - https://www.youtube.com/watch?v=7sc0oB46uc4
Song - Cardigan by Taylor Swift
For a different song, will have to change the strumming pattern and the notes AND the sleep time
"""
import time
# from termcolor import colored,cprint
from os import system
import platform
import streamlit as st
# from time import sleep

st.set_page_config(
    layout="wide",
    page_title="Notes Prompter",
    page_icon="🎸"
)

def playSong(colour):
    
    # """Detect OS name to choose the correct string to clear the display"""
    OSName = platform.system()
    clearStr = "clear"
    if OSName=='Windows':
        clearStr='cls'

    # system(clearStr)
    getReady = 4
    with st.empty():
        while getReady > 0:
            getReady -= 1
            st.write(getReady)
            time.sleep(1)
        system(clearStr)
        st.write("")
    # return
    strummingPattern = "D-D-D-DU-UD-DUDU"
    notes = [
        "Dm,G,F,G",
        "Dm,G,F,G",
        "C,G,F,G",
        "Dm,G,F,G",
        "Dm,G,F,G",
        "C,G,F,G",
        "F,Am,C,F",
        "F,Am,G,F",
        "F,Am,G,F",
        "C,G,F,G",
        "C,G,F,G",
        "C,G,F,G",
        "C,G,F,G",
        "Dm,G,F,G",
        "F,Am,C,F"
    ]
    currentLineContainer = st.empty()
    currentNotesContainer = st.empty()
    nextLineContainer = st.empty()
    for k in range(len(notes)):
        # """Split each line of the notes into consituent chords"""
        chords = notes[k].split(',')

        for indChords in range(len(chords)):
            for indStrumming in range(len(strummingPattern)):
                m = 0
                j = 0

                # """Loop to colour the current chord"""
                currLine = ""
                while j < len(chords):
                    if j == indChords:
                        # st.write(colored(chords[j], colour), end=" ")
                        currLine += ":{}[{}] ".format(colour,chords[j])
                        # currentLine.write()
                    else:
                        # st.markdown(chords[j], end=" ")
                        currLine += chords[j]+" "
                    j += 1
                # st.write()
                # print(currLine)
                currentLineContainer.markdown(currLine)
                # return
                # """Loop to highlight the current strumming pattern to play ie D or U"""
                currNotes = ""
                while m < len(strummingPattern):
                    if m == indStrumming:
                        # """Keeping the commented part incase a future update wants to revert the dash highlighting behaviour"""
                        # if strummingPattern[m] == '-':
                        #     st.write(strummingPattern[m], end="")
                        # else:
                        # st.write(colored(strummingPattern[m], colour), end="")
                        currNotes += ":{}[{}]".format(colour,strummingPattern[m])
                    else:
                        # st.write(strummingPattern[m], end="")
                        currNotes += "{}".format(strummingPattern[m])
                    m += 1
                # st.write()
                currentNotesContainer.markdown(currNotes)

                # """This st.writes the next line to play"""
                if k != len(notes) - 1:
                    nextLineContainer.write(notes[k+1])
                    # st.write(notes[k + 1])
                else:
                    nextLineContainer.write("")
                time.sleep(0.22)
                # system(clearStr)
    currentLineContainer.write("")
    currentNotesContainer.write("")
    nextLineContainer.write("")
    time.sleep(1)
    st.write("Fin.")


if __name__=="__main__":
    # Colour can be 'red', 'green', 'blue', 'white', 'black', etc. More colours can be found on the homepage of termcolor
    #  https://github.com/termcolor/termcolor?tab=readme-ov-file#text-properties
    colour = 'red'
    playSong(colour)
    # cprint("This work?","red")
    # a = st.empty()
    # a.markdown(""":red[This is all]:blue[ red]""")
    # sleep(2)
    # system('clear')
    # a.metric(label="Temp", value="273 K", delta="1.2 K")