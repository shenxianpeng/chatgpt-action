import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_response(prompt: str) -> str:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Python 的发展前景怎么样？",
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"]
    )
    message = (response.choices[0].text).strip()
    return message


def main():
    msg = get_response("How about China?")
    print(msg)


if __name__ == "__main__":
    main()
