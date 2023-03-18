from datetime import datetime
import itertools


class Note:
    iterID = itertools.count()

    def __init__(self, text, tag):
        self.text = text
        self.tag = tag
        self.creationDate = datetime.today().strftime('%d-%m-%Y')
        self.id = next(self.iterID)

    def match(self, text, tag):
        return text in self.text or text in self.tag

    def __str__(self):
        return ("{0}: {1}\{2}\{3}\n".format(self.id, self.tag, self.text))


class Notebook:
    def __init__(self):
        self.notes = []

    def newNote(self, text, tag):
        self.notes.append(Note(text, tag))

    def modifyText(self, noteId, newText):
        for note in self.notes:
            if note.id == noteId:
                note.text = newText
                break

    def modifyTag(self, noteId, newTag):
        for note in self.notes:
            if note.id == noteId:
                note.tag = newTag
                break

    def search(self, substring):
        return [note for note in self.notes if note.match(substring)]


class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.options = {
            "1": self.showNotes,
            "2": self.searchNotes,
            "3": self.addNote,
            "4": self.modifyNote,
            "5": self.quit
        }

    def showMenu(self):
        print(
            """Notebook Menu
1. Show all Notes
2. Search Notes
3. Add note
4. Modify Note
5. Quit"""
        )

    def run(self):
        while True:
            self.showMenu()
            choice = input("Enter an option: ")
            action = self.options.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def showNotes(self, notes=None):
        if notes is None:
            notes = self.notebook.notes
        for note in notes:
            print(note)

    def searchNotes(self):
        keyword = input("Enter a keyword to search for: ")
        notes = self.notebook.search(keyword)
        self.showNotes(notes)

    def addNote(self):
        text = input("Enter a note: ")
        tag = input("Enter a tag: ")
        self.notebook.newNote(text, tag)
        print("Note added sucessfully")

    def modifyNote(self):
        noteId = int(input("Enter a note ID to modify: "))
        note = self.findNoteById(noteId)
        if note:
            print("1. Modify text")
            print("2. Modify tag")
            choice = input("Enter an option: ")
            if choice == "1":
                newText = input("Enter new text: ")
                self.notebook.modifyText(noteId, newText)
                print("Text modified sucessfully")
            elif choice == "2":
                newTag = input("Enter a new tag")
                self.notebook.modifyTag(noteId, newTag)
                print("Tag modified sucessfully")
            else:
                print("{0} is not a valid choice.".format(choice))
        else:
            print("Note not found")

    def findNoteById(self, noteId):
        for note in self.notebook.notes:
            if note.ID == noteId:
                return note
            return None

    def quit(self):
        print("Thank you for using notebook")
        raise SystemExit


if __name__ == "__main__":
    Menu().run()
