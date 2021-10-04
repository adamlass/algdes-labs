import re, json

def get_blosum():
    f = open("./data/BLOSUM62.txt")
    lines = f.readlines()

    blosum = None
    blosum_chars = None

    for line in lines:
        if(line[0] == "#"):
            continue
        else:
            splits = line.split("\n")[0].split(" ")
            splits = list(filter(lambda x: x != "", splits))

            if(blosum == None):
                blosum_chars = splits
                blosum = {i: {j: 0 for j in splits} for i in splits}
            else:
                char = splits[0]
                for i in range(len(blosum_chars)):
                    b_char = blosum_chars[i]
                    blosum[char][b_char] = int(splits[i + 1])

    penalty_char = blosum_chars[-1]
    penalty = int(blosum[blosum_chars[-1]][blosum_chars[0]])

    return {"matrix":blosum, "penalty": penalty}

blosum = get_blosum()

# Serializing json 
json_object = json.dumps(blosum, indent = 4)
  
# Writing to sample.json
with open("data/blosum.json", "w") as outfile:
    outfile.write(json_object)

