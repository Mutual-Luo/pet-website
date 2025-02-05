import streamlit as st
import pandas as pd
from datetime import datetime

st.markdown("<h1 style='text-align: center;'>添加爱宠🐇信息</h1>", unsafe_allow_html=True)

# Pet 
st.markdown("<h3>爱宠信息</h3>", unsafe_allow_html=True)
pet_name = st.text_input("宠物昵称")
pet_gender = st.radio("性别", ['公', '母'])
pet_age = st.text_input("年龄")
pet_type = st.text_input("品种")
pet_birth = st.date_input("生日", min_value=None, max_value=None)
pet_deadth = st.date_input("逝日", min_value=None, max_value=None)
pet_message = st.text_area("最想对Ta说的话")

# Owner
st.markdown("<h3>家长信息</h3>", unsafe_allow_html=True)
owner_name = st.text_input("家长姓名")
owner_gender = st.radio("性别", ['先生', '女士'])
owner_phone = st.text_input("联系方式")
owner_area = st.text_input("居住区域")
owner_find = st.text_input("通过哪种方式找到光予生命")
owner_keywords = st.text_input("搜索关键词")

# Sevice
st.markdown("<h3>服务明细</h3>", unsafe_allow_html=True)
service_weight = st.text_input("善后体重")
service_fee = st.text_input("费用")
service_type = st.text_input("套餐类型")
service_bone = st.text_input("骨灰盒")
service_souvenir = st.text_input("纪念品")
service_charge = st.text_input("负责人")
service_sum = st.text_input("总计")
service_payment = st.radio("支付方式", ['支付宝/微信', '淘宝', '现金', '其他'])


# Note
st.markdown("<h3>善后备注</h3>", unsafe_allow_html=True)
note_photo = st.radio("纪念照留取", ['是', '否'])
note_video = st.radio("火化视频留取", ['是', '否'])
note_bone = st.radio("骨灰领取方式", ['自取', '闪送到付', '届时沟通'])
note_memorial = st.radio("纪念品领取方式", ['自取', '闪送到付', '届时沟通'])
note_belonging = st.radio("爱宠随身物品", ['已交接', '待处理'])
note_message = st.text_area("其他备注")

# Submit
submit_button = st.button("提交")


# Save
if submit_button:
    data = {
        "宠物昵称": pet_name or '',
        "性别（宠物)": pet_gender or '',
        "年龄": pet_age or '',
        "品种": pet_type or '',
        "生日": pet_birth.strftime('%Y-%m-%d') if pet_birth else '',
        "逝日": pet_deadth.strftime('%Y-%m-%d') if pet_deadth else '',
        "最想对Ta说的话": pet_message or '',
        "家长姓名": owner_name or '',
        "性别（家长)": owner_gender or '',
        "联系方式": owner_phone or '',
        "居住区域": owner_area or '',
        "通过哪种方式找到光予生命": owner_find or '',
        "搜索关键词": owner_keywords or '',
        "善后体重": service_weight or '',
        "费用": service_fee or '',
        "套餐类型": service_type or '',
        "骨灰盒": service_bone or '',
        "纪念品": service_souvenir or '',
        "负责人": service_charge or '',
        "总计": service_sum or '',
        "支付方式": service_payment or '',
        "纪念照留取": note_photo or '',
        "火化视频留取": note_video or '',
        "骨灰领取方式": note_bone or '',
        "纪念品领取方式": note_memorial or '',
        "爱宠随身物品": note_belonging or '',
        "其他备注": note_message or ''
    }

    df = pd.DataFrame([data])

    file_path = "./data.xlsx"

    try:
        existing_df = pd.read_excel(file_path, engine='openpyxl')
        df = pd.concat([existing_df, df], ignore_index=True)
    except FileNotFoundError:
        pass
    
    df.to_excel(file_path, index=False, engine='openpyxl')
    st.success("信息已成功提交！")