Due Date: Sunday April 7th, 11:59pm
Submission Method: Upload your .py file to the cyber university.
Cheating Policy: Severe penalties. Do your own work. Do not show your code
                            to your classmates.

Assignment Background Information:
Algebraic notation is a compact way of describing chess moves. (https://en.wikipedia.org/wiki/Algebraic_notation_%28chess%29)
In this notation, the squares on the board are identified by their file and rank (ie,
their column and row). The file is a letter between a and h; the row is a number
between 8 and 1 (ie, decreasing order). Thus, "a8" is the upper-left square on the
board, and "h1" is the bottom right square.

The pieces are named with an upper-case letter. "Q"=Queen, "K"=King,
"N"=kNight, "B"=Bishop, "R"=Rook. Notice that the Knight is represented as
"N", because the king uses the "K". Also notice that there is no letter for pawns.
Instead, they are indicated by not including an upper-case letter.

Moves are indicated by the piece and the target square (ie, the square that you
want to move to). For example:

Qe5  --  Move the Queen to e5.
Kb4  --  Move the King to b4.
Nc7  --  Move one of the kNights to c7.
e4   --  Move one of the pawns to e4.

From the above, notice that there is ambiguity. Which knight will move to c7?
After all, there are two knights. Similarly, which pawn goes to e4? The answer
is that you move the one that can move there. Which means that you have to use
logic to see which one can make the move.

It is also possible (but unlikely) that either knight could move to e4. There
are rules for disambiguating such cases. To quote the wikipedia page:

  "When two (or more) identical pieces can move to the same square, the moving 
  piece is uniquely identified by specifying the piece's letter, followed by 
  (in descending order of preference):
   - the file of departure (if they differ); or
   - the rank of departure (if the files are the same but the ranks differ); or
   - both the file and rank (if neither alone is sufficient to identify the 
     piece--which occurs only in rare cases where one or more pawns have
     promoted, resulting in a player having three or more identical pieces able 
     to reach the same square)."
 
So, for example:
Bdb8  --  Disambiguates that you wish to move the Bishop in file d.
R1a3  --  Disambiguates that you wish to move the Rook in rank 3, given that
          both rooks just so happen to be in the same file.
Qh4e1 --  Disambiguates that you wish to move the Queen at h4, given that two
          are in file h and two queens are in rank 4. Obviously, as stated above,
          this is an extremely rare situation, because you would have to have
          promoted two pawns in order to even get 3 queens on the board.


The notation also requires you to add an "x" before the target if you will capture
a piece. For example:
Nxe4  --  Moves the available knight to e4, and captures the enemy piece at e4.
Ndxe4 --  Moves the knight at file d to e4, and captures the enemy piece at e4. 
N2xe4 --  Moves the knight at rank 2 to e4, and captures the enemy piece at e4,
          but only if both knights are in the same file.
xe4   --  Moves the available pawn to e4, and captures the enemy piece at e4.
          (Remember, pawns capture on a diagonal.)
dxe4  --  Moves the available pawn of file d to e4, and captures the enemy 
          piece at e4. (I say available pawn, because their might be two pawns
          in that file, but only one can legally move to e4.) Note: "dxe4" is
          only legal notation if you have another pawn at f3 (for white) or
          f5 (for black). Otherwise the correct notation would have been "xe4".


There are also special rules of notation for check, checkmate, en passant, pawn
promotion, and castling. We will not implement these additional rules in this 
programming assignment.

-------------------------------------------------------------------------------

The Actual Assignment:
Given the board data generated from the previous homework (ie. the data
structures we used to indicate the positions on the board and the colors of the
pieces),
You will write functions to:
  1. GetAMove():
     - Indicate to the user the color (start with white) and ask for a move.
     - Test if the input is legal, by forward-calling the not-yet-declared function
       named legal(...). If that functionreturns with the value False, ask again.
       To make life intersting, you must splat the inputted string when you pass it
       into legal(...). 
     - Switch the color, for the next time this function is called. Note: the color
       variable must be a mutable default argument that starts out white, but
       which remembers the previous change each time it is called. (See Lecture
       4-5, slides 140-153.) 
     - With the finally obtained legal value, return two separate objects, each 
       being a two-element tuple. 
       The first tuple is a pair of numbers 0-7 that indicates the row and column 
       of the place to move from (numbered as the previous homework did -- ie,
       (0,0) is the upper left). The second column is the square to move to, also 
       a pair of numbers from 0 to 7.

  2. Legal(...):
     - Calls two functions: SyntacticallyLegal(...) & SemanticallyLegal(...).
       If either is False, return False. Else, retun True.
       To keep life intersting, you must forward the input you receive, as-is.

  3. SyntacticallyLegal(...):
     - Returns whether the provided input is in algebraic chess notation (but 
       remember, I won't test castle, en passant, etc.)
       What is legal? Well, for example:
        "Qh4xe1" is legal notation. It is so rarely for there to be 3 queens, but
                 it can happen, so it is syntactically legal (even if you don't
                 have 3 queens).
       "Kfe1" is also syntactically legal. With only one king, dissambiguating
              that you are refering to king at rank "f" is semantically wrong.
              But it is sytactically legal.
       "hxe1" is also syntactically legal. Even though a pawn in file "h" cannot
              move to file "e", it is sytactically legal.
       "hxe9" is illegal, because there is now rank of 9.
       "HXE9" is illegal, because this notation is case sensitive.  

  4. SemanticallyLegal(...): 
     - Returns the current location of the piece to be moved, as a tuple of two
       numbers, if the move indicated is valid, given the current positions on 
       the board. Otherwise, it returns False. 
       Semantic legality refers to whether the move makes sense. For example: 
       - You cannot move to where a piece of the other color is, if you don't
         say "x". And you cannot say "x" unless you do capture a piece.
       - You cannot move into a square already containing one of your own pieces.
       - You cannot make a move where no piece of the indicated type is able to
         move there.
         Hint: look backwards to see what could move here. So if you give Nd4,
               then look at where a knight at d4 could go to; these will be the
               places where a knight can be and be able to move to d4. In other
               words, look in {e6, f5, f3, e2, c2, b3, b5, c6}.
       - You cannot do dissambiguation if there is only one such piece. 
       - You must do dissambiguation if there is more than one such piece.
       - If you do dissambiguation, it must be logical. You cannot indicate, for
         a knight in file "d", if there is no knight in that file (or at least,
         no such knight that can reach the target square). 
       - But you DO NOT HAVE TO CHECK for the right type of dissambiguation,
         in this assignment. You do not have to check that a rank can only be
         given if the file is ambiguous. Or that a rank and file can only be given
         if both are ambiguous.
       - You also do not concern yourself with king checks. In reality, a piece
         cannot be moved if it causes the king to be in check. This would also
         affect whether there is ambiguity. For example, maybe both knights can
         move to e6, but one of them is currently blocking a bishop that would
         otherwise have the king in check. So, technically, there's no ambiguity
         and you would just say "Ne6". This issue is NOT part of this assignment.

  5. PlayGame(): 
     This loops forever, performing three steps:
     -  Call the code from the last homework, to display the board.
     -  Call GetAMove(). 
     -  Update the board based on what GetAMove returns. Note: GetAMove will
        always return a legal move.

     Note that looping forever means that the game never ends. In reality, games
     do end with a checkmate or a draw. But we do not test for that, so our game
     never ends.
