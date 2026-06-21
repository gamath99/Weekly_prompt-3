# Subject 2
#      Pick a S.O.L.I.D design principle and explain the concept and how you can meet that principle when designing a program.
# In Object-oriented programming,  a class can be refer as a blueprint used to create object that share common properties and behavior. It can be created by using the Class keyword followed by te class name.
# To unsure a better fluidity when using class, it is necessary to consider the mnemonic acronym S.O.L.I.D. It refers to five principles intended to make source code more understanble, flexible, and maintainable.
# The five principles are 
#      - singles responsibility principle, 
#      - open-closed principle, 
#      - Liskov substitution principle, 
#      - Interface segregation principle 
#      - Dependency inversion principle.
# One of the most common principles that can be apply when using class statement is the singles responsibility principle. it states that: a class should have only one reason to change. This principle help to make the code more 
# understanble and readable. It also help to avoid inserting multiple functions in the same class that execute different result or might modify the behavior if a data have to change. Therefore, if a class implements multiple responsabilities, they are 
# no longer independent of each other and will require to modify data for each functions. Moreover, the single responsibility principle provide more fluid coding line and reduce the number of bugs as it is much easier to explain and understand. 
# However, as long as it is important to make sure the class does not execute multiple tasks at once, we should ensure to not oversimplify the program and analyze the statement to find the perfect balance for the responsibilities. 
# To meet that principles when designing a program it is important to always ask certain question that can help to identify if it will be a multitask like :  what is the responsibility of my class? does this class perform more than one unrelated task? 
# if the answer includes the word "and", it might requires to analyze the responsibility of the class and make it is single responsibility.  
# Finally, by assigning one responsibility to each class, the program becomes more organized, flexible, and easier to maintain.  

