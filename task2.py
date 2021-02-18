from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import tree
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report

def main():
    X_train, X_test, y_train, y_test = get_train_test()
    nb_classifier(X_train, X_test, y_train, y_test)
    base_dt(X_train, X_test, y_train, y_test)
    best_dt(X_train, X_test, y_train, y_test)

def nb_classifier(X_train, X_test, y_train, y_test):
    gnb = MultinomialNB()
    y_pred = gnb.fit(X_train, y_train).predict(X_test)
    #Commented out for the time being as we technically dont need this print for this task
    print("Number of mislabeled points for Naive Bayes (total %d) : %d" % (X_test.shape[0], (y_test != y_pred).sum()))
    return y_pred

def base_dt(X_train, X_test, y_train, y_test):
    clf = tree.DecisionTreeClassifier(criterion="entropy")
    y_pred = clf.fit(X_train, y_train).predict(X_test)
    #Commented out for the time being as we technically dont need this print for this task
    print("Number of mislabeled points for Base DT (total %d) : %d" % (X_test.shape[0], (y_test != y_pred).sum()))
    return y_pred

def best_dt(X_train, X_test, y_train, y_test):
    clf = tree.DecisionTreeClassifier()
    y_pred = clf.fit(X_train, y_train).predict(X_test)
    #Commented out for the time being as we technically dont need this print for this task
    print("Number of mislabeled points for Best DT (total %d) : %d" % (X_test.shape[0], (y_test != y_pred).sum()))
    return y_pred


def get_y_test():
    converted_labels = open("dataset/converted_labels.txt","r")
    all_docs = open("dataset/all_docs.txt","r")
    converted_array = converted_labels.read().split("\n")
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(all_docs)
    X_train, X_test, y_train, y_test = train_test_split(X, converted_array, test_size=0.2, random_state=0)
    return y_test

def get_train_test():
    converted_labels = open("dataset/converted_labels.txt","r")
    all_docs = open("dataset/all_docs.txt","r")
    converted_array = converted_labels.read().split("\n")
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(all_docs)
    X_train, X_test, y_train, y_test = train_test_split(X, converted_array, test_size=0.2, random_state=0)
    return X_train, X_test, y_train, y_test

if __name__ == '__main__':
    main()