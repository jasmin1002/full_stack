class Student:
    # Constructor
    def __init__(self, name="student", age=0, tracks=[], score=0.00):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    # Modify existing name (i.e set new name)
    def change_name(self, name):
        self.name = name

    # Modify age
    def change_age(self, age):
        self.age = int(age)

    # Print score
    def get_score(self):
        print('{:.2f}'.format(self.score))

    # Add new entry
    def add_track(self, track):
        self.tracks.append(track)


Bob = Student()

# Expected methods
print(Bob.__dict__)
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

print(Bob.__dict__)

Files = Student("Files", 27, ["General", "Full Stack"], 98.23)
Files.get_score()
print(Files.__dict__)

