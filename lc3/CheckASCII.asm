.ORIG x3000
    LD R2, SUB_VALUE ; Load the value at SUB_VALUE into R2
    LD R1, ASCII_START
    ADD R3, R1, R2 ; Subtract 128 from the value in R1
    BRn VALID ; If the result is negative, the original value was less than 128 and is a valid ASCII code
    BRzp INVALID ; If the result is zero or positive, the original value was 128 or greater and is not a valid ASCII code
INVALID
    BRnzp END ; If the value is not a valid ASCII code, branch to the end of the program
VALID
    ADD R0, R1, #0
    TRAP x21 ; If the value is a valid ASCII code, output it
END
    HALT
ASCII_START .FILL 68 ; The initial value to check
SUB_VALUE .FILL -128 ; The value to subtract
.END