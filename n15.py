def pre_process(a=0.97):
    def wrapTheFunction(a_func):
        print("До исполнения a_func()" )
        print(s)
        i=0
        for i in range(len(s)):
             s[i]=s[i]-a*s[i-1]
       
        print("После исполнения a_func()" )
        print(s)
    return wrapTheFunction
s=[3,5,2,5,8,2,5,6,7]
@pre_process(a=0.93)
def plot_signal(s): 
  for sample in s: 
     print(sample)


 
##def get_pages():
##    #print("Я функция, которая требует декорации")
##    return ['chapter1', '', 'contents', '', 'line1','None','None']
##get_pages()


