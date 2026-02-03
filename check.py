# with open("fill.txt", "r") as f:
#      data = f.read()
# new_data = data.replace("python","javascript")
# print(new_data)

# def check_for_word():
#     word = "learning"
#     with open("fill.txt", "r") as f:
#          data = f.read()
#     if (data.find(word)!= -1):
#             print("Found")
#     else:
#             print("Not found")     
# check_for_word()

# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("fill.txt","r") as f:
#           while data:
#                 data = f.readline()
#                 if word in data:
#                       print(line_no)
#                       return
#                 line_no +=1
#     return -1            
# check_for_line()   

# with open("new.txt", "r") as f:
#       data = f.read()
#       print(data)
      
#       num = ""
#       for i in range(len(data)):
#             if (data[i] == ","):
#                   print(int(num))
#                   num = ""
#             else:
#                   num += data[i]  

count = 0
with open("new.txt", "r") as f:
      data = f.read()

      nums = data.split(",")
      print(nums)                     
      for val in nums:
            if(int(val) % 2==0):
                  count +=1
print(count)
