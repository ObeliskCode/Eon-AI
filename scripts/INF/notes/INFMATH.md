## Reduction Proof

= | stands for Reduction.
| = | stands for Irreducible Reduction

## Long Handed Subtraction example

100 - 50 |=| x |=| 0 =| x + 50 =| 100 |=| x - 50 =| 50

## Reductive Algebra Group

1. x |=| x

2. x |=| 0

3. 1/0 |=| 0

note 5-5 = 0 = 4+5+6-4-5-6 = 0

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

solve.
the simplest assumption is that +>x \* +>y = +>x / +>y = +>y / +>X
which is that division is commutative and exactly the same as multiplication

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

(1.)
1-D matrix/2-D matrix calculations could in theory,
be faster than binary integer calculations past a very large number

[CHALLENGE] calculate 4 bil. in less than 32 bits
Hypothesis: inf. mult. isn't more space effic. 
than regular binary addition to infinity?

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

H([[2,3],[3,2]](+\*)) = 576

lets examine[[2,3],[3,2]](+\*)

## Informal Set Subtraction and Simplification

if an nxn(+\*) matrix be allocated a numeric in another matrix,
then an nxn(nxn(+\*)) matrrix would still aloow for ordinary matrix operations
on top of the existing thinner matrix which fits perfectly as subset speed for
found numerics which minimize the computational bound of H to O(1)

ergo, this could lead to faster matrix multiplication algorithms
for most non-trivial computations

so informal number theory suggest matrices contain matrices within matrices

informal subtraction (trivial):

+>4 - +>2 = {-5,5} - {-3,3} = {-5,-4,0,4,5}

obviously using integer subtraction within informal calc. is commutative
same thing for division and subtraction, but informal subtraction
is not integer subtraction! (set closure)

thus,

+>0 - +>0 = {0}

Simplication(Informal Division) Proofs

Q: we said that +>4 meant a solution which means choice for elements in the set

we can quantify it into one number then do some operation probably just
multiplication again to the whole set as one operation to the whole set...

this means division is about multiplication by selection sorting H or maybe h
another conjector function similar to H in the same field of conjector funcs?

so, is it the func H or h which relates Simplification?

u suggest that h is the new function which relates higher dim informal matrices
to lower informal matrix spaces but not to integers!

so if simplification (/) were a real operation in informal numbers regardless
it'd have to send itself as a function from ->n +>x= -> ->1 +>x (n dim to 1 dim)

the example matrix multiplication is the first order of informal (simplification)

INFORMAL MATRIX SIMPLIFICATION ALGORITHM IN 1D:
------------[b1,b2,b3,b4,b5]
[a1, a2, a3, a4]------------

1D informal matrix simpl requires stacking matrices like this.

also, note:

1. x/0 |=| y |=| 0 |=| 0/x =| y |=| x*0 =| 0 ?

2. there are three simpl functions, (/-), (/+), (/\*)

calculating (/+) is the easiest one to calc

there are 6 2d axes to manage in this system in total

(-,/), (+,/), (_,/), (_,+), (-,+), (-,\*)

4-D -> 6-D extension:

+, -, \*, / are all formally defined operations in the informal number system

[+ := set add.,- := set subt.,* := set mult.,/ := simpl.]

so, (-,/), (+,/), (_,/), (_,+), (-,+), (-,_)
= (+,-,_),(+,-,/),(+,_,/),(-,_,/) => 4-D

so for 6-D we have

[1]:[(+,-,*),(+,-,/)]
[2]:[(+,-,*),(+,*,/)]
[3]:[(+,-,*),(-,*,/)]
[4]:[(+,-,/),(+,*,/)]
[5]:[(+,-,/),(-,*,/)]
[6]:[(+,*,/),(-,*,/)]

where for example we have the operator h then,

(+,-,\*) h (+,-,/) |=| (x,y,z) ?

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

