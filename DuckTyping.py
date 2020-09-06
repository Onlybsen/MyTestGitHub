
#If a bird walks like a duck, quecks like a bird and swims like a duck then the bird is a duck
class vi:
    def start(self):
        print("VI:This editor is best for program editing.")
        print("It can do certain things that no other editor can.")

class notepad:
    def start(self):
        print("NOTEPAD:This editor is good for word processing,")
        print("not suitable for program development.")

def myeditor(obj): #it is irrelevant the 'obj' object belongs to which class, 'vi' or 'notepad'
    obj.start()

ed = notepad()
myeditor(ed)
print()
ed = vi()
myeditor(ed)