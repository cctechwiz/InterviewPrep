def is_odd(n):
    return (n % 2) != 0


def count_odds(character_counts):
    odds = 0

    for n in character_counts.values():
        if is_odd(n):
            odds = odds + 1

    return odds


def count_characters(word):
    character_counts = {}

    for c in word:
        character_counts[c] = character_counts.get(c, 0) + 1

    return character_counts


def is_scrambled_palindrome(word):
    character_counts = count_characters(word)
    odds = count_odds(character_counts)

    return (odds == 0) or (odds == 1)



if __name__ == '__main__':
    print('Is Scrambled Palindrome\n')

    words = ['racecar', 'torro', 'test', 'aajjddttiieed', 't', 'ttt']

    for word in words:
        if is_scrambled_palindrome(word):
            print(f'{word} is a scrambled palindrome')