an N-D Informal Matrix is one that grows combinatorically massively
as it gets bigger and one that will always support O(1) matrix addition.

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

Noel's 3SAT methodology:

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

conjector limit hypothesis:
H^inf(+>x + +>y) = (x+1) + (y+1) + 2(inf)
then, H^C(+>x + +>y) = (x+1) + (y+1) + 2(C)

so, assume conjector lim hyp is valid
idea: 
S(x)dx = (x^2/2) + C
why not,
S(x)dx = (x^2/2) + H(C)?

simple proof, perturbing a function to infinity
could mean that C could be infinity or
rather be an element of any number system

does this mean then that possibly,

T(C) is a function that sends to an inf num,

S(x)dx = (x^2/2) + H^inf(T(C)) ?
so,
S(x)dx = (x^2/2) + C + |T(C)|(inf) ?

R = |T(C)|(inf) = w(inf)
then,
S{x}dx^2 = S{ (x^2/2) + C + w(inf) }dx
= S{ (x^2/2) + C }dx + xw(inf)

integral hypothesis:
suppose every time you integrate you get a 
multiplicative infinity that expands the scope
of infinity for every calculation done up to
a limit to infinity

assume C is an irrational number such as pi,
infinitely many digits, then,

|T(C)| consequently should equal inf
so, |T(C)| = inf  iff  C is irrational

thus,
in that case

S(x)dx = (x^2/2) + C + (inf)^2

so, every amount of digit needed to represent
C amounts to a function with a lim to inf

lets say C = pi then, 
S(x)dx = (x^2/2) + pi + (inf)^2

this theory suggests, H^inf(T(pi)) = x + inf^2
where x is a real number what is T?

observation:
1. |(+>(x+1) * +>(x+1))| |=| |(+>x / +>x)

since,
1. +>2 * +>2 = {-9,-6,-4,-3,-2,-1,0,1,2,3,4,6,9}
2. +>1 / +>1 = {-2,-1,0,1,2, 0/-2, 0/-1 , 0/1 , 0/2 , -2/0 , -1/0 , 1/0, 2/0}

both sets have a cardinality of 13 so could
for ex, 1/0 be two values

the result R = |T(C)|(inf) or min|T(C)|(inf)
seems to make little sense except if array x is an el. of X (INF numbers)
is an infinite array in linear algebra because H^inf seems like something
that could be used somewhere completely specific and that to my opinion is
in fact having a number system which has a definite number after 1.
because 0 = {0} is the zero el. and +>0 =  {-1,0,1} is the unit element
correction: +>0 =  {-1,0,1} is not the unit element it is the first element
H(+>0) may send to 1


Corollary:
H^inf(+>x + +>y) = (x+1) + (y+1) + 2(inf)
then, H^C(+>x + +>y) = (x+1) + (y+1) + 2(C)

if H^inf(+>x + ...) then (x0+1) + ... + n(inf)
then it is possible that then we have,

for ex (x0+1) + ... = 12
then,
12 + n(inf) = 6*2 + n(inf)
so is it possible that we can enemurate amount of factors
for 12 this way some how then ?

# Completely Unproven Theory

theory,

mystery of how symbols labeled x/0 could have parity with inf. mult. |=|?

d/ix(x) = i + d/dx(x)/S(x)dx

(x+1)(y+1)/0 = d/ix S(multiply[1,k->inf]d^k/ix(x) * d^k/ix(y))

where d/ix S = i + S(x)dx/d/dx(x)

so (x+1)/0 = ?

it is possible this function could be telegraphic?, divergent and converges at the same time?

could that be because i could possibly only ever have a field of integers if we can modify d/ix ?

a complex function would be interesting if its imaginary field were restricted to integers
because this alone could be outpaced by the monotic function at every step k for some k->inf somewhere?

imagine saying a function is always getting negated so it is now it's negative counterpart.
could a function then say it could always be positive after being negated in a sequence?

