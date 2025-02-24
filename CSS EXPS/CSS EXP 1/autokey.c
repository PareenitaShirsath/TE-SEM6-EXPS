#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Function to encrypt plain text using the Autokey Cipher
void encrypt(char *plain_text, char *key, char *cipher_text) {
    int plain_len = strlen(plain_text);
    int key_len = strlen(key);
    
    for (int i = 0; i < plain_len; i++) {
        key[key_len + i] = plain_text[i];
    }
    key[key_len + plain_len] = '\0';

    for (int i = 0; i < plain_len; i++) {
        if (isalpha(plain_text[i])) {
            char plain_char = toupper(plain_text[i]);
            char key_char = toupper(key[i]);
            cipher_text[i] = ((plain_char - 'A') + (key_char - 'A')) % 26 + 'A';
        } else {
            cipher_text[i] = plain_text[i];
        }
    }
    cipher_text[plain_len] = '\0';
}

// Function to decrypt cipher text using the Autokey Cipher
void decrypt(char *cipher_text, char *key, char *decrypted_text) {
    int cipher_len = strlen(cipher_text);
    char extended_key[100];
    strcpy(extended_key, key);
    
    for (int i = 0; i < cipher_len; i++) {
        if (isalpha(cipher_text[i])) {
            char cipher_char = toupper(cipher_text[i]);
            char key_char = toupper(extended_key[i]);
            decrypted_text[i] = ((cipher_char - 'A') - (key_char - 'A') + 26) % 26 + 'A';
            
            int new_key_len = strlen(extended_key);
            extended_key[new_key_len] = decrypted_text[i];
            extended_key[new_key_len + 1] = '\0';
        } else {
            decrypted_text[i] = cipher_text[i];
        }
    }
    decrypted_text[cipher_len] = '\0';
}

int main() {
    char plain_text[100], key[100], cipher_text[100], decrypted_text[100];
    
    printf("Enter the plain text: ");
    fgets(plain_text, sizeof(plain_text), stdin);
    plain_text[strcspn(plain_text, "\n")] = '\0';
    
    printf("Enter the key (only alphabetic characters): ");
    fgets(key, sizeof(key), stdin);
    key[strcspn(key, "\n")] = '\0';
    
    encrypt(plain_text, key, cipher_text);
    printf("Encrypted text: %s\n", cipher_text);
    
    decrypt(cipher_text, key, decrypted_text);
    printf("Decrypted text: %s\n", decrypted_text);
    
    return 0;
}
