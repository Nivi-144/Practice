#include <stdio.h>
#include <string.h>
#include <math.h>
#include <unistd.h> // for usleep on linux/mac. Use windows.h + Sleep on windows

int main() {
    float A = 0, B = 0;
    float i, j;
    int k;
    float z[1760]; // depth buffer
    char b[1760]; // screen buffer
    printf("\x1b[2J"); // clear screen

    while(1) {
        memset(b, 32, 1760); // fill with spaces
        memset(z, 0, 7040); // fill with 0
        for(j = 0; j < 6.28; j += 0.07) { // j = theta
            for(i = 0; i < 6.28; i += 0.02) { // i = phi
                float c = sin(i);
                float d = cos(j);
                float e = sin(A);
                float f = sin(j);
                float g = cos(A);
                float h = d + 2;
                float D = 1 / (c
