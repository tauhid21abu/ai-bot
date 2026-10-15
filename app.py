import urllib.request
import json

# আপনার কপি করা এপিআই কি এখানে বসান
API_KEY = "AQ.Ab8RN6KYdRgeaKjSGwE9-ndFurMX9KSrbr467uzmkI8NxM1VgQ"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

# বটের সিস্টেম ইনস্ট্রাকশন বা চরিত্র
system_prompt = """
তুমি একজন বিশ্বমানের গবেষক এবং শিক্ষক। 
ব্যবহারকারী যখনই কোনো কঠিন বিষয় বা কনসেপ্ট জানতে চাইবে, তখন গতানুগতিক উত্তর না দিয়ে সেটিকে বাস্তব জীবনের সহজ উদাহরণ দিয়ে পানির মতো সহজ করে বুঝিয়ে দেবে। 
গভীরে গিয়ে (Deep Research/Dive) ওই বিষয়ের মূল লজিক, 'কেন' এবং 'কীভাবে' কাজ করে তা ধাপে ধাপে ব্যাখ্যা করবে। উত্তরগুলো সবসময় সুন্দর হেডিং এবং বুলেট পয়েন্টে লিখবে।
"""

print("--- আপনার মোবাইল ডিপ রিসার্চ বট তৈরি! ---")

# চ্যাট লুপ
while True:
    user_input = input("\nআপনি (প্রশ্ন লিখুন): ")
    if user_input.lower() == 'exit':
        break
    
    # এপিআই-এর জন্য ডেটা প্রস্তুত করা
    payload = {
        "contents": [
            {"role": "user", "parts": [{"text": system_prompt + "\n\nব্যবহারকারীর প্রশ্ন: " + user_input}]}
        ]
    }
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(URL, data=data, headers={'Content-Type': 'application/json'})
    
    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            answer = res_data['candidates'][0]['content']['parts'][0]['text']
            print(f"\nবট:\n{answer}")
    except Exception as e:
        print(f"\nত্রুটি দেখা দিয়েছে: {e}")
