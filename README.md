# Simple calculator
Commandline calculator. 

First summs up x quantitiy of items by their price.
Then substracts discount based on these rules:
```
>= 50000$ = 15%
>= 10000$ = 10%
>=  7000$ =  7%
>=  5000$ =  5%
>=  1000$ =  3%
```

Lastly adds taxes based on input for these states:
```
"TX" = 6.25%
"NV" = 8.00%
"CA" = 8.25%
"UT" = 6.85%
"AL" = 4.00%
```

Example output:
```
Order value: 271.92$
Discount: 0$
Order value after discount: 271.92$
Tax: 17.0$
Total price with 6.25% tax: 288.92$
```