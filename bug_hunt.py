count = 1
total = 0

# BUG: Added the missing colon required before the while-loop body.
# BUG: Changed < to <= so the loop includes 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Converted total to a string so it can be joined to the message.
print("Sum of 1 to 5 is: " + str(total))