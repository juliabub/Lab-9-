#The authors' names are: Julia, Julia, and Christina

#B) Joining Strings
#we think that the expression will give an error
#"-".join("cat")
#This puts dashes in between the letts of the string "cats"

lines = ["Haiku frogs in snow", "A limerick came from Nantucket", "Tetrametric drum-beats thrumming, Hiawathianic rhythm." ]
def breakify(lyric):
    "<br>".join(lyric)
breakify(lines)

#This function takes a parameter and adds a <br> between each different string in the parameter. 
