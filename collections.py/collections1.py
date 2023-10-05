myFruitList = ["apple", "banana", "Orange", "Veggies"]
print(myFruitList)
print(type(myFruitList))

#ACCESSING A LIST BY POSITION
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

#CHANGING THE VALUES IN A LIST
myFruitList[1] = "Pear"
print(myFruitList)

#INTORODUCING THE TUPLE DATA TYPE
#A list uses square brackets [] whiel Tuple uses () brackets
myFinalAnswerTuple = ("apple", "Pear", "Orange")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

#DEFINNG A DICTIONARY
myFavoriteBooksDictionary = {
    "Fiction" : "Half of a yellow sun",
    "Motivation" : "Eat that frog",
    "Spiritual" : "Why revival tarries"
}
print(myFavoriteBooksDictionary)
print(type(myFavoriteBooksDictionary))
#Accessing a dictionary by name
print(myFavoriteBooksDictionary["Fiction"])
print(myFavoriteBooksDictionary["Motivation"])
print(myFavoriteBooksDictionary["Spiritual"])