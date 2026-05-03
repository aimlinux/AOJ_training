//カワニシ君作成

#include <stdio.h>
int main(void) {
    int a, b, n;
    scanf("%d %c %d", &a, &n, &b);
    while (1){
        if(n == '+') {
            printf("%d %c %d\n", a + b);
        }
        else if(n == '-') {
            printf("%d %c %d\n", a - b);
        } 
        else if(n == '*') {
            printf("%d %c %d\n", a * b);
        }
        else if(n == '/') {
            printf("%d %c %d\n", a / b);
        }  
        else if(n == '?') {
            break;
        }
    }

}