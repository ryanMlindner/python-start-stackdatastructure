
class stack:
   def __init__(self):
      self.storage = list()

## TODOne make functs return vars

   def peek(self):
      var = 0
      if self.storage:
         var = self.storage[-1]
      return var

   def pop(self):
      var = 0
      if self.storage:
         var = self.storage[-1]
         self.storage.pop()
      return var

   def push(self, input):
      self.storage.append(input)
      return input

## TODOne make functions in stack return variables
## to make them testable easier
if __name__ == '__main__' :
   done = 0
   dataStack = stack()

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
               print("input: \"" + dataStack.push(userData2)
               + "\" successfully added")

      elif userData == "isEmpty":
         if dataStack.peek(): print("Not Empty")
         else: print("Empty")
         

      elif userData == "pop":
         if dataStack.peek():
            print("top item: \"" + dataStack.pop() + "\" removed")
         else: print("cannot pop, stack is empty")

      elif userData == "peek":
         if dataStack.peek():
            print("top item: \"" + dataStack.peek() + "\"")
         else: print("cannot peek, stack is empty")

      elif userData == "exit":
         done = 1  

##exit()