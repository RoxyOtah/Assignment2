s = "This is an odd place"
# length should be 20
print ("Length of s =%d" % len(s))

#first occurence of "a" should be at index 8
print("The first occurence of the letter a = %d" % s.index("a"))

# number of a's should be 2
print("a occurs %d times" %s.count("a"))

# slicing the strings into bits
print ("The first five characters are '%s'" % s[:5])
print ("The next five characters are '%s'" % s[5:10])
print ("The thirteenth charactersare '%s'" % s[12])
print ("The characters with odd index are '%s'" %s[1::2])


#EXERCISE 2 - use a replace function to change the nouns and adjectives
passage = """As I flew my fast car through the big city, I couldn't help
but notice the old tree standing tall in the center of the road. I
pulled over and got out to take a closer look, and that's when I saw it:
a beautiful house nestled in the branches of the tree. I walked up to
the house and noticed a green book lying on the doorstep. I picked it up
and began to read, and soon I was transported to a different city, one
filled with towering trees and beautiful houses. I drove my fast car
through the streets, taking in the sights and sounds of this new city,
until I finally returned to my own old house, where I sat down to read
my green book under the shade of a nearby big tree."""

# nouns
passage = passage.replace("car", "bicycle")
passage = passage.replace("city", "village")
passage = passage.replace("tree", "bush")
passage = passage.replace("house", "cottage")
passage = passage.replace("book", "tablet")

#adjectives
passage = passage.replace("fast", "swift")
passage = passage.replace("big", "large")
passage = passage.replace("old", "ancient")
passage = passage.replace("green", "blue")
passage = passage.replace("beautiful", "stunning")


print(passage)

