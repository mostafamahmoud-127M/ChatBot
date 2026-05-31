responses = {
'hello':'Hi there! welcome to my model' ,
'help': ' I can asist you about anything you need' ,
'about': "I am a White Box AI guardrail built to prevent hallucinations." ,
'thanks': "You're very welcome! Happy to help." ,
'bye' : 'Bye Bye nice to meet you '
}

def modelreponses(clean_input) :
    matchedText = responses[clean_input]
    return f"Batabeto:{matchedText}"

while True :

    user_iput = input('\nyou:')
    clean_input = user_iput.lower().strip()

    reply = responses.get(clean_input, 'I dont understand')

    if clean_input in responses :
        output = modelreponses(clean_input)
        print(output)

    elif clean_input == 'exit' :
        print('batabeto: goodbyeee')
        break

    else :
        output = reply
        print(output)
