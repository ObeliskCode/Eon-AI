## Informal Number Group

+>x = {+/- x, +/- (x-1), +/- (x+1), 0}

+>x + +>y = +>x - +>y = +y - +>x (1.)

1. both informal addition and informal subtraction are commutative

+>x + +>y = {all numbers in both +>x added together} = N

2. the set N can return either 5,7,...,19,21,...,31,33 numbers

3. there are 15 different cardinalities for the set of adding two informal numbers
   together

## Informal Number Basics

x uses only whole numbers 0,1,2,...,n to inf when, +>x is an informal number

+> x is equal to {-x-1,-x,-x+1,0,x-1,x,x+1}

+> x + >y = {all num in +>x added together with all num in +>y}

a set only contains unique numbers!

+> x + >y = {[{all num in +>x}] + [{all num in +>y}]}

+>x + +>y = +>x - +>y = +>y - +>x
+> commutative subtraction

## Informal Addition and Multiplication

Solve. +>1 \* +>2

to solve find all unique numbers in [-2,-1,0,1,2] \* [-3,-2,-1,0,1,2,3]

=> {-6,-4,-3,-2,-1,0,1,2,3,4,6}
note: only the upper triangle of the matrix needs to be calculated

Assume for sake of contradiction division were not possible in the informal number
set

to be considered an informal number it'd require for the addition after a division
to be,

contained within the set O of informal numbers

so, +>1 + +>1 = 2+>1 NOTEQ +>2

thus, in order to compute 2+>x it'd require H(+>x + +>x) where H relates informal numbers to the integers

the calculation of the set +>x + +>x is trivial and linear but what computational requirements does H take?

