class employee:
    def __init__(self):
        print(id(self))
        self.id=123
        self.salary=50000
        self.designation='SDE'
    def travel(self,destination):
        pass
        # print(f'employee is now travelling to {destination}')
        
sam=employee()

# sam.name='saikumar'
# print(sam.name)
# print(id(sam))
# s=employee()
# print(id(s)+1)
# print(sam.salary)
# print(sam.id)

# sam.travel('kerala')
