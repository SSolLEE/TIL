import streamlit as st

# 마크다운 적용하기
st.markdown('Streamlit is **_really_ cool**.')
st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
st.markdown(':green[$\sqrt{x^2+y^2}=1$] is a Pythagorean iidentity. :pencil:')

# 타이틀, 헤더, 캡션
st.title('This is a :red[title]. :first_quarter_moon_with_face:')
st.header('A **header** with _italics_ :blue[colors] and emojis :mechanic:')
st.subheader('A subheader with :yellow[colors] and emoji :unicorn_face:')
st.caption("This is a string that *explains something* above.")

# 코드 입력
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

# text
st.text('Enjoy coding!')

# 수식
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

# 선 긋기
st.divider()
st.text("STARBUCKS")
st.write("---")