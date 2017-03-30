def non_empty(a_func):
    def wrapTheFunction():
        print("До исполнения a_func()" )
        lst=[]
        lst=a_func()
        print(lst)
        i=0
        while i<len(lst):
                if lst[i]=='' or lst[i]=='None':
                    del lst[i]
                else:
                    i+=1
        print(lst)
        print("После исполнения a_func()" )
    return wrapTheFunction
@non_empty
def get_pages():
    #print("Я функция, которая требует декорации")
    return ['chapter1', ' ', 'contents', '', 'line1','None','None']
get_pages()


