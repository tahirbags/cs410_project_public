from sklearn.tree import DecisionTreeClassifier

class DecisionTreeClassifierModel:
  """
  A class used to represent a Decision Tree Classifier model

  Attributes
  ----------
  model :
      an instance of the DecisionTreeClassifier Class from scikit-learn

  Methods
  -------
  train(X_train, y_train)
      Trains the model using given training data
  predict(X_test)
      Predicts labels for given test data
  """

  def __init__(self):
    """
      Hyperparameter selection:
      List of parameters that can be tuned:
      dict_keys(['ccp_alpha', 'class_weight', 'criterion', 'max_depth', 'max_features', 'max_leaf_nodes', 
      'min_impurity_decrease', 'min_impurity_split', 'min_samples_leaf', 'min_samples_split', 'min_weight_fraction_leaf', 
      'random_state', 'splitter'])
    """
    self.model = DecisionTreeClassifier(max_depth=5, random_state=42)

  def train(self, X_train, y_train):
    self.model.fit(X_train, y_train)

  def predict(self, X_test):
    return self.model.predict(X_test)
