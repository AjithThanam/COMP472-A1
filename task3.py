from task2 import nb_classifier
from task2 import base_dt
from task2 import best_dt
from task2 import get_y_test
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix

def main():
    create_report(get_y_test(),nb_classifier(),"naive_bayes")
    create_report(get_y_test(),base_dt(),"base_dt")
    create_report(get_y_test(),best_dt(),"best_dt")
    
def create_report(y_test,y_pred, filename):
    new_file = open("dataset/task3_reports/"+filename+".txt","w+")
    
    for idx, val in enumerate(y_pred):
        if(int(val) == 0):
            new_file.write(str(idx) + ", neg\n")
        else:
            new_file.write(str(idx) + ", pos\n")
    
    new_file.write("\n\n")
    new_file.write("**********************************************************\n")
    new_file.write("The following are the relevant metrics for this classifier\n")
    new_file.write("**********************************************************\n")
    new_file.write("Confusion Matrix: \n")
    new_file.write(str(confusion_matrix(y_test, y_pred))+ "\n")
    new_file.write("Precision Score (Weighted Average): " + str(precision_score(y_test, y_pred, average='weighted'))+ "\n")
    new_file.write("Recall Score (Weighted Average): " + str(recall_score(y_test, y_pred, average='weighted'))+ "\n")
    new_file.write("F1 Score (Weighted Average): " + str(f1_score(y_test, y_pred, average='weighted'))+ "\n")
    new_file.write("Accuracy Score: " + str(accuracy_score(y_test, y_pred)*100) + "\n")
    new_file.write("**********************************************************"+ "\n")  
    
    new_file.close()
    

if __name__ == '__main__':
    main()