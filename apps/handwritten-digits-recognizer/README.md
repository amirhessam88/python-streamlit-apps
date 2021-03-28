<h1 align="center">
    Diabetes Risk Predictor
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

Now, navigate to the Diabetes Risk Predictor and run:

```
streamlit run app.py
```

## Notes:
- The training dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. The objective of the dataset is to diagnostically predict whether or not a patient has diabetes, based on certain diagnostic measurements included in the dataset. Several constraints were placed on the selection of these instances from a larger database. In particular, all patients here are females at least 21 years old of Pima Indian heritage. More details are available in [Kaggle](https://www.kaggle.com/uciml/pima-indians-diabetes-database) website.
- For the sake of training, XGBoost combined with Bayesian Optimization is used. The complete implementations of the used model/optimizer are available in [SlickML](https://github.com/slickml/slick-ml) library.
- The model will be trained (based on the test size) using learning API of XGBoostCV on number of cross-validation folds, validated on the test set, and predicts the user's input. As seen, the test size, the number of folds for cross validation, evaluation metric,  and user's input values can be passed dynamically.

