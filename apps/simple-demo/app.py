# Simple Streamlit API Demo

# -------------------------------------------
# loading libraries
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import time, datetime
import altair as alt
import plotly.figure_factory as ff
import graphviz as graphviz
import urllib.request

st.markdown(
    "<h1 style='text-align: center; color: black;'>LIVE DEMO</h1>",
    unsafe_allow_html=True,
)
# -------------------------------------------


# # -------------------------------------------
# # DISPLAY TEXT
# # -------------------------------------------
# st.title("DISPLAY TEXT")
# st.text("Fixed width text")
# st.markdown("_Markdown_")
# st.latex(r""" e^{i\pi} + 1 = 0 """)
# st.write("Most objects")
# st.write(["st", "is <", 3])
# st.title("My title")
# st.header("My header")
# st.subheader("My sub")
# st.code("for i in range(8): foo()")
# # -------------------------------------------


# # -------------------------------------------
# # DISPLAY DATA
# # -------------------------------------------
# st.title("DISPLAY DATA")
# df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})

# st.dataframe(df)
# st.table(df.iloc[0:1])
# st.json({"foo": "bar", "fu": "ba"})
# # -------------------------------------------


# # # -------------------------------------------
# # # DISPLAY MEDIA
# # # -------------------------------------------
# # image
# # st.image('./assets/myimage.png')
# st.image("apps/simple-demo/assets/myimage.png")
# # # -------------------------------------------
# # audio
# # audio_file = open('./assets/myaudio.ogg', 'rb')
# audio_file = open("apps/simple-demo/assets/myaudio.ogg", "rb")
# audio_bytes = audio_file.read()
# st.audio(audio_bytes, format="audio/ogg")
# # # -------------------------------------------
# # video
# # video_file = open('./assets/myvideo.mp4', 'rb')
# video_file = open("apps/simple-demo/assets/myvideo.mp4", "rb")
# video_bytes = video_file.read()
# st.video(video_bytes)
# # # -------------------------------------------


# -------------------------------------------
# LINE CHART
# -------------------------------------------
# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
# if st.checkbox("Show dataframe"):
#     chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
#     chart_data

# default charts
# st.line_chart(chart_data)
# st.area_chart(chart_data)
# st.bar_chart(chart_data)


# matplotlib
# arr = np.random.normal(1, 1, size=100)
# fig, ax = plt.subplots()
# ax.hist(arr, bins=20, color="darkgreen")
# st.pyplot(fig)


# # altair
# c = (
#     alt.Chart(chart_data)
#     .mark_circle()
#     .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
# )
# st.altair_chart(c, use_container_width=True)


# # plotly

# # add histogram data
# x1 = np.random.randn(200) - 2
# x2 = np.random.randn(200)
# x3 = np.random.randn(200) + 2

# # Group data together
# hist_data = [x1, x2, x3]

# group_labels = ["Group 1", "Group 2", "Group 3"]

# # Create distplot with custom bin_size
# fig = ff.create_distplot(hist_data, group_labels, bin_size=[0.1, 0.25, 0.5])

# # Plot!
# st.plotly_chart(fig, use_container_width=True)


# # graphviz
# st.graphviz_chart(
#     """
#     digraph {
#         run -> intr
#         intr -> runbl
#         runbl -> run
#         run -> kernel
#         kernel -> zombie
#         kernel -> sleep
#         kernel -> runmem
#         sleep -> swap
#         swap -> runswap
#         runswap -> new
#         runswap -> runmem
#         new -> runmem
#         sleep -> runmem}
# """
# )

# # map
# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=["lat", "lon"]
# )

# st.map(map_data)

# # -------------------------------------------


# # WIDGETS BEGIN

# # -------------------------------------------
# # BUTTON
# # -------------------------------------------
# if st.button("Hit Me"):
#     st.write("Respond after Hit")
# else:
#     st.write("Respond before Hit")
# # -------------------------------------------


# # -------------------------------------------
# # CHECKBOX
# # -------------------------------------------
# agree = st.sidebar.checkbox("I agree")
# if agree:
#     st.write("Great!")
# # -------------------------------------------


# # -------------------------------------------
# # RADIO
# # -------------------------------------------
# genre = st.radio("What's your favorite movie genre", ("Comedy", "Drama", "Documentary"))

# if genre == "Comedy":
#     st.write("You selected comedy.")
# else:
#     st.write("You didn't select comedy.")
# # -------------------------------------------


# # -------------------------------------------
# # SELECTBOX
# # st.selectbox(label,
# #              options,
# #              index=0,
# #              format_func=<class 'str'>,
# #              key=None,
# #              help=None)
# # -------------------------------------------
# option = st.sidebar.selectbox(
#     "How would you like to be contacted?", ("Email", "Home phone", "Mobile phone")
# )
# st.write("You selected:", option)
# # -------------------------------------------


# # -------------------------------------------
# # MULTISELECT
# # st.multiselect(label,
# #                options,
# #                default=None,
# #                format_func=<class 'str'>,
# #                key=None,
# #                help=None)
# # -------------------------------------------
# options = st.multiselect(
#     "What are your favorite colors", ["Green", "Yellow", "Red", "Blue"]
# )
# st.write("You selected:", options)
# # -------------------------------------------


# # -------------------------------------------
# # SLIDER
# # st.slider(label,
# #           min_value=None,
# #           max_value=None,
# #           value=None,
# #           step=None,
# #           format=None,
# #           key=None,
# #           help=None)
# # -----------------------------------------
# age = st.slider("How old are you?", 0.0, 130.0, 25.0)
# st.write("I'm ", age, "years old")

# st.title("OR")

# appointment = st.slider(
#     "Schedule your appointment:", value=(datetime.time(9, 30), datetime.time(12, 45))
# )
# st.write("You're scheduled for:", appointment)
# # -------------------------------------------


# # -------------------------------------------
# # SELECTSLIDER
# # st.select_slider(label,
# #                  options=[],
# #                  value=None,
# #                  format_func=<class 'str'>,
# #                  key=None,
# #                  help=None)
# # -----------------------------------------
# start_color, end_color = st.select_slider(
#     "Select a range of color wavelength",
#     options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
#     value=("red", "blue"),
# )
# st.write("You selected wavelengths between", start_color, "and", end_color)
# # -------------------------------------------


# # -------------------------------------------
# # TEXT INPUT/DATE/TIME
# # st.ext_input(label,
# #              value='',
# #              max_chars=None,
# #              key=None,
# #              type='default',
# #              help=None)
# # -----------------------------------------
# user = st.text_input("Enter your name: ")
# st.write(f"{user} just logged in!")

# d = st.date_input("Date of Birth", datetime.date(1988, 4, 13))
# st.write("Your birthday is:", d)

# t = st.time_input("Set appoitment for", datetime.time(8, 45))
# st.write("Appoitment is set for", t)
# # -------------------------------------------


# -------------------------------------------
# DISPLAY MISC.
# -------------------------------------------

color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", color)


latest_iteration = st.empty()
bar = st.progress(0)
for i in range(11):
    latest_iteration.text(f"Iteration {i}")
    bar.progress(i * 10)
    time.sleep(0.2)

st.spinner()
with st.spinner(text="In progress"):
    time.sleep(2)
    st.success("Done")

st.error("Error message")
st.warning("Warning message")
st.info("Info message")
st.success("Success message")

st.balloons()
# -------------------------------------------
