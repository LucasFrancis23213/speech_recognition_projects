from transformers import pipeline


class TextEmotionClassifier:
    def __init__(self, model: str = 'sentiment-analysis'):
        # 从pipeline中选择预训练的情感分析模型
        self.model = pipeline(model=model)
        self.result = []

    def analyze_emotion(self, text: str):
        analyze_output = self.model(text)
        self.result.append(analyze_output)
        return analyze_output

    def get_result(self, clear: bool = True):
        if clear:
            ans = self.result
            self.result.clear()
            return ans
        else:
            return self.result



