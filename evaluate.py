import argparse
import json
import re
import time

from tqdm import tqdm
from utils import *
import openai


def evaluate(args):
    ans_file = args.ans_file
    openai_key = args.openai_key
    openai.api_key = openai_key
    hal_result = {}
    hal_type_main_hal_rates = {}
    main_hal_rates = []
    overall_hal_rates = []
    extra_hal_claims = []
    with open(ans_file, 'r', encoding='utf-8') as f:
        model_answers = json.load(f)
    with open('./image_data.json', 'r', encoding='utf-8') as f:
        image_datas = json.load(f)
        
    for i, answer in tqdm(enumerate(model_answers)):
        image_id = answer['image_id']
        hal_type = answer['type']
        if hal_type not in hal_type_main_hal_rates.keys():
            hal_type_main_hal_rates[hal_type] = []

        image_data = image_datas[str(image_id)]
        prompt = template.format(answer['instruction'], answer['ground_truth'], image_data['caption'],
                                 image_data['image_information'], answer['answer'])
        pattern_main = re.compile(r"Answer:")
        pattern_extra = re.compile(r"Extra Contradictory Claims: ?(\d+)")
        main_hal = None
        claim_num = None
        while main_hal is None or claim_num is None:
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt}
                    ]
                )
                gpt_output = response.choices[0].message.content
                lines = gpt_output.split("\n")
                for line in lines:
                    match_main = pattern_main.search(line)
                    match_extra = pattern_extra.search(line)
                    if match_main:
                        if 'Incorrect' in line:
                            main_hal = 1
                        elif 'Correct' in line:
                            main_hal = 0
                    if match_extra:
                        claim_num = int(match_extra.group(1))
            except Exception as e:
                print(e)
                time.sleep(10)
        if main_hal + claim_num > 0:
            overall_hal = 1
        else:
            overall_hal = 0
        main_hal_rates.append(main_hal)
        overall_hal_rates.append(overall_hal)
        extra_hal_claims.append(claim_num)
        hal_type_main_hal_rates[hal_type].append(main_hal)
        
    hal_result['Overall Hal%'] = sum(overall_hal_rates) / len(overall_hal_rates)
    hal_result['Main Hal%'] = sum(main_hal_rates) / len(main_hal_rates)
    hal_result['Extra #Hal'] = sum(extra_hal_claims) / len(extra_hal_claims)
    for hal_type in hal_type_main_hal_rates.keys():
        hal_result[f'{hal_type} Hal%'] = sum(hal_type_main_hal_rates[hal_type]) / len(hal_type_main_hal_rates[hal_type])
    return hal_result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--ans_file", type=str, default='path/to/your/answer/file')
    parser.add_argument("--openai_key", type=str, default='your/openai/api/key')
    args = parser.parse_args()
    results = evaluate(args)
    print(results)
