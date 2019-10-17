

pupilsInClass = 15
sweetsInBag = 35

sweetsPerStudent = divmod(sweetsInBag, pupilsInClass)

print("There are sweets",sweetsPerStudent[0],"per student, of these",sweetsPerStudent[1],"are leftover")

