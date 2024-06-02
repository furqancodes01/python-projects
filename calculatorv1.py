#add
def add(n1,n2):
  return n1 + n2
#subtract
def subtract(n1,n2):
  return n1-n2
#multiply
def multiply(n1,n2):
  return n1*n2
#divide
def divide(n1,n2):
  return n1/n2
operations={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}
function =operations["+"]
function(2,3)
num1=int(input("What is the first number?: "))
num2=int(input("Whats the second number?: "))
for symbol in operations:
  print(symbol)
operational_symbol=input("Pick an operation from the line above: ")
calculation_function=operations[operational_symbol]
first_answer=calculation_function(num1,num2)
print(f"{num1} {operational_symbol} {num2} ={first_answer}")

operational_symbol = input("pick another operator: ")
num3=int(input("What is the next number?: "))
calculation_function=operations[operational_symbol]
second_answer = calculation_function(calculation_function(num1,num2), num3)
second_answer = calculation_function(first_answer, num3)
print(f"{first_answer} {operational_symbol} {num3} = {second_answer}")

