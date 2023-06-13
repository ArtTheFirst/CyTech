row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
right_figure = int(position[0])
left_figure = int(position[1])
marker = 'X'
if left_figure == 1 and right_figure == 1:
            row1 = [marker,"️⬜️","️⬜️"]
elif left_figure == 1 and right_figure == 2:
        row1 = ["️⬜️",marker,"️⬜️"]        
elif left_figure == 1 and right_figure == 3:
        row1 = ["️⬜️","️⬜️",marker]
elif left_figure == 2 and right_figure == 1:
        row2 = [marker,"️⬜️","️⬜️"]
elif left_figure == 2 and right_figure == 2:
        row2 = ["️⬜️",marker,"️⬜️"]
elif left_figure == 2 and right_figure == 3:
        row2 = ["️⬜️","️⬜️",marker]
elif left_figure == 3 and right_figure == 1:
        row3 = [marker,"️⬜️","️⬜️"]
elif left_figure == 3 and right_figure == 2:
        row3 = ["️⬜️",marker,"️⬜️"]
elif left_figure == 3 and right_figure == 3:
        row3 = ["️⬜️","️⬜️",marker]
print(f"{row1}\n{row2}\n{row3}")
