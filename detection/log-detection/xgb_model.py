from xgboost.sklearn import XGBClassifier, XGBRegressor
from utility import *

args = get_args()
training_data = args['training_data']
testing_data = args['testing_data']


# Get training features and labeles
training_features, training_labels = get_data_details(training_data)

# Get testing features and labels
testing_features, testing_labels = get_data_details(testing_data)

print("\n XGB Regressor \n")

classifier = XGBClassifier(max_depth=7,
                           eta=0.3, subsample=1, use_label_encoder=True)
classifier.fit(training_features, training_labels)
pred = classifier.predict(testing_features)

print("The accuracy of the model is :" +
      str(get_accuracy(testing_labels, pred, 1))+"%")
