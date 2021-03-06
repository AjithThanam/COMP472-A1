import matplotlib.pyplot as plt


#main method
def main():
    count_responses()
    
#Method will count responses of each type found in the filtered file
#The numerical value of the results are then displayed onto the console
#Then the results are displayed onto a bar chart
def count_responses():
    negative_response = 0
    positive_response = 0
    with open('dataset/all_sentiment_shuffled_filtered.txt', 'r') as f:
        for line in f:
            if "neg" in line:
                negative_response +=1
            elif "pos" in line:
                positive_response +=1

    print("Number of negative responses:",  negative_response)
    print("Number of positive responses:",  positive_response)

    responses = ['Negative', 'Positive']
    numOfResp = [negative_response, positive_response]
    colors = ["red", "green"]

    plt.bar(responses, numOfResp, color=colors)
    plt.title("Positive vs Negative Responses", fontsize=16)
    plt.xlabel("Responses", fontsize=14)
    plt.ylabel("Number of Responses", fontsize=14)
    plt.show()   



if __name__ == "__main__":
    main()