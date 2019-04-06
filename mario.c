#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int rows;
    do
    {
        rows = get_int("Height: ");
    }
    while (rows < 1 || rows > 8);  
    
    for (int columns = 1; columns <= rows; columns++)
    {
        for (int spaces = rows - 1; spaces >= columns; spaces--)
        {
            printf(" ");
        }
        for (int hash = 1; hash <= columns; hash++)
        {
            printf("#");
        }
        printf("\n");
    }
}