that function would have to always grow larger with every step K. thats means will have always atleast
been able to double itself every step K which means the function creates atleast 
2x amount of itself of itself every step K.

imagine always being multiplied by larger and larger negative numbers continuously then always being negated
bt larger and larger negative numbers means if a function save itself from monotonically diverging towards
the negative numbers always then you can only have a function monotonically diverge positively then,
this should measure how much a function displaces amounts "of itself of itself" it is the fact that
i when i^2 = -1 could be expaned to i where i^3 = -1 and this would already mean that when i^2 = -1
it takes depositing i twice for i to be able to create a negative "telegraph",
this means that if you draw a function continously upwards like in signal graphs then the integral
between when the function wasn't negative is the area of the signal square wave of the function.

this means the functions in between negatives are always concave which means quickly all there is
a number before a line almost up and then spaces where there are discontinuities

but those discontinuaties also make a function which were ridiculously concave too if we graphed
its negation, somewhere in the middle is two values for a complex number exactly meaning that
complex number meaning if 1 was a complex value you could find two values for 1 that aren't
the same as -1 that means that the graph of y = x could defy the rules of cartesian planes
a graph of f(x) = x could mean x = f(x) then x = f(x) could be a circle.

if there is a circle where it means (1)x then there could be another circle that represents
2(x) but that circle would have to start at 2(x) and end at 3 or so because
the cartesian plane being graphed means 1 passing on x actually means one function passes by

so if a cartesian plane can only be graphed by counting in integers than it can be used to
count functions instead of variables.

q: how do you use regular math make a sequence which always goes from 0 to i to i^2
in that order to infinity?

the shape of spinors and how i suggest you can plot either (x,y) or (f(x),(x,y))
means to me that spinors are counted in i where i requires more degrees to turn i into -1
so that the folds of spinors mirrors the amount of functions that cannot overlap or
rather an amount of folds. imagine the unit circle centered at (1/2,1/2) then it would
start at 0 and end at one then think there is a unit circle centered at every integer away
from every 1/2 then that would make the whole graph be representable by two functions

hypothesis: then the point is to say eventually that then this system takes the integer before a dot
in the real number for ex. 1.22405215 would then be between 1 and 2 so 1.22 could mean x = 22 for a 
function bounded from [1,2] exactly! this concludes with the suggestion 1.22.44 could mean
that from [1,2] that we plot (f1(22.44),f2(22.44)) suggesting a three dot real number system.

the riemann hypotnuse is the part of the riemann sum that isn't included in calculus
because there are infinitely many squares in linear algebra.

experimental theory: an informal array could take H(+>x) to an integer
but an informal matrix could take H(+>x) to a real number possibly.

this way you can say other bases of dims in these matrices are expansions
of of the space between integers. meaning that every base change in 
a 2d matrix in this system takes the number calculated

to a real number or infinite expansions of spaces between real numbers

would this then be a real number or another construct to infxinf dims

proof.
the point of this number format is to originally
"destroy the unity of number set uniquness of integers"

the original puzzle for informal numbers is:
an infinite list of sanscript characters that never ever repeats
the same character twice in the entire list

a real number could then be if we took H to all rows

let +>x(n) be row n of matrix +>x

H(+>x(0)) + O(+>x(1)) + ..

could mean 1547 + O(71281) + O'2(12515) + ... + O'n(151548)
in a single case becase we could have

inf + O(inf) + O'2(inf) + ... + O'n(inf) ?

solve.

if a real number is calculated to be inf^2 if it was only
made of infinite squares then how can we say that inf^2 
has two cardinalities. in an empty space there is 0 space
this is not even a point, this is a belladurn.

in the first space we have infinity
in the second space we have inf^2 + i*inf
in the third space we have ((inf^2) + i*inf)^2

the point is that the first space is the empty space
is the point for an integer,
so a real number is a two integer space because
there is a . that seperates two integer spaces

