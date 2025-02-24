#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define SHIFT 3 // Fixed shift value for the keyless cipher

// Function to encrypt plain text using a fixed shift
void encrypt(char *plain_text, char *cipher_text) {
    int i = 0;
    while (plain_text[i] != '\0') {
        if (isalpha(plain_text[i])) {
            char base = isupper(plain_text[i]) ? 'A' : 'a';
            cipher_text[i] = ((plain_text[i] - base + SHIFT) % 26) + base;
        } else {
            cipher_text[i] = plain_text[i];
        }
        i++;
    }
    cipher_text[i] = '\0';
}

// Function to decrypt cipher text using a fixed shift
void decrypt(char *cipher_text, char *decrypted_text) {
    int i = 0;
    while (cipher_text[i] != '\0') {
        if (isalpha(cipher_text[i])) {
            char base = isupper(cipher_text[i]) ? 'A' : 'a';
            decrypted_text[i] = ((cipher_text[i] - base - SHIFT + 26) % 26) + base;
        } else {
            decrypted_text[i] = cipher_text[i];
        }
        i++;
    }
    decrypted_text[i] = '\0';
}

int main() {
    char plain_text[100], cipher_text[100], decrypted_text[100];
    
    printf("Enter the plain text: ");
    fgets(plain_text, sizeof(plain_text), stdin);
    plain_text[strcspn(plain_text, "\n")] = '\0';
    
    encrypt(plain_text, cipher_text);
    printf("Encrypted text: %s\n", cipher_text);
    
    decrypt(cipher_text, decrypted_text);
    printf("Decrypted text: %s\n", decrypted_text);
    
    return 0;
}
