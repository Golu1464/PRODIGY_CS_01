def caesar_cipher(text, shift, mode='encrypt'):
  """
  Encrypts or decrypts text using Caesar Cipher.

  Args:
      text: The text to encrypt or decrypt.
      shift: The number of positions to shift letters.
      mode: 'encrypt' for encryption, 'decrypt' for decryption (default: 'encrypt')

  Returns:
      The encrypted or decrypted text.
  """
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  shifted_alphabet = alphabet[shift:] + alphabet[:shift]
  upper_alphabet = alphabet.upper()
  shifted_upper_alphabet = upper_alphabet[shift:] + upper_alphabet[:shift]

  result = ''
  for char in text:
    if char.isalpha():
      if char.islower():
        index = alphabet.find(char)
        new_char = shifted_alphabet[index]
      else:
        index = upper_alphabet.find(char)
        new_char = shifted_upper_alphabet[index]
      if mode == 'decrypt':
        new_char = shifted_alphabet.find(new_char)
        result += alphabet[new_char] if char.islower() else upper_alphabet[new_char]
      else:
        result += new_char
    else:
      result += char

  return result

# Get user input
message = input("Enter your message: ")
shift = int(input("Enter the shift value (positive for encryption, negative for decryption): "))
mode = input("Enter 'encrypt' or 'decrypt': ").lower()

# Check for valid mode
if mode not in ('encrypt', 'decrypt'):
  print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
  exit()

# Perform encryption or decryption
result = caesar_cipher(message, shift, mode)

print(f"{mode.capitalize()}d message: {result}")