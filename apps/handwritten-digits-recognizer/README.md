<h1 align="center">
    Handwritten Digits Recognizer
</h1>


## Installation

First, clone the project `python-streamlit-apps` or run:

```
git clone https://github.com/amirhessam88/python-streamlit-apps.git
```

You need to make sure to have all the requirements instaleld on your system. So, you can simply run:

```
cd python-streamlit-apps
pip install -r requirements.txt 
```

Now, navigate to the Handwritten Digits Recognizer and run:

```
streamlit run app.py
```

## Notes:
- The [MNIST](http://yann.lecun.com/exdb/mnist/) database is used for training.
- The trained models are only some examples of deep/convolutional neural networks. The models did not go through the hyper-parameters tuning process. Additionally, the models are only trained for 25 epochs.
- The current models do have misclassification. Please note that, the MNIST database as the training data is a perfect database and does not cover all possible handwritten digits. For instance, rotated MNIST or any augmentation on top of the MNIST data can decrease the chance of misclassification in addition to improving the models themselves.
- Transfer learning can be another choice.
