### Evaluating the Quality of Hallucination Benchmarks for Large Vision-Language Models

This is the official repo of our paper: Evaluating the Quality of Hallucination Benchmarks for Large Vision-Language Models.

***Abstract -*** LVLMs have been plagued by the issue of hallucination. To evaluate the degree of hallucination in LVLMs, previous works have proposed a series of benchmarks featuring different types of tasks and evaluation metrics. However, we find that the quality of the existing hallucination benchmarks varies, with some suffering from problems, e.g., inconsistent evaluation results under repeated tests, and misalignment with human evaluation. To this end, we propose a **H**allucination benchmark **Q**uality **M**easurement framework (**HQM**), which leverages various indicators to assess their reliability and validity. Furthermore, based on the results of our quality measurement, we construct a **H**igh-**Q**uality **H**allucination Benchmark (**HQH**) for LVLMs,  covering comprehensive types of hallucination.

#### HQM Framework

Inspired by psychometrics, HQM focuses on the reliability and validity of hallucination benchmarks. Specifically, for reliability we explore test-retest reliability and parallel-forms reliability, while for validity we examine criterion validity and coverage of hallucination types. The overview of HQM is as follows:

<img src="D:\Desktop\nips\overview2.png" alt="overview2" style="zoom: 50%;" />



#### HQH Benchmark

HQH is a high-quality hallucination benchmark for LVLMs built on  [Visual Genome](https://arxiv.org/pdf/1602.07332v1.pdf) dataset. It is created to evaluate the performance of LVLMs across different types of hallucination, highlighting their shortcomings. It consists of 1600 free-form VQA image-instruction pairs, with 200 pairs for each hallucination type.

<img src="D:\Desktop\nips\typeexample.png" alt="typeexample" style="zoom: 40%;" />

##### Data

You can download the images from this [LINK](https://1drv.ms/u/s!AnyDvWHXFwUHbqhRo0p0aADKrho?e=3wXoKj). The image annotations are saved in `image_data.json`.

Our evaluation data is saved in `HQH.json`, with the following format:

```python
[
    {"id": 27, 
    "image_id": 150494, 
    "images": ["./images/150494.jpg"],
    "instruction": "What is the man in a suit doing?",
    "ground_truth": "Giving a speech.",
    "type": "action"},
    ...
]
```

where `id` refers to the data id in HQH, `image_id` refers to the image id from [Visual Genome](https://arxiv.org/pdf/1602.07332v1.pdf), `images` refers to the image path, `instruction` refers to the instruction, `ground_truth` refers to the ground truth answer, `type` refers to the hallucination type. 

Note that there is no ground truth in existence hallucination type as the provided image annotations are informative enough.

##### Evaluation

We leverage [GPT-3.5](https://platform.openai.com/docs/overview) to calculate the hallucination rate as our evaluation metric.

Our evaluation code is provided in `evaluate.py`. You can obtain the evaluation results by running:

```python
python evaluate.py --ans_file path/to/your/answer/file
```

The answer of LVLMs should be organized in a json file in the following format:

```json
[
    {"id": 27, 
    "image_id": 150494, 
    "images": ["./images/150494.jpg"],
    "instruction": "What is the man in a suit doing?",
    "ground_truth": "Giving a speech.",
    "type": "action",
    "answer": "The man in the suit is giving a speech to a group of soldiers."},
    ...
]
```

i.e., add an "answer" field to each instance in `HQH.json`.

##### Results

<img src="D:\Desktop\nips\rada.png" alt="rada" style="zoom: 40%;" />

<img src="D:\Desktop\HQH-github\leaderboerd.png" style="zoom: 50%;" />

#### Related Projects

- [BLIP-2](https://github.com/salesforce/LAVIS/tree/main/projects/blip2)
- [InstructBLIP](https://github.com/salesforce/LAVIS/blob/main/projects/instructblip)
- [InternLM-XComposer](https://github.com/InternLM/InternLM-XComposer)
- [LLaVA-1.5](https://github.com/haotian-liu/LLaVA)
- [MiniGPT4](https://github.com/Vision-CAIR/MiniGPT-4)
- [MiniGPT-v2](https://github.com/Vision-CAIR/MiniGPT-4)
- [Otter](https://github.com/Vision-CAIR/MiniGPT-4)
- [Qwen-VL](https://github.com/QwenLM/Qwen-VL)
- [Shikra](https://github.com/shikras/shikra)
- [Gemini-Vision-Pro](https://ai.google.dev/gemini-api/docs)
- [GPT-4o](https://platform.openai.com/docs/overview)






