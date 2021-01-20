#######################
# Test Processing II  #
#######################


def digits_to_words(input_string):
    """
    인풋으로 받는 스트링에서 숫자만 추출하여 영어 단어로 변환하여 단어들이 연결된 스트링을 반환함
    아래의 요건들을 충족시켜야함
    * 반환하는 단어들은 영어 소문자여야함
    * 단어들 사이에는 띄어쓰기 한칸이 있음
    * 만약 인풋 스트링에서 숫자가 존재하지 않는 다면, 빈 문자열 (empty string)을 반환함

        Parameters:
            input_string (string): 영어로 된 대문자, 소문자, 띄어쓰기, 문장부호, 숫자로 이루어진 string
            ex - "Zip Code: 19104"

        Returns:
            digit_string (string): 위 요건을 충족시킨 숫자만 영어단어로 추출된 string
            ex - 'one nine one zero four'

        Examples:
            >>> import text_processing2 as tp2
            >>> digits_str1 = "Zip Code: 19104"
            >>> tp2.digits_to_words(digits_str1)
            'one nine one zero four'
            >>> digits_str2 = "Pi is 3.1415..."
            >>> tp2.digits_to_words(digits_str2)
            'three one four one five'
    """


    # 오직 정수인 값 만 찾아내기 위해서 
    number_string = ""
    number = ['0','1','2','3','4','5','6','7','8','9']

    for i in input_string:
        if i in number:
            number_string += i
    
    # 정수가 존재하지 않으면 공백 출력
    if number_string == "":
        return ""

    # 숫자(정수) 형태의 문자열을 문자 형태로 변환
    digit_string = ""
    number_dict = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four',
                   '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'} 

    
    digit_string += number_dict[number_string[0]]

    for i in range(1,len(number_string)):
        digit_string += " "
        digit_string += number_dict[number_string[i]]

    return digit_string


"""
컴퓨터 프로그래밍에 많은 명명 규칙이 있지만, 두 규칙이 특히 흔히 쓰입니다. 
첫번째로는, 변수 이름을 'underscore'로 나눠준다거나, (ex. under_score_variable)
두번째로는, 변수 이름을 대소문자 구별해 구분자 (delimiter)없이 쓰는 경우가 있습니다. 
이 두번째의 경우에는 첫번째 단어는 소문자로, 그 후에 오는 단어들의 첫번째 글자들은 대문자로 쓰입니다 (ex. camelCaseVariable). 
"""


def to_camel_case(underscore_str):
    """
    이 문제에서 첫번째 규칙 'underscore variable' 에서 두번째 규칙 'camelcase variable'으로 변환함
    * 앞과 뒤에 여러개의 'underscore'는 무시해도 된
    * 만약 어떤 변수 이름이 underscore로만 이루어 진다면, 빈 문자열만 반환해도 됨

        Parameters:
            underscore_str (string): underscore case를 따른 스트링

        Returns:
            camelcase_str (string): camelcase를 따른 스트링

        Examples:
            >>> import text_processing2 as tp2
            >>> underscore_str1 = "to_camel_case"
            >>> tp2.to_camel_case(underscore_str1)
            "toCamelCase"
            >>> underscore_str2 = "__EXAMPLE__NAME__"
            >>> tp2.to_camel_case(underscore_str2)
            "exampleName"
            >>> underscore_str3 = "alreadyCamel"
            >>> tp2.to_camel_case(underscore_str3)
            "alreadyCamel"
    """
    
    # "_" 가 존재하지 않으면 그대로 출력 (iuput은 underscore case따른다 하지 않았나? ex. alreayCamel) 
    if "_" not in underscore_str:
        return underscore_str

    # 모두 소문자로 변환
    small_str = underscore_str.lower()
    
    # 시퀀스의 정뱡향으로 앞에 존재하는 '_' 제거 
    forward_str = []
    flag = False

    for i in small_str:
        if i != '_':
            flag = True

        if flag == True:
            forward_str.append(i)
    
    # 남아 있는 문자가 없으면 빈 문자열 출력
    if forward_str == []:
        return ""

    # 시퀀스 역방향으로 맨 뒤에 존재하는 '_' 제거
    backward_str = []
    flag = False

    while forward_str:
        i = forward_str.pop()
        if i != '_':
            flag = True

        if flag == True:
            backward_str.insert(0, i)

    
    # 문자열 중간에 위치하는 '_'뒤에 문자는 대문자로 변환
    camelcase_str = ""
    pre = True

    for i in backward_str:
        if i == '_' and pre == True:
            pre = False

        elif i != '_' and pre == False:
            camelcase_str += i.upper()
            pre = True

        elif i != '_' and pre == True:
            camelcase_str += i

    return camelcase_str


