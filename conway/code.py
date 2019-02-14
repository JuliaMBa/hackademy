#single_row_stars(4) -> ****
#single_row_stars(6) -> ******
def single_row_stars(number):
  for n in range(number):
    print('*',end='-')

#single_row_of(4,"*") -> ****
#single_row_of(3,"-+") -> -+-+-+
def single_row_of(number,string):
    for n in range(number):
      print(string,end="")

# square_of_stars(4)
# ->
# ****
# ****
# ****
def square_of_stars(num):
  for m in range(num): 
    for n in range(num):
      print("*",end="")
    print("")

def rectangle_of_stars(row,cols):
  for m in range(row):
    for n in range(cols):
      print("*",end="")
    print("")

# list_by_2([1,2,3]) -> [2,4,6]
def list_by_2(a_list):
  new_list = []
  for n in a_list:
    t = n * 2
    new_list.append(t)
  return new_list 

# create_grid(4)
# - 
# [['-','-','-','-'],
#  ['-','-','-','-'],
#  ['-','-','-','-'],
#  ['-','-','-','-']]
def create_grid(size):
  new_grid = []
  for row in range(size):
    new_sublist = []
    for column in range(size):
      new_sublist.append('-')
    new_grid.append(new_sublist)
  return new_grid
