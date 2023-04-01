def question():
    phrase = 'Ola amigos, como estao? tranquilos?'
    phrase = phrase.replace(' ', '').upper()
    counted_letters = dict()
    for letter in phrase:
        counted_letters[letter] = phrase.count(letter)
    most_showed_letter = max(counted_letters, key=lambda x: counted_letters[x])
    print(most_showed_letter)


question()
