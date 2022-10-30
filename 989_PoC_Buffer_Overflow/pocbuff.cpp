#include <bits/stdc++.h>

void overflow(char *character){
    char buffer[8];
    strcpy(buffer, character);
}

int main(int argc, char *argv[]){
    if (argc > 1){
        overflow(argv[1]);
    }

    printf("entrada menor a 8\n");
}