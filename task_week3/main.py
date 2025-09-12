from div import divide
from sum import sum
from sub import sub
from multi import multiply

def getNumsPrompt():
    p = input("Enter Two Numbers (10,20): ").split(',');
    inNum = list(map(int,p))
    # print(inNum,"-",inNum[0],inNum[1]);
    return inNum

# print(getNumsPrompt())

while True:
    nums = getNumsPrompt()
    num1=nums[0];
    num2=nums[1];
    prompt = input("Select Option (+,-,/,*): ")
    
    match(prompt):
        case "*":
            m = multiply(num1,num2)
            print(f"Multiple {num1}*{num2} = {m}")
        case "/":
            d = divide(num1,num2)
            print(f"Divide {num1}/{num2} = {d}")
        case "+":
            s = sum(num1,num2)
            print(f"Sum {num1}+{num2} = {s}")
        case "-":
            subtract = sub(num1,num2)
            print(f"Sub {num1}-{num2} = {subtract}")
        case _:
            print("Invalid Options!")
    
    rep = input("Do you want to perform more calculations (y/n): ").lower()
    if rep == 'n': break