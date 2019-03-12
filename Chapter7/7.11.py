#File System: Explain the data structures and algorithms that you would use to design an in-memory file system.
#Illustrate with an example in code where possible.

class File():
    def __init__(self, name, content):
        self.name = name
        self.content = content

class Directory():
    def __init__(self,name):
        self.name = name
        self.parent = None
        self.subdirectories = {}
        self.files = {}

    def add_directory(self,directory): #ADDING DIRECTORY INTO ANOTHER DIRECTORY
        if directory.parent !=None:
            del directory.parent.subdirectories[directory.name] #if this directory has already parent delete this directory from it's parent's subdirectory
        directory.parent = self
        self.subdirectories[directory.name] = directory

    def addFile(self, file):
        self.files[file.name] = file.content

    def get(self, path):
        parts = path.split("/")
        directory = self
        for part in parts:
            if part == '..':
                directory = directory.parent
                if not directory:
                    return None
            elif part in directory.subdirectories:
                directory = directory.subdirectories[part]
            elif part in directory.files:
                return directory.files[part]
            else:
                return None
        return directory

def main():
    directory0 = Directory("root")
    directory1 = Directory("food")
    directory2 = Directory("vegetables")

    file1 = File("arugula.png", "This is classified")

    directory0.add_directory(directory1)
    directory1.add_directory(directory2)
    directory2.addFile(file1)

    print(directory0.get("food/vegetables/arugula.png"))


if __name__ == '__main__':
    main()
