# Notakto-AI-Python

# Q4: Notakto - AI
Weight: 20%

Last update: 18 Oct, 7am

In this question, you are going to implement an artificial intelligence (AI) vs. human version of Notakto. The AI will be the Player 1, i.e., the AI will always start. Here the AI means that the move of player 1 is determined by your program automatically. You should finish the previous question first before working on this one. All output / input requirements are identical to the previous question. The only difference is that you replace Player 1 with an AI, i.e., don't wait for user input and let your program decide the valid move. 

In Notakto, Player 1 can force a win. It doesn't matter how Player 2 plays. If Player 1 plays optimally there should be a win for Player 1. In this task your AI must always win. Here is an example run (bold font represents user input). 

```
A      B      C
0 1 2  0 1 2  0 1 2
3 4 5  3 4 5  3 4 5
6 7 8  6 7 8  6 7 8
Player 1: B0
A      B      C
0 1 2  X 1 2  0 1 2
3 4 5  3 4 5  3 4 5
6 7 8  6 7 8  6 7 8
Player 2: B3
A      B      C
0 1 2  X 1 2  0 1 2
3 4 5  X 4 5  3 4 5
6 7 8  6 7 8  6 7 8
Player 1: B6
A      C
0 1 2  0 1 2
3 4 5  3 4 5
6 7 8  6 7 8
Player 2: C0
A      C
0 1 2  X 1 2
3 4 5  3 4 5
6 7 8  6 7 8
Player 1: C3
A      C
0 1 2  X 1 2
3 4 5  X 4 5
6 7 8  6 7 8
Player 2: C6
A
0 1 2
3 4 5
6 7 8
Player 1: A0
A
X 1 2
3 4 5
6 7 8
Player 2: A4
A
X 1 2
3 X 5
6 7 8
Player 1: A7
A
X 1 2
3 X 5
6 X 8
Player 2: A8
Player 1 wins game

```

There will be no student site automatic marking for this question. Please perform your own testing and ensure that you never win against your AI. We suggest that you finish the previous question first and then copy over your code from there and only change the part where player 1 (your AI implementation) is moving. 

We will mark your code by playing a number of games against an optimal AI. Your AI must win all games to get full marks for this question. 

Important: Implementing an optimal AI that is able to always win does not require complex computation. Your AI must be very fast. We will use a time threshold of 1 second per move. 
