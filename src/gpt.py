import google.generativeai as genai
import os


class Gemini():
    def __init__(self, token):
        genai.configure(api_key = token)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.gen_cfg = genai.types.GenerationConfig(
            max_output_tokens=2000
        )
        
        # create folder for saving temp file
        os.makedirs("img",exist_ok=True)
    
    def send(self, prompt):
        response = self.model.generate_content(prompt, generation_config=self.gen_cfg)
        return response
    
    def upload_img(self, img, img_name="temp.jpg"):
        file_path = os.path.join("img",img_name)
        img.save(file_path)
        cloud_img = genai.upload_file(path=file_path,
                                        display_name=img_name)
        return cloud_img
    
    def send_img(self, cloud_img, prompt):
        response = self.model.generate_content([cloud_img, prompt], generation_config=self.gen_cfg)
        return response
 
def main():
    with open(os.path.join("config.json")) as json_file:
        config = json.load(json_file)
    gemini = Gemini(config["GOOGLE_TOKEN"])
    # Upload the file and print a confirmation.
    img = Image.open('img/jetpack.jpg')
    sample_file = gemini.upload_img(img)

    print(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")
    # Prompt the model with text and the previously uploaded image.
    response = gemini.send_img(sample_file, "Describe how this product might be manufactured.")

    print(response.text)
    
    # response = gemini.model.generate_content("Write a story about a magic backpack.")
    # print(response.text)
 
if __name__ == "__main__":
    from PIL import Image
    import json
    main()