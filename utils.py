template = """###Task:
Given the input instruction, the ground truth answer, and detailed image information, evaluate whether the LMM response is aligned with the image content.

###Evaluation Criteria:
Answer Correctness: Assess whether the model's response accurately matches the ground truth answer in terms of semantic consistency.

Extra Contradictory Claims: Examine whether the response includes additional factual claims beyond the answer to the question that contradict the image information (e.g., objects, actions, attributes). If such contradictions are present, quantify their occurrence and provide evidence.

Scope of Evaluation: Focus only on explicit factual claims within the model's response. Analytical reasoning or the model’s process of deriving an answer should be excluded from contradiction assessments. Incorrect answers should not be counted as part of the additional contradictory claims.

For each response, provide a judgment supported by evidence:
Answer: Correct / Incorrect
Extra Contradictory Claims: [Number]，[Evidence1], [Evidence2], ...

###Instruction:
{}

###Ground Truth Answer:
{}

###Image Caption:
{}

###Image Details:
{}

###Model Responses:
{}

###Output Format:
Answer: Correct / Incorrect
Extra Contradictory Claims: [Number]，[Evidence1], [Evidence2], ..."""
