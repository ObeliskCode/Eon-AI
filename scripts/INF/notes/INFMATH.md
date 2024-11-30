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
be 000 11 222 333 4 55 66 77 8

where 8 is the number of subtracted items from <+>17>

then we have that for example

<+10> - {+>10, ... , 4(+>10)} = <11> - {11, ... , 4(11)}

where we must subtract the first 4 elements of <+>10>