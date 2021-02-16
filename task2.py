from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import tree
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report

def main():
    nb_classifier()
    base_dt()
    best_dt()

def nb_classifier():
    converted_labels = open("dataset/converted_labels.txt","r")
    all_docs = open("dataset/all_docs.txt","r")
    converted_array = converted_labels.read().split("\n")
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(all_docs)
    X_train, X_test, y_train, y_test = train_test_split(X, converted_array, test_size=0.2, random_state=0)
    gnb = MultinomialNB()
    y_pred = gnb.fit(X_train, y_train).predict(X_test)
    print("Number of mislabeled points for Naive Bayes (total %d) : %d" % (X_test.shape[0], (y_test != y_pred).sum()))

def base_dt():
    converted_labels = open("dataset/converted_labels.txt","r")
    all_docs = open("dataset/all_docs.txt","r")
    converted_array = converted_labels.read().split("\n")
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(all_docs)
    X_train, X_test, y_train, y_test = train_test_split(X, converted_array, test_size=0.2, random_state=0)
    clf = tree.DecisionTreeClassifier(criterion="entropy")
    y_pred = clf.fit(X_train, y_train).predict(X_test)
    print("Number of mislabeled points for Base DT (total %d) : %d" % (X_test.shape[0], (y_test != y_pred).sum()))

def best_dt():
    converted_labels = open("dataset/converted_labels.txt","r")
    all_docs = open("dataset/all_docs.txt","r")
    converted_array = converted_labels.read().split("\n")
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(all_docs)
    X_train, X_test, y_train, y_test = train_test_split(X, converted_array, test_size=0.2, random_state=0)
    clf = tree.DecisionTreeClassifier()
    y_pred = clf.fit(X_train, y_train).predict(X_test)
    print("Number of mislabeled points for Best DT (total %d) : %d" % (X_test.shape[0], (y_test != y_pred).sum()))

if __name__ == '__main__':
    main()