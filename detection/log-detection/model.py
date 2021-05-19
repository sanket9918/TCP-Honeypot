from utility import *

args = get_args()
training_data = args['training_data']
testing_data = args['testing_data']

# Get training features and labeles
training_features, training_labels = get_data_details(training_data)

# Get testing features and labels
testing_features, testing_labels = get_data_details(testing_data)

# LOGISTIC REGRESSION CLASSIFIER
print("\n\nLogistic Regression Classifier\n")

attack_classifier = linear_model.LogisticRegression(C=1e5)
attack_classifier.fit(training_features, training_labels)

predictions = attack_classifier.predict(testing_features)
print("The precision of the Logistic Regression Classifier is: " +
      str(get_accuracy(testing_labels, predictions, 1)) + "%")

print("\n\nDecision Tree Classifier\n")
attack_classifier1 = tree.DecisionTreeClassifier(random_state=42)
attack_classifier1.fit(training_features, training_labels)
predictions1 = attack_classifier1.predict(testing_features)
print("The precision of the Decision Tree Classifier is: " +
      str(get_accuracy(testing_labels, predictions1, 1)) + "%")