so we have 512321.123213 then we also have

123214.21412421.21421214.124214.214124

there are 4 dots here in this example but that also means this
an amount of spaces above the space for a real number
so imagine allocating a dot is a new realer format at every
point

then 21323 is an int
then 213.213 is a real number
then 5215.2215.215215 is a complex number right? wrong?

521.213.213 is equal to fractional components of complex numbers so,

imagine now,

521.213.213 + i(521.213.213)

this simple complex number would now be infinitely confusable if
it could be a complex number but thats the point!

521.213.213 + i(521.213.213)

the fractional component 213 now adds to the same component
where i(521.213.213) used to be

before it became 0 because it now is the third element of the
numbers i!

so,

then,

some magical set of operators O,

521.213.213 + i(521.213.213) = 521.213 + iO(213) + i'O(521.213.213)

this would then require for example adding atleast

.213 to 521.213

adding .213.213 atleast to O(213)

to be able to push i'O(521.213.213) to then copy over the same way.

so then where does 3 dots come into play then?

so with 123214.21412421.21421214.124214

we now have two integer slots after the first so we could then 
stop there!

because with two integer slots after a real number we could
calculate the sides exapnsion in a riemann sum with two integers
that were derived from exactly informal numbers. that means
that the wrong conlcusion to make is this.

that 5 dots are needed to do this computation,

123214.21412421.21421214.124214.21421214.124214

the math for 5 dots is literally the same math but only
harder to do in every way possible.

because informal numbers means we have 

123214.21412421.21/4/21/214.1/24/21/4

this is why a 3 dot number system is more efficient to calculate
than a 5 dot number system, informal numbers are necessary to
understand that they are needed to solve the 5D problem
in an efficient amount of time on earth (NP?)

and maybe that might be because every dot creates another NP hardness
that NP hardness is harder than the amount of time our universe
would take to die. that means it's supposed to take about
that long to do before it would supposedly "die".
my opinion. 5 dots means that a 12D string theory is actually
the 18D string theory. we live in a 12D universe so 18D
math could be a higher dimension around physics here.

this means that the universe is 12D - in terms of string theory

there seems to be a space between towers measuerd
by the change in x which then goes to 0 at the same
time it squeezes the height between each riemann square
to each other. but that means the height difference between
the left riemann sum compared to the right riemann sum
integrate at different speeds. we have

lets say f(x) = x then at every riemann square the left
and right height differences would integrate at the
same constant. if we can say that then equates
to a difference in height of 1 for a square size of 1
(rise over run are the same) then we can actually start
to integrate the sides of riemann sum using integers
and informal numbers if instead of squeezing riemman sum
square size to 0 we could that calculation using integer
values for square sizes. that means that integration
could be done with a square size which would be the diff.
that you integrate by. normal integration uses 0.
but using a seperate formalution of 0 send to it by informality
it could be a different base for integrating height.
this means that squeezing happens where squeezing should happen

so if you had a function that needed smaller squares for ex after 1

if f(x) = { x if x<1 and x^2 if x>=1 }
then riemann squares would squeeze faster after x = 1 to normalize
the rise/run distributing along a real number

what is the integral of 1.2.5x then,

simple 1.2.0.5x^2 is the result of the integration.

that means integrating on time could be expressed otherwise

(1.2.5 + +>X) because if 1.2 + i is the point of complex numbers
then 1.2.5 + 1.2.5(+>X) is the point of informal numbers. so
this means while i is uncomplementary to its expansions
informal number are when are component to two decimal numbers

this is because .5 is just an informal number too.

this means (1.2.5 + 1.2.5(+>X)) + i(1.2.5 + 1.2.5(+>X))

would be a complex informal number because finding the second
pattern for combinatorical growth other i might be "dirac x"
or +d x or +> x, which i thought before.

