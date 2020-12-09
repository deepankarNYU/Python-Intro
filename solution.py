
### welcome_assignment_answers
### Input - All eight questions given in the assignment.
### Output - The right answer for the specific question.

import hashlib 

def welcome_assignment_answers(question):
    #The student doesn't have to follow the skeleton for this assignment.
    #Another way to implement is using a "case" statements similar to C.
    if question == "Are encoding and encryption the same? - Yes/No":
        print("1")
        return "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        print("2")
        return "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        print("3")
        return "Yes"
    elif question == "Is a hashed message supposed to be un-hashed?":
        print("4")
        return "No"
    elif question ==  "What is the MD5 hashing value to the following message: 'NYU Computer Networking' - Use MD5 hash generator and use the answer in your code":
        print("5")
        result = ''
        result += hashlib.md5(b"NYU Computer Networking").hexdigest()
        return result
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        print("6")
        return "No"
    elif question == "What layer from the TCP/IP model the protocol DHCP belongs to? - The answer should be a numeric number":
        print("7")
        return 5
    elif question == "What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number":
        print("8")
        return 4
    else:
        return "no"
# Complete all the questions.

    

if __name__ == "__main__":
    #use this space to debug and verify that the program works
    debug_question = "Are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers(debug_question))
