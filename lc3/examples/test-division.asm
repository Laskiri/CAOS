.ORIG x3000

LD R1, DIVIDEND 
LD R2, DIVISOR

AND R3, R3, X0000
NOT R2, R2
ADD R2,R2, X0001

division ADD R1, R1,R2
BRN ST_quotient 
ADD R3,R3, X0001
BRNZP division 


ST_quotient ST R3, QUOTIENT ;STORE QUOTIENT

 
HALT

DIVIDEND .FILL X0014 
DIVISOR  .FILL X0003
QUOTIENT .FILL X0011 
.END
