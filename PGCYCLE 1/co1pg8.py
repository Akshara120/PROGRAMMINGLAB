#8. Get a string from an input string where all occurrences of first character replaced with
#‘$’, except first character.
#[eg: onion -> oni$n]

str=input("enter the string:")
char=str[0]
str=str.replace(char,'$')
print(char+str[1:])