
class stack:
   def __init__(self):
      self.storage = list()

##      list = list()
##      fill(data)
##   def fill(*data):
##      while bool(data):
##         list.append(data[0])
##         del data[0]

   def peek(self):
      print("top item: \"" + self.storage[-1] + "\"")

   def pop(self):
      if self.storage:
         print("top item removed: \"" + self.storage[-1] + "\"")
         self.storage.pop()
      else: print("cannot pop, stack is empty")

   def push(self, input):
      self.storage.append(input)
      print("input: \"" + input + "\" successfully added")

   def isEmpty(self):
      print("Not Empty") if self.storage else print("Empty")

done = 0
dataStack = stack()

## TODOing make enter data its own input, and null for other commands,
## otherwise you cant store the commands as data
## done

while not(bool(done)):
   userData = input("use pop, peek, isEmpty, exit, or use push for data input:")
   
   ## while loop for data entry, can be entered and exited at will
   ## by the user
   if userData == "push":

      ## flag var for finishing while loop
      entryDone = 0

      while not(bool(entryDone)):
         userData2 = input("enter datum for entry, or \'*\' to go back:")
         if userData2 == "*":
            entryDone = 1
         else:
            dataStack.push(userData2)

   elif userData == "isEmpty":
      dataStack.isEmpty()

   elif userData == "pop":
      dataStack.pop()

   elif userData == "peek":
      dataStack.peek()

   elif userData == "exit":
      done = 1  

exit()