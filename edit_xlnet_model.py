import sentencepiece as spm
import sentencepiece_model_pb2 as model
import re
sp = spm.SentencePieceProcessor()

m1 = model.ModelProto()
m2 = model.ModelProto()

m1.ParseFromString(open('spiece.model', 'rb').read())
m2.ParseFromString(open('wiki-ja.model', 'rb').read())

count = 0

print(dir(m1))
new_wordlist = []
'''
[PAD]	0
[CLS]	0
[SEP]	0
[MASK]	0
'''
for idx, p in enumerate(m1.pieces):
    if count == 20:
        break
    count += 1
    print("iter")
    print(p)
    print(dir(p))
    print("id access")
    print(m1.pieces[idx])
    print(dir(m1.pieces[idx]))
    print(count)
tmp1 = m1.pieces[0:17]
count = 0
for idx, p in enumerate(m2.pieces):
    if count == 20:
        break
    count += 1
    print("iter")
    print(p)
    print(dir(p))
    print("id access")
    print(m2.pieces[idx])
    print(dir(m2.pieces[idx]))
tmp2 = m2.pieces[7:]
tmp3 = []
for i in tmp2:
    flag = False
    for j in tmp1:
        if j.piece == i.piece:
            flag = True
            break
    if not flag:
        tmp3.append(i)
concat = tmp1+tmp3
print(len(m2.pieces))
print(len(tmp2))
print(len(tmp3))
print(len(concat))
print(len(concat[:32000]))
print(concat[32000])
del m1.pieces[:]
m1.pieces.extend(concat)
with open('new.model', 'wb') as f:
    f.write(m1.SerializeToString())
