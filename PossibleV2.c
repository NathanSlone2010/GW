#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//Required libraries

#define MAX_INPUT 5 //Changed number if needed
//Defines the max letter input

int main() {
    char input[MAX_INPUT];

    puts("THE WAR OF COLLAPSE, 02.00.00 Build");
    puts("VOID STUDIOS COPYRIGHT 2026");

    while (1) {  // loop added for choice handling
        puts("You wake up in a forest. You see a house, a mailbox, and a broken window");
        puts("1. Enter the house");
        puts("2. Open the mailbox");
        puts("3. Look through the broken window");

        printf("[INPUT] ");
        fgets(input, sizeof(input), stdin);
        input[strcspn(input, "\n")] = 0;

        if (strcmp(input, "1") == 0) {
            puts("You enter the house, a woman screams, you cannot see her... Pop, you hear a ringing, blood comes out of your ears... Blood and brain matter sprays everywhere, your body falls to the ground 'Delicious... Another toy.....");
            break;  // exit the loop after this choice

        } else if (strcmp(input, "2") == 0) {
            puts("You see a letter, taking it out, you read it.. 'Welcome to the game, Player! This is a linear story-like-lite Text Based Game!");

        } else if (strcmp(input, "3") == 0) {
            puts("You look through the window... Your body falls to the ground...");
            break;

        } else {
            puts("INVALID. SKIPPING THIS CHOICE SET. RESTART PROGRAM TO CHOOSE AN OPTION");
            break;
        }
    }

	while (1) {
		puts("\n\nYou throw down the letter and walk behind the house, seeing three paths. Left, Straight, and Right");
		puts("1. Left path");
		puts("2. Straight path");
		puts("3. Right path");
		printf("[INPUT] ");
		fgets(input, sizeof(input), stdin);
		input[strcspn(input, "\n")] = 0;

		if (strcmp(input, "1") == 0) {
			puts("Walking down the left path, you smell cucumbers, and get hungry... You feel a painful sting on your leg.. A snake... [YOU] Really!? A damn snake?? Fuck-");
			break;

		} else if (strcmp(input, "2") == 0) {
			puts("Walking down the straight path, you feel a blade on your back... 'Give me everything you have!' the man demands.... You refuse...");
			break;

		} else if (strcmp(input "3") == 0) {
			puts("Walking down the right path, you hit the road... Where will you ened up...?");

		} else {
			puts("SKIPPING SINCE YOU DO NOT WANT TO MAKE A CHOICE..!");
		}

    	return 0;
}
