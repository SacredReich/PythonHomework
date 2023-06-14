# К 5 семинару
# Принимает число и его степень, выдает ответ
def degre_of_input_number(num, degree, answer):
    if degree == 0:
        return 1
    while degree > 1:
        return degre_of_input_number(num, degree - 1, answer=answer*num)
    return answer
# Другой вариант:
# def degre_of_input_number(num, degree):
#     if (degree == 1):
#         return (num)
#     if (degree != 1):
#         return (num * degre_of_input_number(num, degree - 1))


def summ_of_2numbs_but_step1(a, b):
    if a > b:
        if b > 0:
            return (summ_of_2numbs_but_step1(a+1, b-1))
        return a
    if a > 0:
        return (summ_of_2numbs_but_step1(a-1, b+1))
    return b
