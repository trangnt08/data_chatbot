from io import open

with open("clean_data/ques2.txt","r",encoding="utf-8") as f_r:
    with open("ques1.txt","w",encoding="utf-8") as f_w:
        for line in f_r:
            if line == "\n":
                f_w.write(line)
            else:
                x = line.split("||")
                label = x[0]
                if label != "13":
                    f_w.write(line)
                else:
                    line1 = "10"+"||"+x[1]
                    f_w.write(line1)
        f_w.close()
