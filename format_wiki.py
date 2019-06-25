import glob
import re
if __name__ == '__main__':
    path = glob.glob("raw_input/*/*")
    count = 0
    for i in path:
        with open(i,encoding = "utf-8") as f:
            line = f.readlines()
            line_st = ""
            line_list = []
            flag = False
            for j in line:
                if flag:
                    flag = False
                    continue
                elif "<doc" in j:
                    flag = True
                    continue
                elif "</doc" in j:
                    if len(line_st) > 5:
                        line_list.append(line_st)
                        line_st = ""
                    continue
                elif len(j) < 5:
                    continue
                else:
                    line_st += j.strip() + "\n"
            for tmp_count, j in enumerate(line_list):
                with open("input/wiki/"+ str(count+tmp_count)+".txt", "w", encoding="utf-8") as f:
                    f.write(j)
            count += len(line_list)
        print(str(count))