+>2 + +>2 = {-6,...,6} = +>1 + +>3
+>4 + +>4 = {-10,...,10} = +>3 + +>5 = +>2 + +>6 NOTEQ +>1 + +>7
+>40 + +>40 = [-82, -81, -80, -79, -78, -41, -40, -39, -2, -1, 0, 1, 2, 39, 40, 41, 78, 79, 80, 81, 82]
+>39 + +>41 = [-82, -81, -80, -79, -78, -42, -41, -40, -39, -38, -4, -3, -2, -1, 0, 1, 2, 3, 4, 38, 39, 40, 41, 42, 78, 79, 80, 81, 82]
+>38 + +>42 = [-82, -81, -80, -79, -78, -43, -42, -41, -39, -38, -37, -6, -5, -4, -3, -2, 0, 2, 3, 4, 5, 6, 37, 38, 39, 41, 42, 43, 78, 79, 80, 81, 82]
so +>40 + +>40 NOTEQ +>39 + +>41 NOTEQ +>38 + +>42
+>4 + +>4 = +>1 + +>2 + +>4 = +>4 + +>2 + +>1 = +>2 + +>1 + +>2 + +>1
+>8 + +>8 = [-18, -17, -16, -15, -14, -9, -8, -7, -2, -1, 0, 1, 2, 7, 8, 9, 14, 15, 16, 17, 18]
4(+>4) = 4(+>2) + 4(+>1)
so , x(+>4) = x(+>2) + x(+>1)
we have, 2x(+>4) = x(+>2) + x(+>6)
+>5 + +>5 = [-12, -11, -10, -9, -8, -6, -5, -4, -2, -1, 0, 1, 2, 4, 5, 6, 8, 9, 10, 11, 12]
... + +>5 = [-18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
+>2 + +>2 = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]
... + +>2 = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
... + +>1 = [-11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
... + +>1 = [-13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
... + +>1 = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
... + +>2 = [-18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
so, 3(+>5) = 4(+>2) + 3(+>1) = 3(+>4) + +>2

3x(+>5) = 3x(+>4) + x(+>2) CORRECT (1.)

+>0 = [->1,+>1]
+>1 = [->2,+>2] =+>0 + +>0
+>2 = [->3,+>3] = +>1 + +>0
+>3 = [->4,+>4] = +>1 + +>1
[->5,+>5] = 2(+>1) + +>0
[->5,+>5] = +>2 + +>1
[->6,+>6] = +>3 + +>1
[->7,+>7] = +>2 + +>3
[->8,+>8] = +>3 + +>3
[->9,+>9] = +>4 + +>3
[->10,+>10] = +>5 + +>3

[->11,+>11] = +>4 + +>3 + +>1
[->12,+>12] = +>5 + +>3 + +>1
[->13,+>13] = +>4 + 2(+>3)
[->14,+>14] = +>5 + 2(+>3)
[->15,+>15] = +>4 + 2(+>3) + +>1
[->16,+>16] = +>5 + 2(+>3) + +>1
[->17,+>17] = +>4 + 3(+>3)
[->18,+>18] = +>5 + 3(+>3)
[->19,+>19] = +>4 + 3(+>3) + +>1
[->20,+>20] = +>5 + 3(+>3) + +>1
[->21,+>21] = +>5 + +>4 + 2(+>3) + +>1

[->22,+>22] = 4(+>4) + (+>1)
[->24,+>24] = 4(+>4) + 2(+>1)
[->26,+>26] = 4(+>4) + 3(+>1)
[->28,+>28] = 4(+>4) + 4(+>1)
[->30,+>30] = 4(+>4) + 5(+>1)
[->32,+>32] = 4(+>4) + 6(+>1)
[->34,+>34] = 4(+>4) + 7(+>1)
[->36,+>36] = 4(+>4) + 8(+>1)
[->38,+>38] = 4(+>4) + 9(+>1)

[->28,+>28] = 4(+>5) + +>3
[->30,+>30] = 5(+>5)
[->36,+>36] = 6(+>5)
[->42,+>42] = 7(+>5)
[->48,+>48] = 8(+>5)
[->54,+>54] = 9(+>5)

H([->102,+>102]) = H(9(+>9) + +>7 + +>3) = 102

## Informal Analysis

Noel's Inequality:
if x >= 1 and y >= 2
(+>x)^y will never return a continuous set of integers

an important deduction to be made first is,
if we have two 1-D informal M and N matrices then
does H(M) + H(N) = H(M+N)

does the decomposition of integers addition relate to,
O(1) integer addition with O(1) matrix addition

1. H(+>1 + +>2) + H(+>1 + +>2) = H(2+>1 + 2+>2)
2. H(+>1 + +>2) = 5
3. H(2+>1 + 2+>2) = 10
4. H(+>1 + +>2) + H(+>1 + +>2) = 5 + 5 = 10


let a 1x2 matrix U be a linear combination up to +>1
each slot will be reperesented by a 2-bit int 0,1,2,3
=> numerics [0,9] are supported by 4 bits allocated by U
4 bits allocated using binary addition allows numerics [0,15]


result: 
iff H(+>x + +>x) != NIL then, 
H(+>x + +>x) = (x+1) + (x+1), since
+>x + +>y = +>y + +>x

so,
H(+>10 + +>15 + +>8) = 36
but,
H(+>10 + +>15) = NIL

so for every whole number x 
there is a finite amount of "special" ways
to add up to the whole number x

my theory is that this is how to "quantify" addition

any whole number integer is re presentable by a finite amount of arrays of informal numbers which allows for matrix addition to represent integer addition, every time a register adds up amounts of +>(x) in 64 bits it allows for a computation of H(f(x)) to calculate an infinite number with decentralized computation that means a decentralized computation could add up an indefinite number

3SAT methodology:

so, +- 1 = 1 or -1 to be exact,
then +- 1 or 0 = +> 0
then, +> 0 + +> 0 = +> 1
and, +> 1 = -2 or -1 or 0 or 1 or 2
then, +>1 = +- 1 or +- 2 or 0
why is (+- 1 or 0) + (+-1 or 0) possibly
a function reducible to 3SAT?

so, (+- 1 or 0) + (+-1 or 0)
then, (+- 1 or 0) and (+-1 or 0)

so,
+>10 + +>15 + +>8 = 
(+-9 or +-10 or +-11 or 0) and
(+-14 or +-15 or +-16 or 0) and
(+-7 or +-8 or +-9 or 0)

there is an equation for satisfiability here!

so a chain of numbers with and operations
could lead to a reduction trivially

so, is (10 and 15 and 8) a special list?
the answer is yes or no.
computational hardness proof required.

let's say we reimagine inf number so that

"""
def infn_set_pow2(x):
    return set([-x-2,-x - 1, -x, -x + 1,-x+2, 0, x-2,x - 1, x, x + 1,x+2])
"""

then we have 'infn_set_pow2(0)' = 2
so then that means since we know,
H(10 and 15 and 8) is 36
then
let H^2 be the 3SAT halting machine for 'infn_set_pow2'
H^2(10 and 15 and 8) is 39?
but we know that iff H(f(x)) is valid,
then H^2(f(x)) is valid 

Informal Abstract Algebra:

the informal number set is not equivalent to the integers.

if we imagine group relations then we have a function for
generating subsets of the entire set denoted <a> to be 
a generated set where a is an element of X (informal numbers).

Calculate: <+>0>

we have that <+>0> = {1(+>0),2(+>0),3(+>0)...}

which has an equivalence relation to <1>

so can we assume <+>x> =: <x+1>, where =: means equiv. rel. ?

since <+>1> =: <2> and <+>2> =: <3> ?

no, a trivial counter-example is 

2(+>100) = [0, 1, 2, 99, 100, 101, 198, 199, 200, 201, 202]

lets examine <+>3>.

<+>3> - {+>3} =: <4> - {4}

so if we had a pattern starting at +>0,
then the number of elements subtracted for
a homomorphism to whole numbers then it'd
be 000 11 22 333 4 55 66 77 8

where 8 is the number of subtracted items from <+>17>

then we have that for example

<+10> - {+>10, ... , 4(+>10)} = <11> - {11, ... , 4(11)}

where we must subtract the first 4 elements of <+>10>

the pattern expanded up to 30

0-10: 000 11 22 333 4
11-20: 55 66 77 88 99 
21-30: 10 10 11 11 12 12 13 13 14 14

possible corollary:

adding (+>12) + 5(+>13) is valid

because 6(+>12) is valid and 6(+>13) isn't valid,

so if we add together these "pross" numbers (+>x)
and the resultant is an informal number (all sets with negative integer parity)

then, the minimum amount of additions needed to make pross addition valid
would be lowered by the pross number added with the smallest scalar needed
to be valid.
  
if +>x is odd then subtract 1 then halve the integer and thats the scalar
for the first full informal number made with +>x

if +>x is even subtract by two then halve the number.

corollary (subtraction):

subtraction must be analogous to integer subtraction
since,

1. scalars wouldn't work (then +>x - +>x != 0)
2. subtracting invalid sets together would be overly trivial

we have that +>1 = +>2 - +>0

hyp: maybe then +>3 = +>4 - +>0 ?

so,

+>10 + +>15 + +>5 is complete

+>10 + +>15 is incomplete

+>10 + +>15 + +>5 - +>z = +>y

+>10 + +>15 - +>z = +>x

how do we map relations

f: +>y -> +>x

in a purely mathematical way 

we need to map the function f to send complete subtractions
to incomplete ones!

(+>10 + +>15 + +>5) + +>2 = +[]35

since, (+>10 + +>15 + +>5) + +>2 = +[]32 + +>2

so, +[]35 - +>5 = x and

x = (+>10 + +>15 + +>2)

x - +>2 = (+>10 + +>15)

so x = +[]29 since,

+>2 + +>10 + +>15 = +[]29

then, x - +>2 - +>2 = +[]23 ?

such that, +>10 + +>15 - +>2 = +[] 23 ?

The subtraction algorithmn may require a very weird rule!

in order to subtract 

(+>10 + +>15) - +>2 we have to say that we are only
doing this in one direction

that means that the subtraction algorithm means you
have to only subtract every element of one set
with all the elements of the other set.

so if we do this subtraction then requiring a restriction
to the domain then,

(+>10 + +>15) could have had a domain of +[]26

but then, (+>10 + +>15) - +>2 is restricted to the domain of +[]23
so that means that subtraction moves the maximum a number can be
held within the set down to 0!

let o be a new subtraction type operator.

if we have +>10 + +>15 - +>2 = +[]23

then,

+[]23 o +>2 = +>10 + +>15

would o represent the analog of - (subtraction)

corollary: assume for sake of contradiction that if a linear combination 
were valid any number of them being negative is a vailid
set down to 0 

how could a full set become an incomplete set after undoing a subtraction.
o operator would then mean regency operator because it works as an incomplete
addition in relation to incomplete subtraction!

o stands for regency, another subtractive operator

the solution to regency is finding incomplete linear combinations of any
kind that could be completed by adding the operated number to the ilc.

undoing subtraction could mean saving integer space by letting
the maximum of incomplete sets to be used as reserve calculations
previously done. why would taking a single degree of of doing
calculations matter if this operator would then only work on complete 
sets denoted +[]x then.

big question. what would o +>x be by itself?

so theoretically o +[]26 = (+>10 + +>15).

then also, o +>26 = (+>10 + +>15) ?

of course, at least, o +>26 = +>26 ?

so if o +[]inf = +>inf, then why

not inf -1, inf, inf + 1 ?

let o be an operator such that there is no infinity
between spaces in integers that take exactly no space in between one
space after and before a . that would mean that . would insuniate that . means all
inf, inf -1 , and inf + 1

ok so +>0 o +>inf o +>2 + +>1 could equal 1.5 ? in some system.

this would suggest we use some kind of 10-max-char system [0-9]

what about 1-max-char system [0] where

a number could be 000.0000 for 3 and then 4 reserved spaces for characters ?

if 1.1.1 meant something it'd only be because 5.5.5 meants something to it, logically.

so 1.1.5 + 1.1.5 = 2.3.0 in some other math system.

could then +>0 o +>inf o +>0 o +>inf o +>0 = 1.1.1 in some representation?

the sliding math makes more sense in the way that a domain expanding would reserve
a new end to a new start at every pair where a single digit is multiplying
a domain expansions such as 5 x 10^3 = 5000
but the digit 5 at 5431 still also means 5000

you have that the regency operator could be a theoretical multi-plexor for higher
maximums without breaks in continuity then we have that you would then count numbers
in reserve space expansion ?

so, {0} o +>9 o +>3 + +>4 o +>89 o +>4 +>1

could represent 79.

what happens below a dot. but also what happens before regency? then what is o^-1 as
an operator? because anything below a dot would then be modeled by o^-1 here.

lets say that {0} o^-1 +>9 o^-1 +>1 is equiv to .2 

then we could have {0} o^-1 C(0) o^-1 +>x and {0} o C(0) o +>x

and that could give us 1.2 for example

we take inv regency and argue that the operator o^1 is the only analog to create an
algebraic structure that would be able to define division as a pragmatic subtraction.
when dividing it is taking as note that divided numbers are supposed to be more
subtracted arithmetic.

if regency can undo a subtraction which means that regency is incomplete addition then
how could its inverse mean incomplete subtraction. the obvious assumptions is valid.
o^-1 could take only complete sets to incomplete sets witha restricted domain like before.

so, +[]29 o^-1 +>2 = (+>10 + +>15) aswell.

then we could then have +>x / +>y

if we said this was 10/5 ?

we could say this is equiv to {0} o +>9 o +[]9 / {0} o +>9 o +[]4

then we'd have {0} o +>9 o +[]9 o^-1 {0} o +>9 o +[]4

consequently, since,

{0} o^-1 +>9 o^-1 +[]9 already means 1/10.

Multiplication hypothesis: multiplication would require oo^-1 or o^-1o in some way together.