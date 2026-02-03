str1 = "haseeb" 
str2 = "tariq"

print(str1+str2) #cancatenation

str = "haseeb"
print(len(str)) #length


str = "haseeb"
str = str[5]
print(str) #indexing


str = "haseeb"

print(str[:5]) #slicing

str = "haseeb"
print(str.endswith("eb")) #to check ending of string
print(str.endswith("ee"))
str = str.capitalize() #to capitalize the first character of string
print(str.capitalize())

print(str)

str = "haseeb"
print(str.replace("e", "a"))
print(str.replace("haseeb", "ahmad")) #to replace the old string with new one

str = "haseeb"
print(str.find("b"))#to find the index of character

str = "i am haseeb tariq \n i am studying python"
print(str.count("am")) #to check the occurence of a occurer