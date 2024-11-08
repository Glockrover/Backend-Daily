#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def main():
    try:
        file_name = "./Input/Names/inivited_names.txt"
        file = open_txt(file_name)
        letter = "./Input/letters/starting_letter.docx"
        message = open_letter(letter)
        for names in file:
            x = message.replace("[name]", names)
            with open("ReadyToSend.txt", "a") as file:
                file.write(f"{x}\n\n--------------------------------------\n\n")
    except:
        raise FileNotFoundError

def open_txt(text_file):
    names = list()
    with open(text_file, 'r') as file:
        contents = file.readlines()
        for name in contents:
            names.append(name.strip())
    return names

def open_letter(letter_docx):
    letter = ""
    with open(letter_docx) as file:
        content = file.readlines()
        for words in content:
            letter += words
    return letter

if __name__ == "__main__":
    main()