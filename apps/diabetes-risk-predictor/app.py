# Amirhessam Tahmassebi
# March-06-2021
# Diabetes Risk Predictor

# loading libraries
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import seaborn as sns
from sklearn.model_selection import train_test_split
from slickml.classification import XGBoostCVClassifier
from slickml.optimization import XGBoostClassifierBayesianOpt
from slickml.metrics import BinaryClassificationMetrics
import urllib.request


# handling warnings
st.set_option("deprecation.showPyplotGlobalUse", False)


# title
st.markdown(
    "<h1 style='text-align: center; color: black;'>Diabetes Risk Predictor</h1>",
    unsafe_allow_html=True,
)

IMAGE_URL = "https://raw.githubusercontent.com/amirhessam88/python-streamlit-apps/master/apps/diabetes-risk-predictor/assets/design/header.jpg"
img_header = Image.open(urllib.request.urlopen(IMAGE_URL))
st.image(img_header, use_column_width=True)

# subheader
st.subheader(
    """DISCLAIMER: The training dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. The objective of the dataset is to diagnostically predict whether or not a patient has diabetes, based on certain diagnostic measurements included in the dataset. However, several constraints were placed on the selection of these instances from a larger database. In particular, all patients here are females at least 21 years old of Pima Indian heritage."""
)

# subheader
st.subheader(
    """NOTE: Users can see their Diabetes Risk Prediction by putting their inputs on the left panel. The features and their measurement units are explained in the data description section."""
)


# load data + cache
@st.cache
def get_data():
    """
    Returns data as pandas DataFrame()
    """
    DATA_URL = "https://raw.githubusercontent.com/amirhessam88/python-streamlit-apps/master/apps/diabetes-risk-predictor/assets/data/data.csv"
    df = pd.read_csv(DATA_URL)

    return df


df = get_data()

# data description
st.markdown(
    "<h2 style='text-align: left; color: black;'>Data Description</h2>",
    unsafe_allow_html=True,
)
st.json(
    {
        "Pregnancies": "Number of times pregnant",
        "Glucose": "Plasma glucose concentration a 2 hours in an oral glucose tolerance test",
        "BloodPressure": "Diastolic blood pressure (mm Hg)",
        "SkinThickness": "Triceps skin fold thickness (mm)",
        "Insulin": "2-Hour serum insulin (mu U/ml)",
        "BMI": "Body mass index (weight in kg/(height in m)^2)",
        "DiabetesPedigreeFunction": "Diabetes pedigree function",
        "Age": "Age (years)",
        "Outcome": "Class variable (0 as non-diabetic or 1 as diabetic)",
    }
)

# data summary stats# data summary stats# data summary stats
st.markdown(
    "<h2 style='text-align: left; color: black;'>Data Summary</h2>",
    unsafe_allow_html=True,
)

st.write("Shape of Data: ", df.shape)
st.write("Number of Classes: ", df["Outcome"].nunique())
st.write("Prevalence: ", np.round(df["Outcome"].sum() / df.shape[0] * 100, 2), "%")
st.write("Raw Data")
st.dataframe(df)
st.write("Descriptive Statistics")
st.write(df.describe(include="all"))


