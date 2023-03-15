words =  ['demo', 'none', 'tied', 'evil', 'dome', 'mode', 'live',
         'fowl', 'veil', 'wolf', 'diet', 'vile', 'edit', 'tide',
         'flow', 'neon']
tmp = {}
output = []
words.collect do |word|
  if tmp[word] == nil
    result = words.filter { |w|
      # p "word:#{word}"
      count = w.chars.filter {|c|
        # p "#{c}, #{word}"
        word.chars.find_index(c) == nil
      }
      # word.split("").each { |c|
      #   p w
      #   w.gsub!(c, "")
      # }
      # p "check:#{w}"
      count.length == 0
      # w.length == 0
    }.to_a

    result.each { |w|
      tmp[w] = 1
    }
    output.push(result)
  end
end

p output
