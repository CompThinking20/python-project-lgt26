OVERVIEW
The proposed project is a video game where two players choose a 'faction' 
and build buildings that spawn units which automatically march towards the 
enemy base while fighting any enemy units on the way.
The bit was made for this assignment was a demonstration of the rock, paper, 
scissor combat mechanic coded in Python in a text-based format. Each faction 
had units that would be good against specific enemy units and vice versa. 


NARRATIVE
To start this project, I first wrote out the different classes needed to build 
a hierarchy (Player to Faction to Unit). Then I wrote initialization functions 
for each specific faction that I wanted. I made this process into seperate 
functions to allow for future customization. Then the main function was written 
to handle user input and the steps of the game. In addition, the main function 
handled the random choices being made by the computer player, health calculation, 
and game over condition checking. Finally, printing out the 'board' was put into 
a seperate function as well as the combat calculator. The combat function is a 
carries out a small rock, paper, scissors game between the two units currently 
fighting. 

For the second milestone, a call to the main function was added so that the game 
actually ran, and small changes to the text output were made. If I were to reapproach 
this project, I would put more of the contents of the main function into seperate 
functions to clear up the clutter. As well as define terms to allow simple customization 
of certain game settings (i.e. player health, number of units fighting at once, etc).


CORRECTIONS
Making corrections from milestone 1 were simple since it was mostly just a forgotten 
call function line at the very end of the code. As for the corrections from milestone 2, 
I added an if statement that checks to see if the user input is one of the valid numbers 
being asked for (this happens twice within the main function. If they enter a number 
that's higher or lower than requested, or if a string is entered, the program outputs an 
error message and asks for input again.