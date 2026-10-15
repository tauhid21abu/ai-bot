import google.generativeai as genai
import streamlit as st

# পৃষ্ঠার টাইটেল
st.set_page_config(
    page_title="Mobile Deep Research Bot", page_icon="🤖", layout="centered"
)

st.title("🤖 আমার মোবাইল ডিপ রিসার্চ বট")
st.write(
    "এখানে আপনার প্রশ্ন লিখুন, এআই ডিপ রিসার্চ করে উত্তর দেওয়া শুরু করবে।"
)

# আপনার এপিআই কি এখানে বসান
API_KEY = "AQ.Ab8RN6KYdRgeaKjSGwE9-ndFurMX9KSrbr467uzmkI8NxM1VgQ"

if API_KEY == "আপনার_এপিআই_কি_এখানে_দিন":
    st.warning("AQ.Ab8RN6KYdRgeaKjSGwE9-ndFurMX9KSrbr467uzmkI8NxM1VgQ")
else:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-pro-latest")

    # চ্যাট ইনপুট বক্স
    user_prompt = st.text_area("আপনার গবেষণার বিষয়টি এখানে লিখুন:")

    if st.button("রিসার্চ শুরু করুন"):
        if user_prompt:
            with st.spinner("ডিপ রিসার্চ চলছে, একটু অপেক্ষা করুন..."):
                try:
                    response = model.generate_content(user_prompt)
                    st.subheader("ফলাফল:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"একটি সমস্যা হয়েছে: {e}")
        else:
            st.warning("আগে কিছু একটা লিখুন!")