# plot histograms
def plot_hist(df):
    """
    Plots histograms of the features with kernel density estimation
    """
    mapping = {1: "Diabetic", 0: "Non-Diabetic"}
    tmp = df.copy()
    tmp["Outcome"] = tmp["Outcome"].map(mapping)
    fig, axs = plt.subplots(2, 4, figsize=(20, 12))
    sns.histplot(
        data=tmp,
        x="Pregnancies",
        hue="Outcome",
        multiple="dodge",
        kde=True,
        color="skyblue",
        ax=axs[0, 0],
    )
    sns.histplot(
        data=tmp,
        x="Glucose",
        hue="Outcome",
        multiple="dodge",
        kde=True,
        color="olive",
        ax=axs[0, 1],
    )
    sns.histplot(
        data=tmp,
        x="BloodPressure",
        hue="Outcome",
        multiple="dodge",
        kde=True,
        color="gold",
        ax=axs[0, 2],
    )
    sns.histplot(
        data=tmp,
        x="SkinThickness",
        hue="Outcome",
        multiple="dodge",
        kde=True,
        color="teal",
        ax=axs[0, 3],
    )
    sns.histplot(
        data=tmp,
        x="Insulin",
        hue="Outcome",
        multiple="dodge",
        kde=True,
        color="skyblue",
        ax=axs[1, 0],
    )
    sns.histplot(
        data=tmp,
        x="BMI",
        hue="Outcome",
        multiple="dodge",
        kde=True,
        color="olive",
        ax=axs[1, 1],
    )
    sns.histplot(
        data=tmp,
        x="DiabetesPedigreeFunction",
        hue="Outcome",
        multiple="dodge",
        kde=True,
        color="gold",
        ax=axs[1, 2],
    )
    sns.histplot(
        data=tmp,
        x="Age",
        hue="Outcome",
        multiple="dodge",
        kde=True,
        color="teal",
        ax=axs[1, 3],
    )

    st.pyplot()


# st.write("Histogram Plots")
# plot_hist(df)

# nfolds cv
nfolds = st.sidebar.slider("N-Folds Cross-Validation (Train)", 0, 10, 4)

# test size slider
test_size = st.sidebar.slider("Validation Data Size (Test)", 0.0, 1.0, 0.2)

# training metrics
metric = st.sidebar.selectbox("Metric", ("AUC", "AUCPR", "LOGLOSS", "ERROR"))


# getting feature input from user
def get_user_input():
    """
    Returns the user inputs to predict risk
    """
    Pregnancies = st.sidebar.slider(
        "Pregnancies",
        int(df["Pregnancies"].min()),
        int(df["Pregnancies"].max()),
        int(df["Pregnancies"].median()),
    )
    Glucose = st.sidebar.slider(
        "Glucose",
        int(df["Glucose"].min()),
        int(df["Glucose"].max()),
        int(df["Glucose"].median()),
    )
    BloodPressure = st.sidebar.slider(
        "BloodPressure",
        int(df["BloodPressure"].min()),
        int(df["BloodPressure"].max()),
        int(df["BloodPressure"].median()),
    )
    SkinThickness = st.sidebar.slider(
        "SkinThickness",
        int(df["SkinThickness"].min()),
        int(df["SkinThickness"].max()),
        int(df["SkinThickness"].median()),
    )
    Insulin = st.sidebar.slider(
        "Insulin",
        int(df["Insulin"].min()),
        int(df["Insulin"].max()),
        int(df["Insulin"].median()),
    )
    BMI = st.sidebar.slider(
        "BMI", int(df["BMI"].min()), int(df["BMI"].max()), int(df["BMI"].median())
    )
    DiabetesPedigreeFunction = st.sidebar.slider(
        "DiabetesPedigreeFunction",
        int(df["DiabetesPedigreeFunction"].min()),
        int(df["DiabetesPedigreeFunction"].max()),
        int(df["DiabetesPedigreeFunction"].median()),
    )
    Age = st.sidebar.slider(
        "Age", int(df["Age"].min()), int(df["Age"].max()), int(df["Age"].median())
    )

    user_input = {
        "Pregnancies": Pregnancies,
        "Glucose": Glucose,
        "BloodPressure": BloodPressure,
        "SkinThickness": SkinThickness,
        "Insulin": Insulin,
        "BMI": BMI,
        "DiabetesPedigreeFunction": DiabetesPedigreeFunction,
        "Age": Age,
    }

    return pd.DataFrame(user_input, index=[0])


# get user's inputs
df_user_input = get_user_input()

