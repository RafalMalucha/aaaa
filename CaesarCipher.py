text = str(input("Enter plain text:  "))
shift = int(input("Shift:  "))
encrypted = ""
for char in text:
    shifted_for = 0
    char_number = ord(char)
    #przesuniecie dla duzych liter
    if ord(char) >= 65 and ord(char) <= 90:
        for i in range(shift):
            shifted_for += 1
            char_number += 1
            if char_number > 90:
                char_number = 65
            if shifted_for == shift:
                encrypted += str(chr(char_number))
    #przesuniecie dla malych liter
    if ord(char) >= 97 and ord(char) <= 122:
        for i in range(shift):
            shifted_for += 1
            char_number += 1
            if char_number > 122:
                char_number = 97
            if shifted_for == shift:
                encrypted += str(chr(char_number))
    #zachowanie spacji miedzy slowami
    if ord(char) == 32:
        encrypted += str(chr(32))
        
print(f"Plain text: {text}\n" f"Shifted for: {shift}\n" f"Encrypted text: {encrypted}")
        

            