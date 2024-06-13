import argparse
import json
import time

from tqdm import tqdm
from utils import *
import openai


def evaluate(args):
    ans_file = args.ans_file
    openai_key = args.openai_key
    openai.api_key = openai_key
    hal_rates = {}
    with open(ans_file, 'r', encoding='utf-8') as f:
        model_answers = json.load(f)
    with open('./image_data.json', 'r', encoding='utf-8') as f:
        image_datas = json.load(f)
    for i, answer in tqdm(enumerate(model_answers)):
        image_id = answer['image_id']
        hal_type = answer['type']
        image_data = image_datas[str(image_id)]

        if hal_type == 'existence':
            prompt = template4existence.format(answer['instruction'], image_data['caption'], image_data['image_information'], answer['answer'])
        else:
            prompt = template.format(answer['instruction'], answer['ground_truth'], image_data['caption'], image_data['image_information'], answer['answer'])

        gpt_output = None
        while gpt_output is None:
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt}
                    ]
                )
                gpt_output = response.choices[0].message.content
            except Exception as e:
                print(e)
                time.sleep(10)

        if 'With hallucination' in gpt_output:
            hal_results[hal_type].append(1)
            hal_results['overall'].append(1)
        elif 'Without hallucination' in gpt_output:
            hal_results[hal_type].append(0)
            hal_results['overall'].append(0)

    for hal_type in hal_results.keys():
        hal_rates[hal_type] = sum(hal_results[hal_type]) / len(hal_results[hal_type])

    return hal_rates


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--ans_file", type=str, default='path/to/your/answer/file')
    parser.add_argument("--openai_key", type=str, default='your/openai/api/key')
    args = parser.parse_args()
    results = evaluate(args)
    print(results)