#include <stdio.h>
#include <ctype.h>

int main() {
    char text[500], ch;
    int key, a;
    
    printf("NOTE: (Enter message in capital letters and without spaces)\n");
    printf("Enter a message to encrypt: ");
    scanf("%s", text);
    
    printf("Enter the key: ");
    scanf("%d", &key);
    
    for (int i = 0; text[i] != '\0'; ++i) {
        ch = text[i];
        if (isupper(ch)) {
            ch = (ch - 'A' + key) % 26 + 'A';
        } else {
            printf("Invalid Message\n");
            return 1;
        }
        text[i] = ch;
    }
    
    printf("Encrypted message: %s\n", text);
    
    for (int i = 0; text[i] != '\0'; ++i) {
        ch = text[i];
        if (isupper(ch)) {
            a = (ch - 'A' - key);
            if (a < 0) {
                ch = (ch - 'A' - key + 26) % 26 + 'A';
            } else {
                ch = (ch - 'A' - key) % 26 + 'A';
            }
        } else {
            printf("Invalid Message\n");
            return 1;
        }
        text[i] = ch;
    }
    
    printf("Decrypted message: %s\n", text);
    return 0;
}
