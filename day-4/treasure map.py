row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1,row2,row3]
print(f"{row1}\n{row2} \n{row3}")
position = input("Where do you want to put the treasure? ")

row=int(position[1])-1
col=int(position[0])-1

# The elements that are to be mapped!

# Mapped_treasure = [col,row]
# print(Mapped_treasure)

map[row][col] = ' X'

print(f"{row1}\n{row2} \n{row3}")

