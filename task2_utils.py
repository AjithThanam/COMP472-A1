def main():
    seperateLabelsAndDocs("dataset/all_sentiment_shuffled_filtered.txt")
    convertLabels("dataset/all_labels.txt")

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

def convertLabels(filepath):
    converted_labels = open("dataset/converted_labels.txt","w+")

    with open(filepath) as f:
        for line in f:
            if "pos" in line:
                converted_labels.write("1\n")
            else:
                converted_labels.write("0\n")

if __name__ == '__main__':
    main()