#include <stdio.h>
int main() {
    float P_yes = 0.6;
    float P_no = 0.4;
    float P_sunny_yes = 0.2;
    float P_sunny_no = 0.6;
    float score_yes = P_yes * P_sunny_yes;
    float score_no = P_no * P_sunny_no;
    if (score_yes > score_no)
        printf("Play Tennis: Yes\n");
    else
        printf("Play Tennis: No\n");
    return 0;
}
