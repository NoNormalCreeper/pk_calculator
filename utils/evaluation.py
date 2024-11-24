def check_answer(question: str, user_answer: str) -> bool:
    try:
        question_answer = float(eval(question))
        user_answer = float(user_answer.strip())
        return abs(question_answer - user_answer) <= 0.01
    except Exception as e:
        return False

def cal_precision(correct, total) -> float:
    return round(correct / total, 2)
