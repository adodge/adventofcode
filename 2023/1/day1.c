#include <stdio.h>
#include <unistd.h>

int main(void){
    char buffer[1024];
    char prev = '\n';
    int acc = 0;
    int n;
    while(n = read(STDIN_FILENO, buffer, sizeof(buffer))){
        char * end = &buffer[n];
        for(char * c = buffer ; c < end; c ++){
            if(*c == '\n'){
                acc += (prev-'0');
                prev = '\n';
            }else if(*c >= '0' && *c <= '9'){
                if(prev == '\n'){
                    acc += 10*(*c-'0');
                }
                prev = *c;
            }
        }
    }
    if(prev != '\n')
        acc += prev-'0';

    printf("%d\n", acc);
}