this means that to add a new type of i in mather after i you
have to make the complex pattern again and add a . to the end
of every number that is just the new expansion.

so i is the number which takes 1 to 1.2 always. if you always
restrict your domain to integers you might also always find
shortcuts to integration without forcefully include the algebra
related to i calculus because the algebra related to +d might
be already a new +d calculus for itself then,

we could have, 

2. (1.2.5 + 1.2.5(+>X)) + i(1.2.5 + 1.2.5(+>X)) +d ((1.2.5 + 1.2.5(+>X)) + i(1.2.5 + 1.2.5(+>X)))

and this is also an informal number.

this means that

1. 521.213.213 + i(521.213.213) = 521.213 + iO(213) + i'O(521.213.213)

is the past math which takes you to two so,

so we have 

1.2.5 + i(1.2.5) = 1.2 + 5i + 
i'((1.2.5 + 1.2.5(+>X)) + i(1.2.5 + 1.2.5(+>X)) +d 
((1.2.5 + 1.2.5(+>X)) + i(1.2.5 + 1.2.5(+>X))))

so, 
1.2.5 + i(1.2.5) - 
i'((1.2.5 + 1.2.5(+>X)) + i(1.2.5 + 1.2.5(+>X)) +d 
((1.2.5 + 1.2.5(+>X)) + i(1.2.5 + 1.2.5(+>X))))

= 1.2 + 5i so what is i'*i then? i'' so that means

i'1.2.5 + i'1.2.5(+>X) + i''1.2.5 + i''1.2.5(+>X) +d 
i'1.2.5 + i'1.2.5(+>X) + i''1.2.5 + i''1.2.5(+>X)

so we have,

i'1.2.5 + i'1.2.5(+>X) +d i'1.2.5 + i'1.2.5(+>X) +
i''1.2.5 + i''1.2.5(+>X) +d i''1.2.5 + i''1.2.5(+>X)


this is the integer format for a real numbered informal number
it obeys all rules as x so

i'1.2.5 + i'1.2.5(+>X) +d i'1.2.5 + i'1.2.5(+>X) +
i''1.2.5 + i''1.2.5(+>X) +d i''1.2.5 + i''1.2.5(+>X)

could equal only an irrational number but that
means that you'd have to encode all 0s instead of
leaving blank information to assume.

lets say you had button with a func f()

and you only had one button and you pressed it many times

now imagine another function g() has a button

you can press the first and second button as many times as you want
for ex,

fgggggffffgffgfffggfgffgffgggffgf is a bunch of button presses

in a sequence one button is always pressed after another there
are no race conditions in this hypothetical

so then button h() does something weird h() switches button 1
to be g() and button 2 to be f().

so then that means fgggggffffgffgfffggfgffgffgggffgf is ok

but fgfgf h fgffgf is a sequence where we flipped f and g

so, 121 h 212 would then be then be 121121 there is a turing complete
language that can utilize this as machine code

there is only the option to now switch buttons with more buttons
in a way that is exactly defined so lets say button 4 is J()

then you have J() switches button 3 and button 2 then

fgfgf J h fgffgf

would then become for ex, 121223 = 121 J h 212!

so if we had a number system like one where

a = 0, b = 1, c = swap(a,b), d = swap(b,c), ...
then this swap math is turing complete, assumably

so, the func standardly applied to a writes 0 and 
the func for b writes 1 then swapping the func to write 
only by possibly swapping it with a func to swap specific 
slots means that only 2 letters in the alphabet will ever 
be assigned to a function which writes in the sequence 

a button is void function in pure math

f(x) is a function, f() is a button

if buttons a() and b() lead to buttons write0() write1() and swap0(), swap1(), ... , swapn() 
then this is the point of this math being about buttons only mapping to buttons purely

now imagine a() is (write 0) and b() is write(1) and c swaps a's action with b's action

a() is only a button because actions are numbered so 1() is unit function
in the action set and a() is the unit button in the button set