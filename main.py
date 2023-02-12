import argparse
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_response(prompt: str) -> str:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    message = (response.choices[0].text).strip()
    return message


def main():
    parser = argparse.ArgumentParser(prog="ChatGPT GitHub Actions", description="Test ChatGPT in github action.")
    parser.add_argument(
        '-p',
        '--prompt',
        type=str,
        required=True,
        help="A well-written prompt provides to ChatGPT"
    )
    args = parser.parse_args()
    prompt = args.prompt

    response = get_response(prompt)
    print(response)


if __name__ == "__main__":
    main()
