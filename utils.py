template = """Given the input instruction, ground truth answer and detailed image information, please determine whether the response provided by a Large Vision-Language Model (LVLM) contains any hallucination. Hallucination here refers to the situation that the generated response is inconsistent with the input image. 
  
Please note that the ground truth answer and image information only contain factual information and may not be completely comprehensive in describing all the objects and their attributes. Detailed ana-lysis or reasoning in LVLM response should be encouraged and not considered as hallucination.

To evaluate the LVLM responses, you need to provide brief evidence to support your judgment. 

###Evaluation criteria:
-Without hallucination: The LVLM response is semantically similar to the ground truth answer and does not contain any contradictory factual claim with the provided information.
-With hallucination: The LVLM response is completely different from the ground truth answer, or contains a contradictory factual claim about an object, action, attribute, or any other detail that is not grounded in the provided information.

###Instruction:\n{}\n
###Ground Truth:\n{}\n
###Image Caption:\n{}\n
###Image Details:\n{}\n
###Model Response:\n{}
###Output Format:\nWith/Without hallucination, [evidence].\n
"""

template4existence = """Given the input instruction and detailed image information, please determine whether the response provided by a Large Vision-Language Model (LVLM) contains any hallucination. Hallucination here refers to the situation that the generated response is inconsistent with the input image. 

Please note that the image information only contain factual information and may not be completely comprehensive in describing all the objects and their attributes. Detailed ana-lysis or reasoning in LVLM response should be encouraged and not considered as hallucination.

To evaluate the LVLM responses, you need to provide brief evidence to support your judgment. 

###Evaluation criteria:
-Without hallucination: The LVLM response does not contain any contradictory factual claim with the provided information.
-With hallucination: The LVLM response contains a contradictory factual claim about an object, action, attribute, or any other detail that is not grounded in the provided information.

###Instruction:\n{}\n
###Image Caption:\n{}\n
###Image Details:\n{}\n
###Model Response:\n{}
###Output Format:\nWith/Without hallucination, [evidence].\n
"""

hal_results = {'overall': [], 'action': [], 'attribute': [], 'comparison': [], 'count': [], 'environment': [],
               'existence': [], 'OCR': [], 'relation': []}
