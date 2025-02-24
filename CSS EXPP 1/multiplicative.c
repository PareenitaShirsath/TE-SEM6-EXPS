#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Function to encrypt plain text using multiplicative cipher
void encrypt(char *plain_text, int key) {
    char *ptr = plain_text;
    while (*ptr != '\0') {
        if (isalpha(*ptr)) {
            *ptr = toupper(*ptr);
            *ptr = (((*ptr - 'A') * key) % 26) + 'A';
        }
        ptr++;
    }
}

// Function to decrypt cipher text using multiplicative cipher
void decrypt(char *cipher_text, int key) {
    char *ptr = cipher_text;
    int key_inverse;
    for (key_inverse = 1; key_inverse < 26; key_inverse++) {
        if ((key * key_inverse) % 26 == 1) {
            break;
        }
    }

    while (*ptr != '\0') {
        if (isalpha(*ptr)) {
            *ptr = toupper(*ptr);
            *ptr = (((*ptr - 'A') * key_inverse) % 26) + 'A';
        }
        ptr++;
    }
}

int main() {
    char plain_text[100];
    int key;
    
    printf("Enter the plain text: ");
    fgets(plain_text, sizeof(plain_text), stdin);
    plain_text[strcspn(plain_text, "\n")] = '\0';
    
    printf("Enter the key (a number between 1 and 25 that is coprime with 26): ");
    scanf("%d", &key);
    
    char cipher_text[100];
    strcpy(cipher_text, plain_text);

    encrypt(cipher_text, key);
    printf("Encrypted text: %s\n", cipher_text);

    decrypt(cipher_text, key);
    printf("Decrypted text: %s\n", cipher_text);

    return 0;
}
