# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

first_censor = "learning algorithms"
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

#TASK 2 - censor a string from text - works but disregards punctuation (i will look into that later)
def censor_single_word(text, string):
    result = text.replace(string, " ")
    return result
    
print(censor_single_word(email_one, first_censor))

#TASK 3 - inspired from Task 2 - censors list from email - works but disregards punctuation too
def censor_multiple_words(text, lst):
    for word in lst:
        text = text.replace(word," ")
    return text
            
print(censor_multiple_words(email_two, proprietary_terms))

#This was my first try at Task 3 - it does not work. Is there a reason why returning a variable that I created (like for Task 2) does not work here - does it have to do with the loop?
def censor_multiple_words(text, lst):
    for word in lst:
        censored_text = text.replace(word," ")
    return censored_text
            
