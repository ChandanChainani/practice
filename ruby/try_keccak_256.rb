# import { keccak_256 } from "js-sha3";
# import { Buffer } from "buffer/";
#
#
#
# export function getNamehash(name: string) {
#   let node = "0000000000000000000000000000000000000000000000000000000000000000";
#
#   if (name) {
#     let labels = name.split(".");
#
#     for (let i = labels.length - 1; i >= 0; i--) {
#       let labelSha = keccak_256(labels[i]);
#       node = keccak_256(Buffer.from(node + labelSha, "hex"));
#     }
#   }
#
#   return "0x" + node;
# }

require 'digest/keccak'

def getNamehash(name)
  node = "0000000000000000000000000000000000000000000000000000000000000000"

  if name
    labels = name.split(".");

    labels.each { |label|
      labelSha = Digest::Keccak.hexdigest(label, 256)
      # p labelSha.class, node.class, (node + labelSha).hex.class
      # node = Digest::Keccak.hexdigest((node + labelSha).hex.to_s, 256)
      node = Digest::Keccak.hexdigest((node + labelSha), 256)
    }
  end

  "0x" + node;
end


# p getNamehash("a") # == "0xc3025f6c23b9ab4d91adbcccf350072ec880c65db9a3f42e802fe4ceed56e728"

# p getNamehash("a.b")  #== "0xa57dcb7e802753630ec035bae538ca332465791509b1375525fe8b3b0bada7ef"

# p getNamehash("abc.def")  #== "0xc3025f6c23b9ab4d91adbcccf350072ec880c65db9a3f42e802fe4ceed56e728"

def sha3raw(str)
  Digest::Keccak.digest(str, 256)
end

def tohex(binary)
  binary.unpack('H*').first
end

def get_namehash(str)
  node = "\x0" * 32
  labels = str.split(".").reverse
  while labels.length > 0
    label = labels.shift
    labelhash = sha3raw(label)
    # p 'labelhash', tohex(labelhash)
    node = sha3raw(node+labelhash)
  end

  "0x" + tohex(node)
end

p get_namehash("a") # == "0xc3025f6c23b9ab4d91adbcccf350072ec880c65db9a3f42e802fe4ceed56e728"

p get_namehash("a.b")  == "0xa57dcb7e802753630ec035bae538ca332465791509b1375525fe8b3b0bada7ef"

p get_namehash("abc.def")  == "0xc3025f6c23b9ab4d91adbcccf350072ec880c65db9a3f42e802fe4ceed56e728"
