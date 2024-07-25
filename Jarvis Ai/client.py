# # from openai import OpenAI
# # import time

# # # client = OpenAI()
# # # defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# # # if you saved the key under a different environment variable name, you can do something like:
# # client = OpenAI(
# #   api_key="AIzaSyBuUxLkJZ4WU-Ny6cVNc_PkNxBYObxXGYc",
# # )


# # # completion = client.chat.completions.create(
# # #   model="gpt-4o-mini",
# # #   messages=[
# # #     {"role": "system", "content": "You are a Virtual Assistant named Jarvis , skilled in general tasks like Alexa and Google"},
# # #     {"role": "user", "content": "what is python"}
# # #   ]
# # # )

# # # print(completion.choices[0].message)

# import google.generativeai as genai
# import os

# # env:AIzaSyBuUxLkJZ4WU-Ny6cVNc_PkNxBYObxXGYc="AIzaSyBuUxLkJZ4WU-Ny6cVNc_PkNxBYObxXGYc"


# genai.configure(api_key="AIzaSyBuUxLkJZ4WU-Ny6cVNc_PkNxBYObxXGYc")

# model = genai.GenerativeModel('gemini-1.5-flash')

# response = model.generate_content("what is python")
# # response = [
# #     {"role": "system", "content": "You are a Virtual Assistant named Jarvis , skilled in general tasks like Alexa and Google"},
# #     {"role": "user", "content": "what is python"}
# #   ]
# print(response.text)