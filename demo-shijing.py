import streamlit as st
st.title("Hello, 天津")
st.header("You need to learn some basic operations")
st.subheader("eg, Python")
st.text("It's undemanding")

st.markdown("this is an image: \n \
            ![](https://tse3-mm.cn.bing.net/th/id/OIP-C.zH_E9xuU74TTBsIUmSoRhQHaEo?rs=1&pid=ImgDetMain)")

if st.checkbox("查看更多"):
    st.text("已选中复选框来查看更多")


gender = st.radio("请选择你的性别:", ('男', '女', '其他'))
if gender == '男':  
    st.success("你选择了男性")  
elif gender == '女':  
    st.success("你选择了女性")  
else:  
    st.success("你选择了其他")

hobbies = st.multiselect("Hobbies:",
               ['Sports',
                'Cooking',
                'Coding',
                'Traveling'])
st.write("You selected: ", hobbies)

if st.button("关于"):
    st.text("Streamlit is a great tool")

name = st.text_input("请输入你的姓名:")
if st.button("Submit"):
    st.write("Hello, ", name)

level = st.slider("Select your level", 1, 5)
st.write("You selected: ", level)


    