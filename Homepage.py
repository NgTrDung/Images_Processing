import streamlit as st
import base64

st.set_page_config(
    page_title="Hello",
    page_icon=" ",
)

st.write("<h1 style='font-size: 50px;color:black'>Welcome to the website for Images Processing! </h1>", unsafe_allow_html=True)
st.sidebar.success("You can choose one of my projects above.")


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local("Background/Background.jpg")  
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #748A88;
    }
</style>
""", unsafe_allow_html=True)
  
st.markdown(
    """
    <style>
    .red-text {
        color: red;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.write('<div class="header">'
            '<p class="header-title">ĐỒ ÁN CUỐI KỲ XỬ LÝ ẢNH SỐ</p>'
        '</div>',
          unsafe_allow_html=True)
# st.write("# Mã lớp : DIPR430685_23_1_01")
st.write("## 21133021 - Nguyễn Trọng Dũng")
st.write("## Lớp chiều tối Thứ 4 - Mã lớp trên FHQX: DIPR430685_23_2_03")


st.markdown(
    """
    
    ## Sản phẩm
    #### Project cuối kỳ cho môn học XỬ LÝ ẢNH SỐ (DIPR430685).
    Thuộc Trường Đại Học Sư Phạm Kỹ Thuật TP.HCM do 
    **Th.S Trần Tiến Đức** hướng dẫn. 

    ### Đồ án gồm 6 chức năng cơ bản
    - 📖 1. Đếm số ngón tay
    - 📖 2. Nhận dạng 5 loại Thiết bị công nghệ thông tin và truyền thông (ITC Devices)
    - 📖 3. Nhận diện cảm xúc trên khuôn mặt (angry, disgust, fear, happy, neutral, sad, suprise)
    - 📖 4. Nhận dạng chữ số viết tay
    - 📖 5. Nhận diện khuôn mặt (5 người)
    - 📖 6. Xử lý ảnh

    ### Em đã thêm các chức năng:
    - 🍀 1. Đếm số ngón tay
    - 🍀 3. Nhận diện cảm xúc trên khuôn mặt (angry, disgust, fear, happy, neutral, sad, suprise)

    Đề tài và bài báo cáo được em thực hiện trong khoảng thời gian ngắn, với những kiến thức còn hạn chế cùng nhiều hạn chế khác về mặt kĩ thuật và kinh nghiệm trong việc thực hiện một dự án. Do đó, trong quá trình làm nên đề tài có những thiếu sót là điều không thể tránh khỏi nên em rất mong nhận được những ý kiến đóng góp quý báu của thầy để kiến thức của em được hoàn thiện hơn và chúng em có thể làm tốt hơn nữa trong những lần sau. Em xin chân thành cảm ơn. 
    """
)