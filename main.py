from posixpath import expanduser
from numpy.lib.shape_base import column_stack
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit超入門')

st.write('Display progress bar')
'Start!!'

latest_iteration = st.empty()
bar  = st.progress(0)   

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!'

st.write('Interactive Widgets')

left_column, right_column = st.columns(2)
button = left_column.button('Display character in right column')
if button:
    right_column.write('Here is right column')

expander1 = st.expander('Inquire')
expander1.write('Write answer')
expander2 = st.expander('Inquire')
expander2.write('Write answer')
expander3 = st.expander('Inquire')
expander3.write('Write answer')

option = st.text_input('Tell me what you like?')

'You like', option

condition = st.slider('Your condition is',0,100,50)
# condition = st.sidebar.slider('Your condition is',0,100,50)

'condition', condition
# option = st.selectbox(
#     'Tell me the number you like?',
#     list(range(1,11))
# )

# 'The number you like is ', option
# if st.checkbox('Show Image'):
#     img = Image.open('/Users/gumjitatsuya/Downloads/kimetsu.jpeg')
#     st.image(img, caption='poster', use_column_width=True)









# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69,139.70],
#     columns=['lat','lon']
# )

# st.dataframe(df.style.highlight_max(axis=0),width=300,height=200)

# st.table(df.style.highlight_max(axis=0))

# st.map(df)

# """""
# # 1
# ## 2
# ### 3

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """

