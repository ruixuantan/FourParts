from fourparts import KeyClassifier
import pandas as pd
from sklearn.neural_network import MLPClassifier

data_input = "Insert path to training data here"
data = pd.read_csv(data_input)
model = MLPClassifier(solver='sgd', alpha=1e-5,
                      hidden_layer_sizes=(15,), random_state=1)

kc = KeyClassifier(model)
res = kc.test_train(data, test_size=0.2)
print(res)

predict = "insert path to prediction sample here"
idx_list = kc.predict_midi(predict)
key_list = KeyClassifier.convert_to_key(idx_list)
print(key_list[0])
