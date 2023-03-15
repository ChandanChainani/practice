# input: 18
# output: 21

# def successor(arr, num)
#   h = {}
#   max_value = arr[0]
#   arr.each {|a|
#     h[a] = 0
#
#     if a > max_value
#       max_value = a
#     end
#   }
#
#   i = num
#   while i < max_value
#     i += 1
#
#     if h[i]
#       return i
#     end
#   end
#   return nil
# end

def successor(arr, num)
  # diff = (arr[0] - num).abs
  diff = nil
  result = -1
  i = 0
  while i < arr.length
    p "CURR: #{arr[i]}, DIFF: #{(arr[i] - num).abs}"
    if (diff == nil || (arr[i] - num).abs < diff) && arr[i] > num
    # if (arr[i] - num).abs < diff && arr[i] > num
       diff = (arr[i] - num).abs
       result = arr[i]
    end
    i += 1
  end
  result
end

arr = [1, 2, 141, 21, 18]
num = 18
p "First: #{successor(arr, 18)}"
p "Second: #{successor(arr, 2)}"
p "Second: #{successor(arr, 1)}"
