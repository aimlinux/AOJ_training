#include <stdio.h>

int main() {
    double r;
    // メモにある精度の高い円周率を使用
    double pi = 3.14159265358979323846;

    // 実数の入力は %lf
    if (scanf("%lf", &r) != 1) return 0;

    double area = pi * r * r;           // 面積: πr^2
    double circumference = 2.0 * pi * r; // 円周: 2πr

    // 出力は小数点以下を多めに（例えば6桁）指定して誤差を防ぐ
    printf("%.6f %.6f\n", area, circumference);

    return 0;
}