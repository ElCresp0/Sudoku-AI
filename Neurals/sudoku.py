#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import copy

import keras
import numpy as np

from model import get_model
from scripts.data_preprocess import get_data
from scripts.validate_solution import correct_sudoku, mistakes_made_sudoku

# ## Load the data
x_train, x_test, y_train, y_test = get_data('sudoku_multiple_solutions.csv')

# ## Train your own Model
#
# model = get_model()
#
# adam = keras.optimizers.Adam(learning_rate=.001)
# model.compile(loss='sparse_categorical_crossentropy', optimizer=adam)
#
# model.fit(x_train, y_train, batch_size=20, epochs=3)
#
# ## Load pretrained model

# model = keras.models.load_model('model/sudoku.model')
model = keras.models.load_model('my_model_51')


# ## Solve Sudoku by filling blank positions one by one

def norm(a):
    return (a / 9) - .5


def denorm(a):
    return (a + .5) * 9


def inference_sudoku(sample):
    feat = copy.copy(sample)

    while (1):

        out = model.predict(feat.reshape((1, 9, 9, 1)))
        out = out.squeeze()

        pred = np.argmax(out, axis=1).reshape((9, 9)) + 1
        prob = np.around(np.max(out, axis=1).reshape((9, 9)), 2)

        feat = denorm(feat).reshape((9, 9))
        mask = (feat == 0)

        if (mask.sum() == 0):
            break

        prob_new = prob * mask

        ind = np.argmax(prob_new)
        x, y = (ind // 9), (ind % 9)

        val = pred[x][y]
        feat[x][y] = val
        feat = norm(feat)

    return pred


# ## Testing 100 games

def test_accuracy(feats, labels):
    correct = 0
    mistakes = 0
    for i, feat in enumerate(feats):

        pred = inference_sudoku(feat)

        true = labels[i].reshape((9, 9)) + 1
        if (abs(true - pred).sum() == 0):
            correct += 1
        elif correct_sudoku(pred):
            correct += 1
        else:
            mistakes += mistakes_made_sudoku(pred)
    print(str(correct / feats.shape[0] * 100) + '% Accuracy')
    print(str(mistakes / feats.shape[0]) + ' Mistakes made on average')


test_accuracy(x_test[:1000], y_test[:1000])


# ## Test your own game


def solve_sudoku(game):
    game = game.replace('\n', '')
    game = game.replace(' ', '')
    game = np.array([int(j) for j in game]).reshape((9, 9, 1))
    game = norm(game)
    game = inference_sudoku(game)
    return game


print("For 1000 games")
# game = '''
#           0 8 0 0 3 2 0 0 1
#           7 0 3 0 8 0 0 0 2
#           5 0 0 0 0 7 0 3 0
#           0 5 0 0 0 1 9 7 0
#           6 0 0 7 0 9 0 0 8
#           0 4 7 2 0 0 0 5 0
#           0 2 0 6 0 0 0 0 9
#           8 0 0 0 9 0 3 0 5
#           3 0 0 8 2 0 0 1 0
#       '''
#
# game = solve_sudoku(game)
#
# print('solved puzzle:\n')
# print(game)
#
# model.save("my_model")
