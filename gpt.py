import google.generativeai as genai


class Gemini():
    def __init__(self, token):
        genai.configure(api_key = token)
        self.model = genai.GenerativeModel('gemini-pro')
        self.gen_cfg = genai.types.GenerationConfig(
            max_output_tokens=2000
        )
    
    def send(self, prompt):
        response = self.model.generate_content(prompt, generation_config=self.gen_cfg)
        return response
 
def main():
    gemini = Gemini()
    prompt = "你好，你可以用中文回復我嗎?\nWho are you?"
    response = gemini.send(prompt)
    print(response.text)
    # prompt = "Who are you?"
    # response = model.generate_content(prompt)
    # print(response.text)
 
if __name__ == "__main__":
    main()