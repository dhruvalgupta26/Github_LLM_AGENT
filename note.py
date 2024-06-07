from langchain_core.tools import tool

@tool
def note_tool(note):
    """
    saves a note to the local file 
    
    Keyword arguments:
        note: the text note to save
    """
    with open("notes.txt","a") as f:
        f.write(note + "\n")