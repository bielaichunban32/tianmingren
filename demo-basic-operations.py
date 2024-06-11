import streamlit as st
st.title("你好，天命人！")
st.header("8/20，中国人的首款3A大作即将上架，现在多个平台已经开启预售！！")
st.subheader("这款游戏已经在多次线下试玩中获得好评。")
st.text("下面是相关照片")

st.markdown("this is an image:\n \
             ![Alt text](https://gameplus-platform.cdn.bcebos.com/gameplus-platform/upload/file/source/c6b818a70001ec7eb0d97e2e4e7ce603.jpeg)", 
             unsafe_allow_html=True)

st.subheader("来做一个小测试，看看你是否会喜欢这款游戏吧。")

status = st.radio("由于该款游戏存在年龄限制，请选择你的年龄:" ,
                  ('未满十八岁',
                   '已满十八岁'))
if status == '未满十八岁':
    st.success("child")
else:
    st.success("adult")

hobbies = st.multiselect("以下游戏你曾玩过哪些:",
               ['原神',
                '永劫无间',
                '艾尔登法环',
                '只狼',
               '以上都没玩过'])

if hobbies == ['以上都没玩过']:
    st.warning("根据你的选择，你可能不太适合这款游戏。")
else:
    st.success("根据你的游戏经历，你适合体验这款游戏。")






    