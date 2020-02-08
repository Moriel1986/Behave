import os, sys,random,unittest,HtmlTestRunner


class NBARoster:
    __name = ''
    __position = ''
    __height = ''
    __weight = 0
    __player_rating = 0
    __college = ''

    def __init__(self, name, position, height, weight, player_rating, college):
        self.__name = name
        self.__position = position
        self.__height = height
        self.__weight = weight
        self.__player_rating = player_rating
        self.__college = college

    def __set_name__(self, name):
        self.__name = name

    def __get_name__(self):
        return self.__name

    def __set_position__(self, position):
        self.__position = position

    def __get_position__(self):
        return self.__position

    def __set_height__(self, height):
        self.__height = height

    def __get_height__(self):
        return self.__height

    def __set_weight_(self, weight):
        self.__weight = weight

    def __get_weight__(self):
        return self.__weight

    def __set_player_rating__(self, player_rating):
        self.__player_rating = player_rating

    def __get_player_rating__(self):
        return self.__player_rating

    def __set_college__(self, college):
        self.__name = name

    def __get_college__(self):
        return self.__college

    def get_class(self):
        print("NBARoster")

    def get_player_info(cls):
        return "Name: {}, Position: {}, Height: {}, Weight: {}, Player Rating: {}, College: {}".format(cls.__name,
                                                                                                       cls.__position,
                                                                                                       cls.__height,
                                                                                                       cls.__weight,
                                                                                                       cls.__player_rating,
                                                                                                       cls.__college)


steph = NBARoster("Stephen Curry", "Point Guard", "6ft 3", 180, 96, "Davidson")
kobe = NBARoster("Kobe Bryant", "2Guard", "6ft 6", 220, 100, "N/A")

print(steph.get_player_info())
print(kobe.get_player_info())

######Sets#######
nba_teams = {"Warriors", "Bulls", "Bucks", "Spurs", "Hawks"}
print(nba_teams)
nba_teams.remove("Hawks")
print(nba_teams)
nba_teams.add("Lakers")
print(nba_teams)

for b in nba_teams:
    print(b.casefold())

for x in range(2, 45):
    print(x)

for a in [1, 2, 3, 4, 5, 6, 7]:
    print(a)


#  While loops

random_num = random.randrange(0, 100)

while random_num != 15:
    print(random_num)
    random_num = random.randrange(0, 100)


class Calculator:

    def add_num(num1, num2):
        sum_num = num1 + num2
        return sum_num

    def sub_num(num1, num2):
        sum_num = num1 - num2
        return sum_num

    def divide_num(num1, num2):
        sum_num = num1 / num2
        return sum_num

    def multi_num(num1, num2):
        sum_num = num1 * num2
        return sum_num

    def remain_num(num1, num2):
        sum_num = num1 % num2
        return sum_num


add = Calculator
print(add.add_num(234,888))
print(add.sub_num(234,888))
print(add.divide_num(234,888))
print(add.multi_num(234,888))
print(add.remain_num(234,888))












