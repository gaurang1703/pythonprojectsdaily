# string concatenations

programmer = "? Programmer"

print("whos is the {}".format(programmer))
print("who is the "+programmer)
print("hello who is the {programmer}")

verb = input("verb: ")
verb1 = input("vrb1: ")
famousLanguage = input("language: ")

adj = input("Adjective: ")
turn=input("turn-left: ")

madlib = f"Programming is very intresting {adj}! Until you {turn} into bug/error beacause \I dont know i hate errors {verb}. Stay hydrated  and {verb1} like {famousLanguage} "

# print("madlib",madlib)

loop=1

while(loop<2):
    name=input("name: ")
    pronoun=input("pronoun: ")
    name1=input("name: ")
    place=input("Place: ")
    food=input("Food: ")

    print("----------------------------")
    sentence=f"Hijo {name} ra {name1} ghumdai jana {pronoun} kt dekheu near {place} ani {food} khayeu "
    print(sentence)
    loop=loop+1