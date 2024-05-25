def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char.lower()) - ord('a') + shift) % 26 + shift_amount)
            result.append(encrypted_char)
        else:
            result.append(char)
    return ''.join(result)

def encrypt_file(input_file_path, output_file_path, shift):
    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        encrypted_text = caesar_cipher(text, shift)

        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(encrypted_text)

        print(f"File '{input_file_path}' has been encrypted and saved as '{output_file_path}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
input_file = 'BHW\Origin.txt'  # Replace with your input file path
output_file = 'BHW\Encode.txt'  # Replace with your output file path
shift_value = 3  # Replace with your desired shift value

encrypt_file(input_file, output_file, shift_value)
