import language_evaluation
from pprint import PrettyPrinter
pprint = PrettyPrinter().pprint

predicts = ['i am a boy', 'she is a girl']
answers = ['am i a boy ?', 'is she a girl ?']

evaluator = language_evaluation.CocoEvaluator()
results = evaluator.run_evaluation(predicts, answers)
pprint(results)
# {'Bleu_1': 0.9999999997500004,
#  'Bleu_2': 0.5773502690332603,
#  'Bleu_3': 4.3679023223468616e-06,
#  'Bleu_4': 1.4287202142987477e-08,
#  'CIDEr': 3.333333333333333,
#  'METEOR': 0.43354749322305886,
#  'ROUGE_L': 0.75,
#  'SPICE': 0.6666666666666666}