
def shifting(message: str, shift:int):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    message_list = list(message)
    for i in range(len(message_list)):
        if message_list[i] in alphabet:
            index = (alphabet.index(message_list[i]) + shift) % len(alphabet)
            if index >= len(alphabet) - 1:
                index -= len(alphabet)
            message_list[i] = alphabet[index]
    return "".join(message_list)

def cipher():
    
    start = "yes"
    
    while start == "yes":
        option = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")

        while option not in ["encode", "decode"]:
            option = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
        
        message = input("Type your message: \n")
        shift = int(input("Type the shift number: \n"))
        
        result = ""
        if option == "encode":
            result = shifting(message, shift)
        else: 
            result = shifting(message, -shift)
        print(f"Here's the encoded result: {result}")
        
        start = input("Type 'yes' if you want to go again. Otherise type 'no'. \n")
        
    print("Goodbye")