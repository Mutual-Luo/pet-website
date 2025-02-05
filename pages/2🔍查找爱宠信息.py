import streamlit as st
import pandas as pd

st.markdown("<h1 style='text-align: center;'>搜索爱宠🐇信息</h1>", unsafe_allow_html=True)

file_path = "./data.xlsx"
search_phone = st.text_input("请输入家长的联系方式来搜索（输入完成后请按回车键Enter）")

# 1. 检查是否已经加载过数据，如果没有，读取 Excel 数据并缓存到 session_state
if 'data_df' not in st.session_state:
    try:
        data_df = pd.read_excel(file_path, engine='openpyxl')
        data_df = data_df.fillna('')  # 替换空值为字符串
        st.session_state.data_df = data_df  # 保存数据到 session_state
    except FileNotFoundError:
        st.error("找不到数据文件")

# 2. 搜索按钮点击时的操作
if search_phone and 'data_df' in st.session_state:
    # 获取缓存的 DataFrame
    data_df = st.session_state.data_df
    # 筛选出包含搜索电话的记录
    search_results = data_df[data_df['联系方式'].astype(str).str.contains(search_phone, na=False)]

    if not search_results.empty:
        result_count = len(search_results)
        st.write(f"共搜索到 {result_count} 条记录")

        # 3. 修改记录和保存操作
        updated_records = []

        # 使用表单处理修改记录
        with st.form(key="edit_form"):
            for idx, row in search_results.iterrows():
                st.markdown(f"<h5>记录 {idx + 1}</h5>", unsafe_allow_html=True)
                updated_record = row.copy()  # 保留原始记录

                # Pet Info Section
                updated_record['宠物昵称'] = st.text_input("宠物昵称", updated_record['宠物昵称'], key=f"pet_name_{idx}")
                updated_record['性别（宠物)'] = st.radio("性别", ['公', '母'], index=['公', '母'].index(updated_record['性别（宠物)']), key=f"pet_gender_{idx}")
                updated_record['年龄'] = st.text_input("年龄", updated_record['年龄'], key=f"pet_age_{idx}")
                updated_record['品种'] = st.text_input("品种", updated_record['品种'], key=f"pet_type_{idx}")
                updated_record['生日'] = st.text_input("生日", value=pd.to_datetime(updated_record['生日']), key=f"pet_birthday_{idx}")
                updated_record['逝日'] = st.text_input("逝日", value=pd.to_datetime(updated_record['逝日']) if updated_record['逝日'] else None, key=f"pet_death_{idx}")
                updated_record['最想对Ta说的话'] = st.text_area("最想对Ta说的话", updated_record['最想对Ta说的话'], key=f"pet_message_{idx}")

                # Owner Info Section
                updated_record['家长姓名'] = st.text_input("家长姓名", updated_record['家长姓名'], key=f"owner_name_{idx}")
                updated_record['性别（家长)'] = st.radio("性别", ['先生', '女士'], index=['先生', '女士'].index(updated_record['性别（家长)']), key=f"owner_gender_{idx}")
                updated_record['联系方式'] = st.text_input("联系方式", updated_record['联系方式'], key=f"owner_phone_{idx}")
                updated_record['居住区域'] = st.text_input("居住区域", updated_record['居住区域'], key=f"owner_area_{idx}")
                updated_record['通过哪种方式找到光予生命'] = st.text_input("通过哪种方式找到光予生命", updated_record['通过哪种方式找到光予生命'], key=f"owner_find_{idx}")
                updated_record['搜索关键词'] = st.text_input("搜索关键词", updated_record['搜索关键词'], key=f"owner_keywords_{idx}")

                # Service Section
                updated_record['善后体重'] = st.text_input("善后体重", updated_record['善后体重'], key=f"service_area_{idx}")
                updated_record['费用'] = st.text_input("费用", updated_record['费用'], key=f"service_fee_{idx}")
                updated_record['套餐类型'] = st.text_input("套餐类型", updated_record['套餐类型'], key=f"service_type_{idx}")
                updated_record['骨灰盒'] = st.text_input("骨灰盒", updated_record['骨灰盒'], key=f"service_bone_{idx}")
                updated_record['纪念品'] = st.text_input("纪念品", updated_record['纪念品'], key=f"service_souvenir_{idx}")
                updated_record['负责人'] = st.text_input("负责人", updated_record['负责人'], key=f"service_charge_{idx}")
                updated_record['总计'] = st.text_input("总计", updated_record['总计'], key=f"service_sum_{idx}")
                updated_record['支付方式'] = st.radio("支付方式", ['支付宝/微信', '淘宝', '现金', '其他'], index=['支付宝/微信', '淘宝', '现金', '其他'].index(updated_record['支付方式']), key=f"payment_payment_{idx}")

                # Notes Section
                updated_record['纪念照留取'] = st.radio("纪念照留取", ['是', '否'], index=['是', '否'].index(updated_record['纪念照留取']), key=f"note_photo_{idx}")
                updated_record['火化视频留取'] = st.radio("火化视频留取", ['是', '否'], index=['是', '否'].index(updated_record['火化视频留取']), key=f"note_video_{idx}")
                updated_record['骨灰领取方式'] = st.radio("骨灰领取方式", ['自取', '闪送到付', '届时沟通'], index=['自取', '闪送到付', '届时沟通'].index(updated_record['骨灰领取方式']), key=f"note_bone_{idx}")
                updated_record['纪念品领取方式'] = st.radio("纪念品领取方式", ['自取', '闪送到付', '届时沟通'], index=['自取', '闪送到付', '届时沟通'].index(updated_record['纪念品领取方式']), key=f"note_memorial_{idx}")
                updated_record['爱宠随身物品'] = st.radio("爱宠随身物品", ['已交接', '待处理'], index=['已交接', '待处理'].index(updated_record['爱宠随身物品']), key=f"note_belonging_{idx}")
                updated_record['其他备注'] = st.text_area("其他备注", updated_record['其他备注'], key=f"note_message_{idx}")

                # 将修改后的记录添加到列表
                updated_records.append(updated_record)

            st.markdown("<p style='font-size: 12px; text-decoration: underline;'>如果有修改信息，请点击提交并保存，如果没有修改则不用</p>", unsafe_allow_html=True)
            # 提交表单后自动保存
            form_submitted = st.form_submit_button("提交并保存")

            if form_submitted:
                # 将所有更新后的记录合并为一个 DataFrame
                updated_df = pd.DataFrame(updated_records)

                # 4. 更新 Excel 文件，使用 mode='w' 来覆盖原文件
                try:
                    with pd.ExcelWriter(file_path, engine='openpyxl', mode='w') as writer:  # 使用 mode='w' 覆盖文件
                        updated_df.to_excel(writer, index=False, sheet_name='UpdatedData')
                    st.success("修改已保存！")
                    print(updated_df)
                except Exception as e:
                    st.error(f"保存时发生错误: {e}")

    else:
        st.warning("没有找到相关记录。")
else:
    st.warning("请输入家长的联系方式来搜索。")
