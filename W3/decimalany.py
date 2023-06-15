from pythonds.basic.stack0 import Stack0


def decany(num, type):
    digits = '0123456789ABCDE'
    final = ''
    st = Stack0()
    while num > 0:
        st.push(num % type)
        num = num//type
    while not st.ifempty():
        final = final+digits[st.pop()]
    return final
