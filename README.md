## HQH Benchmark

**HQH** is a high-quality hallucination benchmark for LVLMs built on  [Visual Genome](https://arxiv.org/pdf/1602.07332v1.pdf) dataset. It is created to evaluate the performance of LVLMs across different types of hallucination, highlighting their shortcomings. It consists of 4000 free-form VQA image-instruction pairs, with 500 pairs for each hallucination type.

<p align="center">
<img src="https://github.com/HQHBench/HQHBench/blob/main/assets/typeexample.png" alt="typeexample" width="600" />
</p>

### Data

You can download the images from this [LINK](https://1drv.ms/u/c/3990e975c588b26f/EUhh8nJwRRpMkWk4xItqMQMB6phnWkdCykliVUdlUs4hNw). The image annotations are saved in `image_data.json`.

Our evaluation data is saved in `HQH.json`, with the following format:

```python
[
    ...
    {"id": 633,
    "image_id": 2325616,
    "image": "./images/2325616.jpg",
    "instruction": "What is the man doing?",
    "ground_truth": "Playing tennis.",
    "type": "action"},
    ...
]
```

where `id` refers to the data id in HQH, `image_id` refers to the image id from [Visual Genome](https://arxiv.org/pdf/1602.07332v1.pdf), `images` refers to the image path, `instruction` refers to the instruction, `ground_truth` refers to the ground truth answer, `type` refers to the hallucination type. 


### Evaluation

We leverage [GPT-4o](https://platform.openai.com/docs/overview) to calculate the hallucination rate as our evaluation metric.

Our evaluation code is provided in `evaluate.py`. You can obtain the evaluation results by running:

```python
python evaluate.py --ans_file path/to/your/answer/file --openai_key your/openai/api/key --num model/num/for/evaluation
```

The answer of LVLMs should be organized in a json file in the following format:

```python
[
    ...
    {"id": 633,
    "image_id": 2325616,
    "image": "./images/2325616.jpg",
    "instruction": "What is the man doing?",
    "ground_truth": "Playing tennis.",
    "type": "action",
    "answer": "He is about to hit the ball with his tennis racquet"},
    ...
]
```

i.e., add an "answer" field to each instance in `HQH.json`.

### Results

<p align="center">
    <img src="https://github.com/HQHBench/HQHBench/blob/main/assets/rada.png" alt="rada" width="400" />
</p>


## Related Projects

- [BLIP-2](https://github.com/salesforce/LAVIS/tree/main/projects/blip2)
- [InstructBLIP](https://github.com/salesforce/LAVIS/blob/main/projects/instructblip)
- [InternLM-XComposer](https://github.com/InternLM/InternLM-XComposer)
- [LLaVA-1.5](https://github.com/haotian-liu/LLaVA)
- [LLaVA-OneVision](https://github.com/LLaVA-VL/LLaVA-NeXT)
- [MiniGPT4](https://github.com/Vision-CAIR/MiniGPT-4)
- [MiniGPT-v2](https://github.com/Vision-CAIR/MiniGPT-4)
- [Otter](https://github.com/Vision-CAIR/MiniGPT-4)
- [Qwen-VL](https://github.com/QwenLM/Qwen-VL)
- [Qwen2-VL](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct)
- [Shikra](https://github.com/shikras/shikra)
- [GLM-4V](https://github.com/THUDM/GLM-4)
- [Phi-3-Vison](https://huggingface.co/microsoft/Phi-3-vision-128k-instruct)
- [Emu2-Chat](https://huggingface.co/BAAI/Emu2-Chat)
- [MiniCPM](https://github.com/OpenBMB/MiniCPM)

- [Gemini-1.5-Pro](https://ai.google.dev/gemini-api/docs)
- [GPT-4o](https://platform.openai.com/docs/overview)







