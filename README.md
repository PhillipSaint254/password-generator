1. A description of the algorithm used in the password generation
   -  After getting all inputs about What the user wants for the password, code provided runs the password generator algorithm
   -  The first stage of this algorithm is initialization of values and dealing with edge cases
   -  Then, depenant on what characters the user wants in the password, the algorithm runs the following steps:
      * Make sure the number of characters specified as the minimum length is atleast equal to the number of characters specified for inclusion
      * Weight calculation - These weights are the defined percentage of the number of characters that will exist in the password to be generated depending on the characters included.
      * These weights are specified for each of the characters to be included in the password
      * Password generation is done step by step per the character(s) to be included in the password 
      * Mixer function - This function is used to mix the position of the each character in any string randomly
      * At every stage (as per character to be included) of password generation, the password string created is subjected to the mixer function
      * This ensures that it is very hard if not impossible for a hacker to determine the posioning of a character even if he had all characters used in the password
      * At the end, return the generated password to the user
