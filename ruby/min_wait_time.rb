task_arr = [1, 6, 4, 8]

[1, 6, 4, 8]

# [1, 4, 6, 8]
# 0 + 1 + (4 + 1) + (1 + 4 + 6) = 17

# [8, 4, 6, 1]
# 0 + 8 + (8 + 4) + (8 + 4 + 6) = 38

# [1, 8, 4, 6]
# 0 + 1 + (8 + 1) + (8 + 4 + 1) = 23

def minimun_wait_time(arr)
  arr.sort!
  # sum = 0
  # arr.each_with_index { |v, idx|
  #   if idx < arr.length - 1
  #     p "IDX: #{idx}, CURR: #{sum}, V: #{v}"
  #     sum += sum + v
  #   end
  # }
  # sum
  arr.reduce {|m, n|
    sum = m
    if n < arr[arr.length - 1]
      p "M: #{m}, N: #{n}"
      sum = m + n
    end
    sum
  }
end

p "MINIMUM WAIT TIME: #{minimun_wait_time(task_arr)}"
