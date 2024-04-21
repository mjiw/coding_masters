def solution(src):
    answer = ''
    one=[x for x in src.split('0') if x]
    zero=[x for x in src.split('1') if x]
    one_length=list()
    zero_length=list()
    result=list()

    for i in one:
        one_length.append(len(i))
    for i in zero:
        zero_length.append(len(i))

    text=''
    for i in range(len(one_length)):
        text=chr(64+one_length[i])
        one_length[i]=text
    for i in range(len(zero_length)):
        text=chr(64+zero_length[i])
        zero_length[i]=text

    result.append(src[0])
    if result[0]=='1':
        max_length = max(len(one_length), len(zero_length))
        for i in range(max_length):
            if i < len(one_length):
                result.append(one_length[i])
            if i < len(zero_length) and not zero_length[i]:
                break
            elif i < len(zero_length):
                result.append(zero_length[i])

    else:
        max_length = max(len(one_length), len(zero_length))
        for i in range(max_length):
            if i < len(zero_length):
                result.append(zero_length[i])
            if i < len(one_length) and not one_length[i]:
                break
            elif i < len(one_length):
                result.append(one_length[i])

    answer=''.join(result)
    return answer