from pyuca import Collator
col = Collator()

file_obj = open("dictionary.txt", "r", encoding="utf8")

count = 0
dict = {}
english_word = ""

for line in file_obj:
    if count % 2 == 0:
        ## do something with english text
        ##print("English: " + line)
        english_word = line

    else:
        ## do something with greek text
        ##print("Greek: " + line)
        dict[english_word.rstrip("\n")] = line.rstrip("\n")

    count += 1

file_obj.close()

output_eng2grk = open("english2greek.txt", "a", encoding="utf8")
output_grk2eng = open("greek2english.txt", "a", encoding="utf8")

for key in sorted(dict.keys()):
    # print("%s: %s" % (key, dict[key]))
    output_eng2grk.write("%s: %s\n" % (key, dict[key]))

print("\n")

def get_key(val):
    for key, value in dict.items():
        if val == value:
            return key

for k in sorted(dict.values(), key=col.sort_key):
    # print("%s: %s" % (get_key(k), k))
    output_grk2eng.write("%s: %s\n" % (k, get_key(k)))


output_eng2grk.close()
output_grk2eng.close()