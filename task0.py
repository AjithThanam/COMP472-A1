import re

#creates the necessary parsed data file
def main():
    raw_dataset = 'dataset/all_sentiment_shuffled.txt'
    filter_dataset(raw_dataset)
    seperate_dataset("dataset/all_sentiment_shuffled_filtered.txt",count_lines(raw_dataset))
    
#returns the number of lines in a give file (Primarily for the raw dataset)
def count_lines(filepath):
    lines = 0

    with open(filepath, encoding="utf8") as f:
        for line in f:
            lines = lines + 1
    
    return lines

#Parses the raw dataset and creates a new file without the:
# - document identifier --> xxx.txt
# - the topic label --> music, books, camera etc..
def filter_dataset(filepath):
    new_file = open("dataset/all_sentiment_shuffled_filtered.txt","w+")

    with open(filepath, encoding="utf8") as f:
        for line in f:
            line = line.split(' ', 1)[1]
            line = re.sub('\\b\d{1,3}\\b\.txt ', '', line)
            new_file.write(line)
    
    new_file.close()

#parses the filtered dataset and create two new text files:
# - the training_dataset which counts for 80% of the original set
# - the evaluation_dataset which counts for 20% of the original set
def seperate_dataset(filepath,num_lines):
    training_doc = open("dataset/training_dataset.txt","w+")
    evaluation_doc = open("dataset/evaluation_dataset.txt","w+")
    counter = 0

    with open(filepath) as f:
        for line in f:
            if(counter < int(num_lines*0.8)):
                training_doc.write(line)
            else:
                evaluation_doc.write(line)
            
            counter+=1
            
            

    training_doc.close()
    evaluation_doc.close()


if __name__ == '__main__':
    main()
    