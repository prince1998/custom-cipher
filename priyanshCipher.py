class CustomCipher:
    cipherText = []
    plainText = []

    def encryptMessage(self, plain_text):
        for character in plain_text:
            cipherTextChar = chr(ord(character) * len(plain_text))
            self.cipherText.append(cipherTextChar)
        return self.cipherText

    def decryptMessage(self, cipher_text):
        for character in cipher_text:
            plainTextChar = chr(ord(character)//len(cipher_text))
            self.plainText.append(plainTextChar)
        return self.plainText

cipher = CustomCipher()

choice = int(input("What would you like to do?\n1. Encrypt Message\n2. Decrypt Message\n3. Exit\n"))
while choice != 3:
    if choice == 1:
        plain_text = input("Enter text to encrypt:\n")
        cipher_text = cipher.encryptMessage(plain_text)
        print("Ciphertext = ",cipher_text)
        choice = int(input("What would you like to do?\n1. Encrypt text\n2. Decrypt text\n3. Exit\n"))


    elif choice == 2:
        cipher_text = input("Enter text to decrypt:\n")
        plain_text = cipher.decryptMessage(cipher_text)
        print("Plaintext = ",plain_text)
        choice = int(input("What would you like to do?\n1. Encrypt text\n2. Decrypt text\n3. Exit\n"))

    else:
        print("Bad Input")
        choice = int(input("What would you like to do?\n1. Encrypt text\n2. Decrypt text\n3. Exit\n"))
