total_second = 9875
#a. Compute Hours, Minutes and Seconds
hours= total_second // 3600
minute = (total_second %3600) //60
second = total_second %60
#Or We Can write
#remaining_second = total_second % 3600
#minutes = remaining_second // 60
#seconds = remaining_second %60

print(f"{hours} H - {minute} m - {second} s")