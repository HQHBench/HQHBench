import argparse
import json
import re
import time

from tqdm import tqdm
from utils import *
import openai
import os


def evaluate(args):
    ans_file = args.ans_file
    openai_key = args.openai_key
    openai.api_key = openai_key
    num = args.num
    all_hal_results = {f'Model{i+1}': hal_results for i in range(num)}
    all_hal_rates = {f'Model{i+1}': {} for i in range(num)}

    with open(ans_file, 'r', encoding='utf-8') as f:
        model_answers = json.load(f)
    with open('./image_data.json', 'r', encoding='utf-8') as f:
        image_datas = json.load(f)

    for i, answer in tqdm(enumerate(model_answers)):
        image_id = answer['image_id']
        hal_type = answer['type']
        image_data = image_datas[str(image_id)]
        answers_format = ''
        output_format = ''
        for j, text in enumerate(answer['answers']):
            answers_format += f'Answer{j+1}: {text}\n'
            output_format += f'Answer{j+1}: With/Without hallucination, [evidence]\n'

        if hal_type == 'existence':
            prompt = template4existence.format(answer['instruction'], image_data['caption'],
                                               image_data['image_information'], answers_format, output_format)
        else:
            prompt = template.format(answer['instruction'], answer['ground_truth'], image_data['caption'],
                                     image_data['image_information'], answers_format, output_format)

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
        print(prompt)
        print(gpt_output)
        lines = gpt_output.split("\n")
        pattern = re.compile(r"Answer(\d+)")

        for line in lines:
            match = pattern.search(line)
            if not match:
                continue
            answer_id = match.group(1)
            if 'With hallucination' in line:
                all_hal_results[f'Model{answer_id}'][hal_type].append(1)
                all_hal_results[f'Model{answer_id}']['overall'].append(1)
            elif 'Without hallucination' in line:
                all_hal_results[f'Model{answer_id}'][hal_type].append(0)
                all_hal_results[f'Model{answer_id}']['overall'].append(0)

    for hal_type in hal_results.keys():
        for i in range(num):
            all_hal_rates[f'Model{i+1}'][hal_type] = sum(all_hal_results[f'Model{i+1}'][hal_type]) / len(all_hal_results[f'Model{i+1}'][hal_type])

    return all_hal_rates


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--ans_file", type=str, default='path/to/your/answer/file')
    parser.add_argument("--openai_key", type=str, default='your/openai/api/key')
    parser.add_argument("--num", type=int, default=1)
    args = parser.parse_args()
    results = evaluate(args)
    print(results)