# model training
st.markdown(
    "<h2 style='text-align: left; color: black;'>Model Development</h2>",
    unsafe_allow_html=True,
)


# train/test splits
def get_train_test_splits(df, test_size):
    """
    Returns stratified train/test splits
    """
    y = df["Outcome"].values
    X = df.drop(["Outcome"], axis=1)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, shuffle=True, stratify=y, random_state=1367
    )

    return X_train, X_test, y_train, y_test


# get train/test splits
X_train, X_test, y_train, y_test = get_train_test_splits(df, test_size)

st.write("Training Data Shape: ", X_train.shape)
st.write("Training Prevalence: ", np.round(y_train.sum() / len(y_train) * 100, 2), "%")
st.write("Testing Data Shape: ", X_test.shape)
st.write("Testing Prevalence: ", np.round(y_test.sum() / len(y_test) * 100, 2), "%")


# bayesian optimization for best params
st.write("XGBoost Parameters Tuning via Bayesian Optimization")
xbo = XGBoostClassifierBayesianOpt(n_splits=nfolds)
xbo.fit(X_train, y_train)
xbo_results = xbo.get_optimization_results()
best_params = xbo.get_best_params()
st.write("Bayesian Optimization Results")
st.dataframe(xbo_results)
st.write("Best Parameters")
st.json(best_params)

# train using best params
clf = XGBoostCVClassifier(params=best_params, n_splits=nfolds, metrics=(metric.lower()))
clf.fit(X_train, y_train)

# prediction on test set
y_pred_proba = clf.predict_proba(X_test, y_test)

# plot cv results using metric
st.write("N-Folds Cross-Validation Evolution")
clf.plot_cv_results()
st.pyplot()

# plot  features importance
st.write("Feature Importance")
clf.plot_feature_importance()
st.pyplot()

st.markdown(
    "<h2 style='text-align: left; color: black;'>Model Validation</h2>",
    unsafe_allow_html=True,
)

# plot SHAP summary plot
st.write("SHAP Layered Violin Summary Plot on Test Data")
clf.plot_shap_summary(plot_type="layered_violin", layered_violin_max_num_bins=5)
st.pyplot()

# plot SHAP waterfall plot
st.write("SHAP WaterFall Plot on Test Data")
clf.plot_shap_waterfall()
st.pyplot()

# plot binary metrics
st.write("Model Performance on Test Data")
clf_metrics = BinaryClassificationMetrics(y_test, y_pred_proba)

# metrics dataframe
st.dataframe(clf_metrics.metrics_df_)

# metrics plots
clf_metrics.plot()
st.pyplot()

st.markdown(
    "<h2 style='text-align: left; color: black;'>User's Diabetes Risk Prediction</h2>",
    unsafe_allow_html=True,
)

# user input prediction
st.write("User's Inputs")
st.dataframe(df_user_input)

user_proba = clf.predict_proba(df_user_input)
user_risk = np.round(user_proba[0] * 100, 2)
st.write("User's Diabetes Risk Prediction: ", user_risk, "%")


# create class based on risk prediction for different thresholds
def prediction_class(clf_metrics, user_risk):
    """
    Function to define prediction class based on threshold
    """
    # getting thresholds dict
    thresholds_dict = clf_metrics.thresholds_dict_
    methods = []
    thresholds = []
    classes = []
    for method, threshold in thresholds_dict.items():
        methods.append(method)
        thresh = np.round(threshold * 100, 2)
        thresholds.append(thresh)
        if user_risk >= thresh:
            classes.append("Diabetic")
        else:
            classes.append("Non-Diabetic")

    data = {
        "Threshold Method": methods,
        "Threshold (%)": thresholds,
        "Prediction Class": classes,
    }

    return pd.DataFrame(data)


# user input class prediction
df_user_class = prediction_class(clf_metrics, user_risk)
st.write("Prediction Class Based on Multiple Thresholds")
st.dataframe(df_user_class)
