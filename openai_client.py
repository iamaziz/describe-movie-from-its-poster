from openai import OpenAI

class OpenAIClient():
    def __init__(self) -> None:
        self.client = OpenAI() # assumes you have the OPENAI_API_KEY set in your environment

    def chat(self, messages, model="gpt-3.5-turbo"):
        return self.client.chat.completions.create(messages=messages, model=model)

    def get_embedding(self, text: str,  model="text-embedding-ada-002") -> list[float]:
        text = text.replace("\n", " ")
        resp = self.client.embeddings.create(input=[text], model=model)
        return resp.data[0].embedding

    def describe_images(self, full_plot: str, image_url: str, model_name="gpt-4-vision-preview") -> str:
        # based on: https://platform.openai.com/docs/guides/vision
        
        client = self.client
        
        prompt =  f"Given the following movie plot and its image poster. What the movie poster tells about the plot? here is the plot: \n\n {full_plot}"

        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "user",
                 "content": [{"type": "text", "text": prompt}, {"type": "image_url", "image_url": {"url": image_url}}]
                 }],
        max_tokens=300,
        )

        return response.choices[0].message.content, prompt


if __name__ == "__main__":
    client = OpenAIClient()
    
    # -- chat
    # messages = [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "What is the purpose of life?"}]
    # print(client.chat(messages=messages))

    # get_embedding
    text = "Once upon a time"
    print(client.get_embedding(text))