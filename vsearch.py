def search4vowels(phrase: str) -> set:
    """"Returns the set of vowels found in 'phrase'."""
    return set('aeiou').intersection(set(phrase))


def search4letters(phrase: str, letters: str='aeiou') -> set:
    """Returns the set of 'letter' found in 'phrase'."""
    return set(phrase).intersection(set(phrase))