def main():
    seperateLabelsAndDocs("dataset/all_sentiment_shuffled_filtered.txt")
    convertLabels("dataset/all_labels.txt")

#Makes separate 2 seperate files for labels and docs
def seperateLabelsAndDocs(filepath):
    all_labels = open("dataset/all_labels.txt","w+")
    all_docs = open("dataset/all_docs.txt","w+")

    with open(filepath) as f:
        for line in f:
            line = line.split(' ', 1)
            all_labels.write(line[0] + "\n")
            all_docs.write(line[1])

    all_labels.close()
    all_docs.close()

#Converts labels into 0 (neg) and 1 (pos)
def convertLabels(filepath):
    converted_labels = open("dataset/converted_labels.txt","w+")
    line_count = 0
    file_lines = 0

    #Get number of lines the file contains
    with open(filepath) as f:
        file_lines = len(f.readlines())
        print(file_lines)

    #Will create a new file with '1' and '0' instead of 'pos' and 'neg'.
    #The last line won't print a newline '\n'
    with open(filepath) as f:
        for line in f:
            line_count += 1
            if line_count == file_lines:
                if "pos" in line:
                    converted_labels.write("1")
                else:
                    converted_labels.write("0")
            else:
                if "pos" in line:
                    converted_labels.write("1\n")
                else:
                    converted_labels.write("0\n")

if __name__ == '__main__':
    main()