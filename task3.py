
#creates the necessary parsed data file
def main():
    #convertLabels("dataset/all_labels.txt")
    nb_classifier()


from sklearn.metrics import confusion_matrix

cum = confusion_matrix(y_test, y_pred)

from sklearn.metrics import confusion_matrix

cum = confusion_matrix(y_test, y_pred)

print(cum)

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

print(accuracy_score(y_test, y_pred)*100)   
print(precision_score(y_test, y_pred, average='weighted'))
print(recall_score(y_test, y_pred, average='weighted'))
print(f1_score(y_test, y_pred, average='weighted'))