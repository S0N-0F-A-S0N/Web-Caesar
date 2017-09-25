from helpers import alphabet_position, rotate_character

def encrypt(message, rotation):
    encrypted = ""
    for i in message:
        letter = rotate_character(i, (rotation % 26))
        encrypted += letter
    return(encrypted)




def main():
    message = "Hello world"
    rotation = input("Rotation: \n")
    encrypt(str(message), int(rotation))



if __name__ == "__main__":
    main()
