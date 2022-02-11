import time

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title("Streamlit超入門")

#st.sidebar.write("サイドバー")

#ctrl+Dで選択してる文字列をドキュメント内で全部同時に選択状態にできる

st.write('プログレスバーの表示')
'Start!!'

#空の要素
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.01)

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write('ここは右カラムです')

expander = st.expander('問合せ')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')

# #スライダー
# slider = st.slider('slider info',0,100,50)
# 'slider:', slider

# #チェックボックス
# if st.checkbox('Show Image'):
#     st.write('Display Image')
#     #画像の出し方
#     img = Image.open('kouhaitou.jpg')
#     st.image(img, caption='学長高配当株リスト', use_column_width=True)



#セレクトボックスの表示
option = st.selectbox(
    'データを選択してください',
    ["bar_chart", "map", "code"]
)
'選択中のデータは', option, 'です'

#テキスト入力の表示
text = st.text_input("何か入力してください")
"入力された文字は", text, "です。"

#optionの選択値によって色々変えてみる
if option == "bar_chart":
    #データフレーム、グラフ表示
    st.write('DataFrame')

    df = pd.DataFrame(
        np.random.rand(20,3),
        columns = ['a','b', 'c']
    )

    st.write(df)

    st.dataframe(df.style.highlight_max(axis=0))

    st.bar_chart(df)

if option == "map":
    #map表示
    df = pd.DataFrame(
        np.random.rand(100, 2)/[50,50] + [35.69, 139.70],
        columns = ['latitude','longitude']
    )

    st.dataframe(df.style.highlight_max(axis=0))

    st.map(df)

if option == "code":
    #マジックコマンド？
    """

    # 章
    ## 節
    ### 項

    ```python
    import streamlit as st
    import numpy as np
    import pandas as pd
    ```
    """