while True:
  my_list = []
  number = int(input("number:"))
  if number == "done":
    print (my_list)
    break
  elif number > 5:
    my_list.append(number)
  