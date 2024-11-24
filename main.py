from utils.calculator import generate_challenge
from utils.evaluation import check_answer, cal_precision


total_amount = int(input("请输入问题个数："))
correct = 0

for i in range(total_amount):
    question = generate_challenge()
    print(f"第{i+1}题: {question}")
    user_answer = input("请输入答案: ")
    if check_answer(question, user_answer):
        correct += 1
        result_text = "正确"
    else:
        result_text = "错误"
    print(f"回答{result_text}！")
    
print(f"准确率：{cal_precision(correct, total_amount)}")
