def write_file():
    with open('clean_data/ques2.txt','r') as f, open('data_file/0.txt','w') as f0, open('data_file/1.txt','w') as f1, \
            open('data_file/2.txt','w') as f2, open('data_file/3.txt','w') as f3, open('data_file/18.txt','w') as f18:
        for line in f:
            if line != "\n":
                label_number, question = line.split("\t")
                label,number = label_number.split("||#")
                if label == '0':
                    f0.write(line)
                if label == '1':
                    f1.write(line)
                if label == '2':
                    f2.write(line)
                if label == '3':
                    f3.write(line)
                if label == '18':
                    f18.write(line)

if __name__ == '__main__':
    write_file()