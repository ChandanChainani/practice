require 'keccak256'

def _nodejs_buffer_to_hex origin_string
  #origin_string = "ce159cf3"

  i = 0 
  result = []
  temp = ""
  loop do
    break if i == origin_string.length
    temp += origin_string[i]
    if i % 2 == 1
      result << temp
      temp = ""
    end 
    i += 1
  end

  result = result.map do |e| 
    "0x#{e}".hex
  end 

  return result.join()
end 

def get_name_hash name
  node = "0" * 64

  if (name)
    labels = name.split(".")
    i = labels.size - 1
    puts i
    while i >= 0
      puts labels[i]
      labelSha = Digest::Keccak256.new.hexdigest(labels[i])
      # here will throw the exception: 
      node = Digest::Keccak256.new.hexdigest(_nodejs_buffer_to_hex(node + labelSha))
      i -= 1
    end
  end

  return "0x" + node;
end

result = []
"abcd".split("").each_with_index {|letter, idx|
  puts "#{idx}:#{idx.class}, #{letter}:#{letter.class}"
  if idx % 2 == 1
    result << letter.hex
  end
}

puts get_name_hash "a"
puts get_name_hash "a.b"
puts get_name_hash "abc.def"



def sha3raw(str)
  Digest::Keccak.digest(str, 256)
end

def tohex(binary_str)
  binary_str.unpack('H*').first
end

def get_namehash(str)
  node = "\x0" * 32
  labels = str.split(".").reverse
  while labels.length > 0
    label = labels.shift
    labelhash = sha3raw(label)
    p 'labelhash', tohex(labelhash)
    node = sha3raw(node+labelhash)
  end

  "0x" + tohex(node)
end
