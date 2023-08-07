# 9.5 Challenge: Wax poetic

# In this challenge, write a program that contains that generates poetry.
# Create five lists for different word types:
import  random

nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "curdles"]
prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverbs = ["curious", "extravagantly", "tantalizingly", "furiously", "sensuously"]

def make_a_poem():
    noun1 = random.choice(nouns)
    noun2 = random.choice(nouns)
    noun3 = random.choice(nouns)
    verb1 = random.choice(verbs)
    verb2 = random.choice(verbs)
    verb3 = random.choice(verbs)
    adj1 = random.choice(adjectives)
    adj2 = random.choice(adjectives)
    adj3 = random.choice(adjectives)
    prep1 = random.choice(prepositions)
    prep2 = random.choice(prepositions)
    adverb1 = random.choice(adverbs)
    article = random.choice(["A", "An"])

    poem = (
        f"{article} {adj1} {noun1}\n\n"
        f"{article} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}\n"
        f"{adverb1}, the {noun1} {verb2}\n"
        f"the {noun2}, {verb3}, {prep2} a {adj3} {noun3}\n"
    )
    return poem

poem = make_a_poem()
print(poem)