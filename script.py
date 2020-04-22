# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

first_censor = "learning algorithms"
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]


#TEST to call on whole list in lower - works
def lower_the_list(lst):
    result2 = []
    result2.append([word.lower() for word in lst])
    return result2
#print(lower_the_list(proprietary_terms))

#TEST to call on broken text - works
def broken_text(text):
    text_lower = text.lower()
    broken_text = text_lower.split()
    return broken_text

#print(broken_text(email_two))


#TASK 2 - censor a string from text- works!
def censor_single_word(text, string):
    result = text.replace(string, " ")
    return result
    
print(censor_single_word(email_one, first_censor))


#TASK 3 - simplified from Task 2; censor list from email - works but not for grammar
def censor_multiple_words(text, lst):
    for word in lst:
        text = text.replace(word," ")
    return text
            
print(censor_multiple_words(email_two, proprietary_terms))

#works -- does not work if you change the name at the bottom for other than text. why??
def censor_multiple_words(text, lst):
    for word in lst:
        censored_word = ""
        for x in range(0, len(word)):
            if word[x] == " ":
                censored_word = censored_word + " "
            else:
                censored_word = censored_word + "X"
        text = text.replace(word,censored_word)
    return text
    
   # censored_text = []
    #for i in broken_text:
        #for wordl in lst_lower:
           # if i==wordl:
               # i.replace(wordl, "*").strip()
           #     censored_text.append("*")
           # else:
            #    censored_text.append(i)
            #return " ".join(censored_text)

   
    #censored_text = []
    #for i in broken_text: 
        #if i==([wordl for wordl in lst_lower]):
            #censored_text.append("*")
       # else:
           # censored_text.append(i)
           # return " ".join(censored_text)

                        # censored_text = []
    #for i in broken_text:
        #for wordl in lst_lower:
           # if i==wordl:
               # i.replace(wordl, "*").strip()
           #     censored_text.append("*")
           # else:
            #    censored_text.append(i)
            #return " ".join(censored_text)
        
