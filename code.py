import os

def hello(a_name):
  print("Hello! " + a_name)

def hello2(name_a,name_b):
  print("Hello" + name_a + " and " + name_b)


def sum_two(x,y):
  z = x + y
  return z 


import math
def circle_area(radius):
  # return the area
  area = math.pi*radius**2
  return area 

print(circle_area (4))

def today():
  now = datetime.datetime.now()
  return now.day

def my_sum(a_list):
    total = 0
    for n in a_list:
        total = total + n
    return total

def my_prod(a_list):
  total  = 1
  for n in a_list:
     total = total * n
  return total

def my_count(a_list):
  # number of items in the list
  count = 0
  for n in a_list:
     count = 1 + count  
  return count 

def my_count_less_5(a_list): 
  count = 0
  for n in a_list:
    if n < 5:
      count = count + 1
  return count
 
def my_count_ones(a_list):
  count = 0
  for n in a_list: 
    if n == 1:
     count = count + 1
  return count

def is_list_empty(a_list):
  if my_count(a_list) == 0:
    return True
  else: 
    return False 

def my_max(a_list):
  if is_list_empty(a_list):
    return None 
  b = a_list[0]
  for n in a_list:
    if n > b:
      b = n 
  return b

# get filenames("C:\\Users\\sback")
# --> list of file names
# ['code.py', 'imageprocessor.py', 'loops.py', 'start.py']

def get_filenames(a_dirname):
  list_of_files = os.listdir(a_dirname)
  all_files = []
  for filename in list_of_files:
    print(filename)
    full_path = os.path.join(a_dirname,filename)
    all_files.append(full_path)
  return all_files

# Rotation aller Beispiele 

pic_list = code.get_filenames("C:\\Users\\JuliaMB\\Desktop\\Pictures")
num = 0
for pic_name in pic_list:
  num = num + 1
  im = Image.open(pic_name)
  im = to_grayscale(im)
  
  newfilename = "pic_gray_" + str(num) + ".jpg"
  newfullpath = os.path.join
  im.save("C:\\Users\\JuliaMB\\Desktop\\Pictures\\grayscale")

def to_grayscale(an_image):
  grayscale_im = an_image.convert('LA')
  return grayscale_im

im = Image.open("C:\\Users\\JuliaMB\\Desktop\\Pictures\\picture2.jpg")
im = to_grayscale(im)
im.save("C:\\Users\\JuliaMB\\Desktop\\Pictures\\picture2.jpg")

# 13.2.2019
#[12, 34, [56, 67]] -> [12 34 56 67]
def flatten(a_list_with_lists):
  new_list = []
  for n in a_list_with_lists:
    if isinstance(n,list):
      for i in n: 
        new_list.append(n)
  return new_list

# neue Liste 
a_list = [12, 34, [56, 67], 78]
flattened_list = flatten(a_list)
print(flattened_list)

def print_right(a_list_with_lists):
    for n in a_list:
        if isinstance(n,list):
            for i in n:
                print(i,end='')
            print('')
        else:
            print(n)


#single_row_stars(4) -> ****
#single_row_stars(6) -> ******
def single_row_starts(numbers):
  for n in range(numbers):
    print('*',end='-')

#single_row_of(4,"*") -> ****
#single_row_of(3,"-+") -> -+-+-+
# def single_row_of(number,string):
# continue in intro1.py