 List - []


word = 'Programming'
 word[2]
 word[10]
 word[3:5]
  word[5:9]
  word[-4:4]
  word[4:-4]
  word[:5]
  word[8:]
 word[3:]
 word[:3]
 word[:3] + word[3:]




'Programming'
 p  r  o  g  r  a  m  m  i  n  g
 0  1  2  3  4  5  6  7  8  9  10
-11-10-9 -8 -7 -6 -5 -4 -3 -2 -1

 x = 'Hello World'
 x[3]
 x[-5]
 x[-6]
 x[0]



len(word)

 len(word) + len(x)
22
cube = [10, 20, 30, 45, 50]
cube
[10, 20, 30, 45, 50]
cube[3]
45
cube[3]= 40
cube
[10, 20, 30, 40, 50]
cube.append(60)
 cube
[10, 20, 30, 40, 50, 60]
cube.append(4+10+20+36)
cube
[10, 20, 30, 40, 50, 60, 70]
 cube.reverse()
 cube
[70, 60, 50, 40, 30, 20, 10]
cube.reverse()
 cube
[10, 20, 30, 40, 50, 60, 70]
 cube.sort()
>>> cube
[10, 20, 30, 40, 50, 60, 70]
>>> cube.remove(20)
>>> cube
[10, 30, 40, 50, 60, 70]
>>> cube.append(20)
>>> cube
[10, 30, 40, 50, 60, 70, 20]
>>> cube.sort()
>>> cube
[10, 20, 30, 40, 50, 60, 70]
>>>
>>> cube1 = [10, 20, 30, 45, 50]
>>> cube2 = [1, 2, 3, 4, 5]
>>> cube3 = cube1 + cube2
>>> cube3
[10, 20, 30, 45, 50, 1, 2, 3, 4, 5]
>>> cubeA = ['A', 'B', 'C', 'D', 'E']
>>> cube4 =cube1 + cubeA
>>> cube1.extend(cube2)
>>> cube1
[10, 20, 30, 45, 50, 1, 2, 3, 4, 5]
>>> del cube1[3]
>>> cube1
[10, 20, 30, 50, 1, 2, 3, 4, 5]
 del cube1[1:3]
>>> cube1
[10, 50, 1, 2, 3, 4, 5]
>>> del cube1[:]

programA = ['A', 'B', 'C', 'D', 'E']
>>> programB = ['a', 'b', 'c', 'd', 'e']
>>> programC = programA + programB
>>> programC
['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e']
>>> programC[9:]
['e']
>>> program[9:] 



 a = [10, 20, 30, 40, 50]
>>> b = [60, 70, 80, 90, 100]
>>> c = [110, 120, 130, 140, 150]
>>> x = [a, b, c]
>>> x
[[10, 20, 30, 40, 50], [60, 70, 80, 90, 100], [110, 120, 130, 140, 150]]
>>> x[2][4]
150
>>> x[0][2]
30
>>> x[1][1]
70
>>> x[][3]
  File "<stdin>", line 1
    x[][3]
      ^
SyntaxError: invalid syntax
>>> x[1][2]
80
>>> x[1][1:2]
[70]
>>>https://docs.python.org/3/tutorial/datastructures.html
5.1.3. List comprehensions
5.1.4. Nested List comprehensions
5.2 The del Statement