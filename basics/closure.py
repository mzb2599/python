def anonymous():
    a = "Workin with closures"

    def message():
        print(a)


    return message()

af = anonymous()
af()
print("Hii")
# def outerFunction(text):
#     text = text

#     def innerFunction():
#         print(text)

#     return innerFunction  # Note we are returning function WITHOUT parenthesis


# if __name__ == '__main__':
#     myFunction = outerFunction('Hey!')
#     myFunction()
