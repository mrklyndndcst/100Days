# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
col = int(position[0]) - 1 
row = int(position[1]) - 1

# if row == 1:
#   row1[col] = "💎"
# elif row == 2:
#   row2[col] = "💎"
# else:
#   row3[col] = "💎"

#or

map[row][col] = "💎"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")