#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    float amount; // Initiate amount as float.
    do // Prompt user to enter positive float value.
    {
        amount = get_float("Change owed: ");
    }
    while (amount <= 0);
    
    // To perform mathematics to calculate total numbor of coins.
    int change1 = 0; 
    int change2 = 0; 
    int change3 = 0;
    int change4 = 0;
    if (amount >= 0.25)
    {
        change1 = amount / 0.25;
        float intermediate1 = change1 * 0.25;
        if (intermediate1 < amount)
        {
            float intermediate2 = amount - intermediate1;
            change2 = intermediate2 / 0.1;
            float intermediate3 = change2 * 0.1;
            float sofar1 = intermediate1 + intermediate3;
            if (sofar1 < amount)
            {
                float intermediate4 = amount - sofar1;
                change3 = intermediate4 / 0.05;
                float intermediate5 = change3 * 0.05;
                float sofar2 = sofar1 + intermediate5;
                if (sofar2 < amount)
                {
                    float intermediate6 = amount - sofar2;
                    change4 = intermediate6 / 0.01;
                    float intermediate7 = change4 * 0.01;
                    float sofar3 = sofar2 + intermediate7;
                }
            }
        }
    }
    int sum = change1 + change2 + change3 + change4;
    printf("%i\n", sum);
}
